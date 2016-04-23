Title: first class objects
Date: 2016-04-18 13:36
Tags: python
Category: tech

我们经常听到说，python 中一切皆对象，还有就是`function is first class object`，到底 first class object 是什么意思？
[维基百科][1]里面是这样定义 `first class` 的：

> In programming language design, a first-class citizen (also type, object, entity, or value) in a given programming language is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable.

对应到 python 中，也就是说函数跟普通的变量一样，可以被创建，传递，赋值，返回。

实际上，python 的[设计目标][2]是 `Everything is a object and first class everything`.

> By this, I meant that I wanted all objects that could be named in the language (e.g., integers, strings, functions, classes, modules, methods, etc.) to have equal status. That is, they can be assigned to variables, placed in lists, stored in dictionaries, passed as arguments, and so forth.


<http://stackoverflow.com/questions/245192/what-are-first-class-objects>

[1]: https://en.wikipedia.org/wiki/First-class_citizen
[2]: http://python-history.blogspot.jp/2009/02/first-class-everything.html
