Title: python 自定义 exception 的原则
Date: 2016-09-01 16:17
Tags: python,exception
Category: tech

# 自定义 exception 的困扰
在 Web 编程的时候，经常会遇到一种场景，内部接口实现的时候会出现各种错误的情况，对于一些错误又不能直接在接口中处理，大部分时候可能需要告知调用者错误发生了，然后由调用者 (view) 来处理并返回相应的信息给 UI。

这种时候，我们通常想的是，为每种错误自定义一个 exception，然后 raise 出去，有调用者 except 后再进行相应的处理，这样会导致大量的自定义 exception，毕竟错误（异常）场景还是很多的。


# 参考
[Proper way to define customer exception][1]
[Write cleaner python user exceptions][2]
[Robust exception handling][3]
[modules should never raise core python exceptions][4]


[1]: http://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
[2]: https://jeffknupp.com/blog/2013/02/06/write-cleaner-python-use-exceptions/
[3]: http://eli.thegreenplace.net/2008/08/21/robust-exception-handling
[4]: https://www.reddit.com/r/Python/comments/51ksht/modules_should_never_raise_core_python_exceptions/
