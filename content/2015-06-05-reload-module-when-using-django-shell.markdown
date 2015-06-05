Title: Reload module when using Django shell
Date: 2015-06-05 10:57
Tags: django, python
Category: tech

### Issue
The annoying part of using django shell is that:
> Once you changed the source code, you need restart the shell and enter the code again.


### Solution
Use `django-extensions` in the project and with `shell_plus`, there is a better expirence using django shell, although
it's not the best, anyway it's much better.
```
# python manage.py shell_plus --notebook
```

The above command would open a notebook on your browser, write your code in a cell.
When you changed your module, just click `Kernel > Restart`, and rerun the code.

Done! Happy django.
