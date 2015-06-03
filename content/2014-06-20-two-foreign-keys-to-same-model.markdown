---
Title: two foreign keys to same model
Date: 2014-06-20 14:35
Tags: django, python
Category: tech
---

#### Use `related_name`:

``` python
class Test(models.Model):
    example1 = models.ForeignKey(Example, related_name='test1')
    example2 = models.ForeignKey(Example, related_name='test2')
```

See [stackoverflow question][1] and [django doc][2]

#### Why `related_name`:

The `related_name` attributes specifies the name of reverse relation from `Example` model  
to your model.

If no `related_name` is specified, Django creates one using the name of your model with suffix `_set`,
for instance `example.test_set.all()`

In this case, as there are two foreign keys to `Example`, if `related_name` is not specified, Django
doesn't know how to build up the reverse relation.

See [django doc][3]


[1]: http://stackoverflow.com/questions/543377/how-can-i-have-two-foreign-keys-to-the-same-model-in-django
[2]: http://docs.djangoproject.com/en/dev/ref/models/fields/#foreignkey
[3]: http://docs.djangoproject.com/en/dev/topics/db/queries/#backwards-related-objects
