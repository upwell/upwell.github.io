Title: osx 上使用 docker
Date: 2016-03-10 13:36
Tags: docker, osx
Category: tips

## 安装
根据[官方文档][1]的步骤进行安装，由于 mac 原生没有 container 的机制，需要在 mac 上安装一个 linux 的虚拟机，然后再在虚拟机上跑 docker engine，安装好之后点击运行 `Docker Quickstart Terminal`。

> 注意: 这里如果选择使用 iTerm 打开的话会有问题，建议使用 Terminal 打开。

## 运行

启动 `Docker Quickstart Terminal` 后，默认会创建好一台 linux 虚拟机，可以通过下面的命令查看：

```bash
➜  ~ docker-machine ls
NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
default   *        virtualbox   Running   tcp://192.168.99.100:2376           v1.10.3  
```

这里可以看到已经通过 virtualbox 创建好了一台 linux 虚拟机，基于 docker 的操作都在该台虚拟机中完成。同时在 mac 中打开 VirtualBox 应用，也能打开相应的虚拟机在运行中。

执行`docker run hello-world`可以验证 docker 是否安装好了，由于 docker 服务在国外，速度慢，可以配置使用代理服务器来下载，执行下面的命令让`docker run`使用代理服务器。
```
export http_proxy=http://localhost:8118
export https_proxy=http://localhost:8118
export no_proxy="192.168.99.100"
```

注意最后的`export no_proxy`是必须的，否则`docker`在连接虚拟机时也会走代理服务器，连接当然会出错了。

## 使用 docker
使用 docker 部署 [devdocs][2]
```
docker build -t thibaut/devdocs .
```
这个时候，container 中会更新服务，这个时候有两个需要注意的：
> 1. 内部系统更新时，网络会使用 ipv6，但本地网络并不具备 ipv6 的环境，这时需要在`docker-machine`的 linux 虚拟机中禁用 ipv6，禁用后需要重启。
> 2. 内部系统更新时，网络较慢时，需要使用代理，可以在 Dockerfile 中配置 `ENV http(s)_proxy=`。

```
docker run --name devdocs -d -p 9292:9292 thibaut/devdocs
```
> 服务跑起来后，并不是在`localhost:9292`，而是`192.168.99.100:9292`。

[1]: https://docs.docker.com/mac/
[2]: https://github.com/Thibaut/devdocs/
