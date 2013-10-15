---
layout: post
title: "Ignore files when building tags"
date: 2013-10-15 17:52
comments: true
categories: 
---

Use the following commands:

    ctags --exclude=*.html --exclude=*.js --exclude=*.sql -R

It's annoying to enter the long parameters every time. You can configure  
it as the default config.

Edit `~/.ctags`. Add the following lines:

    --exclude=*.html
    --exclude=*.js
    --exclude=*.sql

Then you only need to type:

    ctags -R

