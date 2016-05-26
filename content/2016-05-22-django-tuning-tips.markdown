Title: django tuning tips
Date: 2016-05-23 13:58
Tags: django
Category: tech

# 数据库查询优化

使用`select_related`和`prefetch_related`来减少查询次数，详见 [django 文档][1]。

# 对象处理优化

## 避免过多的`model`对象实例化
数据从数据库取出后，对象实例化的开销也很大，不仅仅是每个对象的初始化，还有各个`field`的初始化，下面是一个实际的例子：
```
6069    0.155   0.000   0.220   0.000   site-packages/django/db/models/base.py:388(__init__)
22      0.036   0.002   0.036   0.002   {method 'query' of      '_mysql.connection'     objects}
61251   0.036   0.000   0.036   0.000   {hasattr}
6069    0.030   0.000   0.250   0.000   site-packages/django/db/models/base.py:484(from_db)
107794  0.030   0.000   0.043   0.000   {isinstance}
```
可以看到`__init__`的次数非常多，耗时也比较长。

需要注意：
> 对于不希望实例化的`ForeignKey`或者`ManyToManyField`，不要使用`select_related`或`prefetch_related`，
> 不然会被自动实例化。

## 使用`values`来获取需要的数据



[1]: https://docs.djangoproject.com/en/dev/topics/db/optimization/
