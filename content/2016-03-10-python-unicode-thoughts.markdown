Title: python unicode 编码整理
Date: 2016-03-10 13:36
Tags: python， unicode
Category: tech

## unicode 与 utf-8 的关系
### unicode 是 character set

- character set 是把每个字符**对应**成数字的集合，比如unicode中 A对应0041，  
汉字『我』对应 '6211'
- unicode 是个很大的集合，几乎覆盖世界上所有的字符，现在的规模已经可以容纳  
100万个字符。

### utf-8 是对 unicode 存储的实现方式

unicode 只定义字符对应的数字，但没有规定这些数字如何存储起来，比如像中文的『我』字存储时  
需要两个字节来表示，而英文字母A却只需要一个字节，有些其他的字符可能需要3-4个字节。

- 如果统一规定每个字符用3个或者4个字节来存储，那么每个英文字符都必然需要额外2到3个0，  
这对存储是很大的浪费。
- 如果每个字符按照实际需要的字节数来存储，计算机就分不清三个字节是表示三个字符还是一个字符。

***utf-8 是对 unicode 编码存储的一种实现方式，同样的还有 utf-16, utf-32。***

utf-8 是使用最广泛的编码方式，采用变长的编码方式，可以使用1-4个字节来表示一个字  
符； utf-16 用2个或4个字节，utf-32 用4个字节表示。编码规则如下：

1. 对于单字节的符号，字节的第一位设为0，后面7位为这个符号的unicode码。因此  
对于英语字母， UTF-8编码和ASCII码是相同的。
2. 对于n字节的符号（n>1），第一个字节的前n位都设为1，第n+1位设为0，后面字节  
的前两位一律设为10。剩下的没有提及的二进制位，全部为这个符号的unicode码。

## python2 中的 str 和 unicode
python2 中有字符串类型有两种：`byte string (str)`和 `unicode string (unicode)`。
```python
>>> s = '美的'
>>> s
'\xe7\xbe\x8e\xe7\x9a\x84'
>>> s = u'美的'
>>> s
u'\u7f8e\u7684'
>>> s = '美的'
>>> s.decode('utf-8')
u'\u7f8e\u7684'
```
上面的输出中，第一个s的类型是str，打印出来的内容是 utf-8 编码过的内容。第二个s的类型是  
unicode，打印出来的两个双字节的数字分别表示了两个汉字『美的』。

> `encode`和`decode`提供 str 和 unicode 这两种的类型的互相转化。

- encode 把 str(byte string) 转化成 unicode
- decode 把 unicode 转化成 str(byte string)

本质上，str是存放的字节序，有可能是ascii, gbk, utf-8等等中的任意一种，通过调用  
decode可以把他们转化成unicode，默认的decode编码是ascii。str中到底是用的哪一种  
编码，取决于它所在的场景，跟locale，文件编码等等都有关系。

### 文本文件、编辑器的处理
```python
#!/usr/bin/env python
# -*- coding: GBK -*-

s = u'中文'
print repr(s)
print repr(s.encode('GBK'))
```

比如上面的文件`enc.py`，保存的时候选择`文件编码`是GBK，程序文件本质上也是文件，当我们使用  
某个外部的应用  打开它时（编辑器或者python解释器等），外部应用是不知道该文件的编码格式的，  
这个时候有三种情况：

- 应用使用其默认的编码方式去解析，比如UTF-8或者ASCII；python解释器默认是ASCII，编辑器  
可以自己设置；
- 应用根据文件中的字节内容，自动检测编码方式；
- 文本文件告诉应用使用什么编码方式去解码；比如`# -*- coding: GBK -*-`告知解释器使用GBK  
来解码；

试验一下，把`# -*- coding: GBK -*-`删除后，执行`python enc.py`，输出：  
```
   File "enc.py", line 4
 SyntaxError: Non-ASCII character '\xd6' in file enc.py on line 4, but no encoding declared;
```

试着用vim打开该文件时，『中文』两个字就会显示成乱码，应为vim默认的文件编码方式被设置成UTF-8了。

```python
#!/usr/bin/env python
# -*- coding: GBK -*-

s1 = u'中文'

print repr(s1)
print repr(s1.encode('GBK'))

s2 = '中文'

print repr(s2)
print repr(s2.decode('GBK'))
```
输出结果：
```
u'\u4e2d\u6587'
'\xd6\xd0\xce\xc4'
'\xd6\xd0\xce\xc4'
u'\u4e2d\u6587'
```
从这里可以看出来， s2中存放的是byte格式的从文件中读到的GBK编码的内容。

再看下面的这段代码，程序文件`utf8_enc.py`，保存成UTF-8编码的。
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

s1 = u'中文'

print repr(s1)
print repr(s1.encode('GBK'))

s2 = '中文'

print repr(s2)
print repr(s2.decode('GBK'))
```
输出：
```
u'\u4e2d\u6587'
'\xd6\xd0\xce\xc4'
'\xe4\xb8\xad\xe6\x96\x87'
Traceback (most recent call last):
  File "unicode_enc.py", line 12, in <module>
    print repr(s2.decode('GBK'))
UnicodeDecodeError: 'gbk' codec can't decode bytes in position 2-3: illegal multibyte sequence
```
这里同样可以知道，s2中存放的是文件保存的编码UTF-8的byte码。

## References

http://www.rrn.dk/the-difference-between-utf-8-and-unicode/
http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html
https://docs.python.org/2/howto/unicode.html
http://yergler.net/2012/bytes-chars/
