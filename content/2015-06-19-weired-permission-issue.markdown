Title: Weired directory permission issue
Date: 2015-06-19 17:06
Tags:
Category: tech

### Issue
While I was deploying a php project for apache on my `HOME` directory, although I used `chmod` and `usemod` to grant user `apache`    
the permissions, apache still failed to access the `HOME` directory.

### Solution
After a little dig, occationally I found the `HOME` directory has a special permission symbol.
```
drwxr-xr-x+ 93 han      han      4.0K 6月  23 11:30 han
```
There is a `+` at the end of permission field. What does this means?

[This][1] gives an explanation of this special `+` sign.

The `HOME` directory has extended permissions. The output of `getfacl`:
```
# file: han
# owner: han
# group: han
user::rwx
user:qemu:--x
group::---
mask::r-x
other::r-x
```

The following command grants the group `r+x` permissions.
```
# setfacl -m 'g:han:rx' han
```


[1]: http://serverfault.com/questions/227852/what-does-a-mean-at-the-end-of-the-permissions-from-ls-l

