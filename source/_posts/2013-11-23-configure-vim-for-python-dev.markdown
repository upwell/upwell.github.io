---
layout: post
title: "configure vim for python dev"
date: 2013-11-23 08:42
comments: true
categories: 
---

## Flake8

[flake8][1] :  wrapper for python checkers:

- PyFlakes
- pep8
- Ned Batchelder's McCabe script

### Install

``` bash
# sudo pip install flake8
```

## Vim-flake8

[vim-flake8][2] : vim wrapper for flake8.

### Install

``` bash
# git submodule add https://github.com/nvie/vim-flake8.git bundle/vim-flake8
```

### How to use

1. Open a python file
2. ress `F7` to run `flake8` on it

## Syntastic

[syntastic][3] : syntax checking plugin that runs file through external syntax  
checker and displays any resulting errors to user.

### Install

``` bash
# git submodule add https://github.com/scrooloose/syntastic bundle/syntastic
```

Start vim, then type `:Helptags`.

### How to use

Check

```
:SyntasticCheck
```

See available external checker:

```
:SyntasticInfo
```

[1]: https://pypi.python.org/pypi/flake8/
[2]: https://github.com/nvie/vim-flake8
[3]: https://github.com/scrooloose/syntastic
