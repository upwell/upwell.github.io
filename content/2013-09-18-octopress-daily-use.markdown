---
Title: octopress daily use
Date: 2013-09-18 17:00
Tags: octopress
Category: tech
---

### Check ruby version

``` bash
    ruby -v
```

If the version is not 1.9.3, use the following commmand to switch to 1.9.3:

``` bash
    rvm use 1.9.3
```

### Create a new post

``` bash
    rake new_post['octopress daily use']
```

This would create a new markdown file under `source/_posts/` folder. Edit the file  
to compose the new post.

### Preview and generate

``` bash
    rake generate
    rake preview
```

Visit `http://localhost:4000` to preview the site.

### Deploy to github page

``` bash
    rake generate
    rake deploy
```

This would deploy the generate file on to github page for display.

### Submit source to github repo

``` bash
    git add .
    git commit -m 'new post'
    git push origin source
```

### Use octopress in two machines

Before update / add a new post, remember:
``` bash
    cd source
    git pull origin source
    cd ../_deploy
    git pull origin master
```

After the update, remember to submit to source and deploy to github

