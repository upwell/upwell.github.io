Title: android tips
Date: 2016-05-20 11:16
Tags: android
Category: tech

## Build with command line
```
./gradle assembleDebug
```
这个命令，偶尔会触发下载`gradle.ver.zip`，而下载又很慢，可以把该文件自行下载下来，拷贝到`$HOME/.gradle`底下指定的目录去。

## package binary to apk
可以把`binary`文件放到`assets`目录里面，如果目录不存在，则在`app/src/main`带下创建该目录。

安装后，由于`assets`中的文件是只读的，需要在程序中使用`AssetManage`把`binary`拷贝到用户目录。
