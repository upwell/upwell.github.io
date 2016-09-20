Title: python eval 的问题
Date: 2016-09-20 11:17
Tags: python
Category: tech

# 场景
最近在代码会看到一些使用 `eval` 的代码场景，比如动态获取变量的值：
```python
NAME_H = 'h'
NAME_X = 'x'

name = eval('NAME_H')
```

# 问题
其实 `eval` 在各种语言中，都是比较特殊的函数，一般的场景下都不应该使用，主要的几个原因是：
- There is almost always a better way to do it
- Very dangerous and insecure compare to most other python functions
- Makes debugging difficult
- Slow

# 结论
`eval` 的使用场景比较特殊，一般的情况下都不应该使用，非得使用它的时候也要谨慎考虑。

> It seems simple to me: eval is a vector for code injection, and is dangerous in a way that most other Python functions are not. That doesn't mean you shouldn't use it at all, but I think you should use it judiciously.


# 参考
[Is using eval in python a bad practice][1]


[1]: http://stackoverflow.com/questions/1832940/is-using-eval-in-python-a-bad-practice
