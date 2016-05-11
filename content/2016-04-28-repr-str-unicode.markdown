Title: repr vs. str vs. unicode
Date: 2016-04-28 13:36
Tags: python
Category: tech

### `__repr__`和`__str__`
两者都是把对象转化成字符串：

- `__repr__`主要是要 ___明确___ 表示对象
- `__str__`主要是要为了 ___可读___

下面的示例：
```
In [42]: d = Decimal('100.00')
In [43]: str(d)
Out[43]: '100.00'
In [44]: repr(d)
Out[44]: "Decimal('100.00')"
```
可以看到`repr`的输出更明确，而`str`的输出更明确。

这里有一点要注意的：
> 如果`__str__`没有定义，而`__repr__`定义了，调用对象的`__str__`实际上就是使用`__repr__`。

那么，使用`print`打印一个对象时候到底使用的哪个函数呢？

- print一个对象时，调用的是__str__;
- print list时，调用的是list的__str__，但list的__str__调用的是每个项的__repr__;

### `__str__`和`__unicode__`
#### python2
`str`实际上是字节码，一个一个byte，而`unicode`是一个个字符，

```
In [49]: s = u'汉字'
In [50]: s
Out[50]: u'\u6c49\u5b57'
In [51]: s.encode('utf-8')
Out[51]: '\xe6\xb1\x89\xe5\xad\x97'
In [52]: type(s)
Out[52]: unicode
```

#### python3
所有的字符都是unicode字符格式的，没有`unicode`这个函数只有`str`，python3中的`str`实际上跟python2中的`unicode`是一样的。python3中如果要获得byte格式的话，可以用`bytes`函数。

```
>>> s = '汉字'
>>> s
'汉字'
>>> str(s)
'汉字'
>>> s.encode('utf-8')
b'\xe6\xb1\x89\xe5\xad\x97'
```

<http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python>
