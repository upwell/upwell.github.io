---
layout: post
title: "two foreign keys to same model"
date: 2014-06-20 14:35
comments: true
categories: django python
---

Use `related_name`:

``` python
class Test(models.Model):
    example1 = models.ForeignKey(Example, related_name='example1')
    example2 = models.ForeignKey(Example, related_name='example2')
```

Reference:  
[stackoverflow question](http://stackoverflow.com/questions/543377/how-can-i-have-two-foreign-keys-to-the-same-model-in-django)  
[related_name in django docs](http://docs.djangoproject.com/en/dev/ref/models/fields/#foreignkey)
