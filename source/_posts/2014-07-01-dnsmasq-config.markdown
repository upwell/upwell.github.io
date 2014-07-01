---
layout: post
title: "dnsmasq config"
date: 2014-07-01 19:07
comments: true
categories: system
---

### Set dns server for dnsmasq
Use a separate conf file, the format is the same as resolv.conf.
```
resolv-file=/etc/resolv.masq.conf
```
Then after dnsmasq is started, set `127.0.0.1` in `/etc/resolv.conf`.

### listening address with localhost
```
listen-address=127.0.0.1
```

### Use separate DNS for certain domains
```
server=/www.google.com/8.8.8.8
```

### Use regular expression for server
```
server=/:.*google.*/8.8.8.8
```
