Title: gitlab docker 部署问题
Date: 2016-07-28 17:10
Tags: gitlab,docker
Category: tech

# 部署步骤

参考 [docker 文档][1]。

注意，先要`pull image`
```
docker pull gitlab/gitlab-ce:latest
```

# 问题
## docker pull 使用代理服务器
直接export http_proxy https_proxy不生效，按照 [docker文档][2] 配置。

## docker run 的配置
```
sudo docker run --detach \
    --hostname gitlab.example.com \
    --publish 443:443 --publish 80:80 --publish 22:22 \
    --name gitlab \
    --restart always \
    --volume /srv/gitlab/config:/etc/gitlab \
    --volume /srv/gitlab/logs:/var/log/gitlab \
    --volume /srv/gitlab/data:/var/opt/gitlab \
    gitlab/gitlab-ce:latest
```

- `hostname`需要设置成实际的地址，比如：192.168.1.100
- 对外的端口 22 会与 主机 sshd 的端口冲突，可以把主机 sshd 的端口改成非22，比如2222

docker run 之后，同名的不能再运行，如果没有配置，可以先删除了，再重新run。
```
docker stop gitlab
docker rm gitlab
docker run ....
```

## 配置防火墙
```
firewall-cmd --permanent --add-port=2222/tcp
firewall-cmd --reload
```

## 连接到container
```
docker exec -it gitlab /bin/bash
```

## 改变绑定的端口
对于已经`run`过的container，没办法直接修改，两种方式：
- 通过 iptables 再做端口转发
- 重新创建 container，步骤见 [stackoverflow的问题][3]

## 配置 smtp
连到到container里面，修改`/etc/gitlab/gitlab.rb`，添加下面的列：

```
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = "smtp.exmail.qq.com"
gitlab_rails['smtp_port'] = 465
gitlab_rails['smtp_user_name'] = "gitlab@yourdomain.com"
gitlab_rails['smtp_password'] = "yourpassword"
gitlab_rails['smtp_domain'] = "smtp.qq.com"
gitlab_rails['smtp_authentication'] = "login"
gitlab_rails['smtp_enable_starttls_auto'] = true
gitlab_rails['smtp_tls'] = true
gitlab_rails['gitlab_email_from'] = "gitlab@yourdomain.com"
```

重新配置：
```
gitlab-ctl reconfigure
```

[1]: http://docs.gitlab.com/omnibus/docker/
[2]: https://docs.docker.com/engine/admin/systemd/#http-proxy
[3]: http://stackoverflow.com/questions/19335444/how-to-assign-a-port-mapping-to-an-existing-docker-container
