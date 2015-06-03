---
Title: django - use silk for profiling
Date: 2014-08-13 17:41
Tags: django, python
Category: tech
---
[django-debug-toolbar][1] does not work for ajax requests. Here comes [silk][2] which works perfect for the ajax condition.

### Installation
Following the [instructions][2] to install and configure for your own projects.

### Tips

#### Middleware Settings
Pay attention to the __middleware__ setting, you should not just append the line at the end of existed middle settings.  

This would give you lots of error messages:  

> AttributeError: 'thread._local' object has no attribute 'temp_identifier'

The solutions is, put it before the csrf middleware, like
```
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'silk.middleware.SilkyMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)
```

#### Server Error
The server side may generate error message like:

> pipe error  
> MySQL server has gone away

Add `SILKY_MAX_RESPONSE_BODY_SIZE = 1024` in `settings.py`.

#### Static file handling
If you don't want to run django in debug mode and also haven't setup the external server (nginx, uwsgi, etc.) for static file serving.

To make `silk` display as expected, you need to do the following changes:
```
# python manage.py collectstatic
```
This would collect static files to `settings.STATIC_ROOT` folder.

After that, add a url pattern in `urls.py`.
```
url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}),
```


[1]: https://github.com/django-debug-toolbar/django-debug-toolbar
[2]: https://github.com/mtford90/silk
