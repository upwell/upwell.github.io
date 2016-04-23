Title: python GIL 整理
Date: 2016-04-18 13:36
Tags: python
Category: tech

## GIL 是什么
GIL 是 Global Interpreter Lock 的缩写，全局解释器锁。在 CPython 中，GIL 被用来防止多个原生线程同时执行。

其实并不是所有的 Python 实现都使用 GIL，Python 实现中，包含 GIL 的有：

- CPython (我们通常说到 Python 时指的就是这个实现)
- PyPy

没有 GIL 机制的实现：

- Jython (Java)
- IronPython (.NET)

## 为什么 CPython 中使用 GIL
主要是因为 CPython 的内存管理不是线程安全的。线程安全，主要是要保护共享数据，通常有两种做法：

- 对每个共享数据进行操作时采用独立的细粒度锁进行保护
- 使用一个全局粗粒度锁保护所有的共享数据 （GIL）

这两种做法各有优缺点：

- 细粒度锁可以利用多CPU，多个线程可以同时执行，发挥并发的优势，但锁是有开销的，而且程序复杂度也较高；
- 全局锁正好相反，两个线程不能同时执行，但是单线程执行时效率会更高；

采用 GIL 而不是细粒度锁的好处：

- 单线程程序会更快
- 编写基于C的扩展程序时更容易
- 使用C库时更容易，不用考虑C库是否线程安全

减小 GIL 影响的做法：

- 提供了释放 GIL 的机制，实际上标准库中，在每个 blocking i/o 的调用时候，GIL 都会被释放掉，所以对于IO型的程序，GIL 并不会导致性能下降;
- 对于像 NumPy 这样的计算型库，在调用C或者Fortran时，总是尽可能的先释放掉 GIL，保证其它的线程可以继续执行;

实际上移除 GIL 的讨论一直都存在，但是到目前为止都还没有一个很好的实现，[Guido 也承认移除 GIL 是很困难的][1]。之前的 Patch 会使单线程的性能下降很多，但对多线程程序的性能提升又有限，所以被弃用。


## References
<https://wiki.python.org/moin/GlobalInterpreterLock>  
<http://programmers.stackexchange.com/questions/186889/why-was-python-written-with-the-gil>  
<http://stackoverflow.com/questions/265687/why-the-global-interpreter-lock>  
<https://docs.python.org/2/faq/library.html#can-t-we-get-rid-of-the-global-interpreter-lock>  
<http://www.dabeaz.com/GIL/>  
<http://python-notes.curiousefficiency.org/en/latest/python3/multicore_python.html>  

[1]: <http://www.artima.com/weblogs/viewpost.jsp?thread=214235>
