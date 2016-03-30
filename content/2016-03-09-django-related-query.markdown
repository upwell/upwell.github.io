Title: django query 使用的 manager
Date: 2016-03-09 18:03
Tags: django, python
Category: tech


## default manager

如果 model 中定义了多个 manager 时，Django 会选取第一个（排在最前面的）作为 default manager，Django 中会选用 default manager 去执行一些操作 (dumpdata)，因此在 override `get_queryset` 的时候要小心，有可能会导致 **获取对象的时候取不到值** 的情况。

## 访问 related object 时使用的 manager

**默认** Django 会选用 "plain" manager (`models.Manager`) 实例作为访问 related object 时的 manager，这样访问 model 中的 Foreign Key 时，使用 "plain" manager 能够保证总是能取到值。

也可以通过在 `default manager` 中加入设置 `use_for_related_fields = True` 来让访问 related object 时使用该 manager，而不是 "plain" manager。详细解释见下一条说明。

## use_for_related_fields 的更多场景 automatic manager

Django 在有些场景下需要创建临时的 `automatic manager` 来执行一些操作，比如：  
- 为没有定义 manager 的 model 生成 `default manager`
- 访问 related object 时的临时 manager

通常情况下，Django 使用 `models.Manager` 来生成 manager 实例。

Django 提供了一个机制来使用自定义的 manager，而不是 `models.Manager` 来生成 `automatic manager` 的实例：  
- 该自定义的 manager 必须是 **default manager**
- 在 **default manager** 中加入 `use_for_related_fields=True`

## reverse query 时使用的 manager
```python
from django.db import models

class Entry(models.Model):
    #...
    objects = models.Manager()  # Default Manager
    entries = EntryManager()    # Custom Manager

b = Blog.objects.get(id=1)
b.entry_set(manager='entries').all()
```
默认情况下，`RelatedManager` 会使用对应 model 的 **default manager** 的子类作为查询时的 manager，你也可以通过传入 `manager` 参数来使用指定的 manager。


## References
[django automatic manager ](https://docs.djangoproject.com/en/1.9/topics/db/managers/#controlling-automatic-manager-types)

[using a custom reverse manager](https://docs.djangoproject.com/en/1.9/topics/db/queries/#using-a-custom-reverse-manager)
