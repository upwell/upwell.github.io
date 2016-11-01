Title: WSGI 研究
Date: 2016-10-31 11:15
Tags: wsgi,python
Category: tech

## 现象
之前一直以为Django/Flask是实现了完整的http协议的，最近遇到协议不支持才发现原来并非如此。

实际遇到的问题是App上传图片到服务器时，如果django挂在nginx下，图片可以上传成功，但如果直接用runserver跑起来的话，上传失败。通过抓包分析，发现App上传图片时，http header里面Transfer-Encoding的值是Chunked。

Google 之后，发现并没有很多关于这方面的讨论，一致的说法是这并不是Django的问题，其实是WSGI spec中不支 Content-Length为空的情况。单步调试django的代码也发现确实如此，遇到Content-Length为空或0时，就直接不再解析body了。django的代码中也没法任何处理Chunked的逻辑。

[参考一][5]  [参考二][6]  [参考三][7]

## 疑问
### WSGI是什么呢？
[WSGI][9]全称Web Server Gateway Interface，其实它是一个规范(Specification)，定义了web server和web application之间的通信机制，它是Python特有的，由[PEP 3333][1]完整描述了该Spec。

其实WSGI、CGI、FastCGI都是一样的作用定义了web server和web application如何通信，与之类似的还有Java中的Servlet，也是同样的作用。

### 为什么需要CGI，FastCGI，WSGI？
回归到网站的本质，当用户在浏览器上输入网址后，一个请求就发到web server（比如apache或nginx），server会去找到文件（比如html，css，js），然后发送给浏览器。如果只是静态文件的网站，真的只需要有个web server就完全搞定了。

但现实中大部分网站并非如此，网站内容是动态生成的，并不是文件系统中的某个文件，比如论坛的帖子，电子邮件，最新的新闻或者只是当前的时间，这些都是动态生成出来，然后再发送给浏览器的。具体去生成这些内容的程序区别于web server，我们可以称之为web application。这些程序可以是任意的编程语言实现的，可以是php，python，ruby，Java等等。

通常情况下web server或者说http server处理http协议的解析部分，实现了完整的http协议，大多数的web server都是C或者C++实现的，比如apache, nginx, lighttpd。它们并不能直接执行php,python的代码，又或者说把这些代码嵌(embed)在web server中效率很差，所以它们之间需要一个桥梁或者说接口(interfaces)。这些接口定义了它们之间通信的机制。实际上在web出现的这些年来，已经有非常多的尝试去定义这样一个好用的interface，但值得提起却只有几个。

大部分的web server默认只支持一些很老的interface（比如CGI），但他们都提供了扩展的方式，可以通过第三方的module来支持新的interfaces。

Python官方有一篇[很好的文章][4]描述了这段历史。

### WSGI是如何工作的？
这里有一篇[Tutor][8]用例子简单介绍WSGI的工作机制。详细的细节请看[PEP 3333][1]。

### Django中的WSGI
正式由于WSGI规范的产生，基于Python的web framework，只需要了按照WSGI的规范来实现就能够在所有支持WSGi的web server上部署了。

Django的主要部署方式也是WSGI，详细的部署可以看[Django的官方文档][10]。

Django自带的server，也就是`runserver`命令，本质上是继承自Python库中的`WSGIServer`的服务端，同时把Django中的WSGI application作为参数传递进去。区别于通过nginx+uwsgi的部署，最终工作的都是WSGI application。


[1]: https://www.python.org/dev/peps/pep-3333/
[2]: http://stackoverflow.com/questions/219110/how-python-web-frameworks-wsgi-and-cgi-fit-together
[3]: http://stackoverflow.com/questions/2089271/what-is-common-gateway-interface-cgi?rq=1
[4]: https://docs.python.org/3/howto/webservers.html
[5]: http://stackoverflow.com/questions/12091067/handling-http-chunked-encoding-with-django
[6]: https://github.com/pallets/flask/issues/367
[7]: https://www.reddit.com/r/django/comments/4j6sx5/transferencoding_chunked/
[8]: http://wsgi.tutorial.codepoint.net/
[9]: http://www.wsgi.org/
[10]: https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
