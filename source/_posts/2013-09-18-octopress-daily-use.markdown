---
layout: post
title: "octopress daily use"
date: 2013-09-18 17:00
comments: true
categories: 
---
### Check ruby version

    ruby -v

If the version is not 1.9.3, use the following commmand to switch to 1.9.3:

    rvm use 1.9.3

### Create a new post

    rake new_post['octopress daily use']

This would create a new markdown file under `source/_posts/` folder. Edit the file  
to compose the new post.

### Preview and generate

    rake generate
    rake preview

Visit `http://localhost:4000` to preview the site.

### Deploy to github page

    rake generate
    rake deploy

This would deploy the generate file on to github page for display.

### Submit source to github repo

    git add .
    git commit -m 'new post'
    git push origin source

