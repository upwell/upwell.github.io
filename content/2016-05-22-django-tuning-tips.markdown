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
正常我们使用`get`, `filter`获取到结果后，如果遍历或使用时，`django`会帮我们把`model`实例化，而在上面已经提到了，实例化的开销是比较大，尤其在`model`比较复杂的的时候。
这里我们可以使用`values`方法，把需要的字段取出来，然后再自行构造需要的数据，通常是组织成`dict`，供前端或者模板渲染使用。

从这点可以看出，`ORM`虽然很方便，但当数据量很大的时候，效率就会出现问题。处理问题还是要灵活，当然如果`django`能够提供一套机制来组织需要的数据而不用实例化对象就更好了。

# 参考资料
[Django Performance Tuning][2]
[SQL Database Best Practises with Django][3]


[1]: https://docs.djangoproject.com/en/dev/topics/db/optimization/
[2]: http://www.servercobra.com/django-performance-tuning/
[3]: http://scottlobdell.me/2015/01/sql-database-best-practices-django-orm/
