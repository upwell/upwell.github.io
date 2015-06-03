---
Title: Install oracle jdk 32bit on 64bit Fedora
Date: 2013-10-18 22:31
Tags: jdk, fedora
Category: tech
---

Issue
----

When execute:

```
# rpm -ivh ~/Downloads/jdk-7u45-linux-i586.rpm
```

There comes error messages:
```
Unpacking JAR files...
    rt.jar...
Error: Could not open input file: /usr/java/jdk1.7.0_45/jre/lib/rt.pack
Error: unpack could not create JAR file:

    /usr/java/jdk1.7.0_45/jre/lib/rt.jar

Please refer to the Troubleshooting section of the Installation Instructions
on the download page.
    jsse.jar...
Error: Could not open input file: /usr/java/jdk1.7.0_45/jre/lib/jsse.pack
Error: unpack could not create JAR file:

    /usr/java/jdk1.7.0_45/jre/lib/jsse.jar
```

Solution
----

Install the 32bit libraries:

```
# rpm -ivh glibc.i686 glibc-devel.i686
```

