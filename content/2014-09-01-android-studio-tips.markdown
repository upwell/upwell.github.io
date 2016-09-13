---
Title: android studio tips
Date: 2014-09-01 15:45
Tags: android
Category: tech
---

## Cannot run program aapt -- no such file or directory

Install missing 32bit libraries:

```
yum install libstdc++.i686 zlib.i686
```

## studio running with the openjdk

Although I installed the oracle jdk, and export `STUDIO_JDK` in both zshrc and bashrc, when  
start android studio from desktop application, it still uses the open jdk.

For desktop application defined under `~/.local/share/applications/`, you need to  
setup the environment variables in `~/.profile`.

```
export STUDIO_JDK=/usr/java/jdk1.8.0_20
```

After that, logout and relogin, start android studio again, it works now.

## gradlew behind proxy

```
./gradlew -Dhttp.proxyHost=127.0.0.1 -Dhttp.proxyPort=8118 -Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=8118 --stop
```

## stop running tasks

```
./gradlew --stop
```
