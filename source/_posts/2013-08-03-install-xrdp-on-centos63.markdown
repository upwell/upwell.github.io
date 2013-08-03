## Install xrdp on CentOS 6.3

### Install packages

CentOS 6.3 does not have xrdp package in the official repo.

- Install xrdp

> wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm  
> wget http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6  
> rpm --import RPM-GPG-KEY-EPEL-6  
> rpm --ivh epel*.rpm  
> yum install xrdp  

### Start service

> /etc/init.d/xrdp start  
> chkconfig xrdp on

### Issues

- problem connecting 5910

> try start vncserver  
> /etc/init.d/vncserver start

- vnc no display configured

> edit /etc/sysconfig/vncservers

    VNCSERVERS="2:root"
    VNCSERVERARGS[2]="-geometry 1280x1024 -localhost"

- vnc password for user root is not configured

> login as root  
> vncpasswd

- vnc undefined symbol: pixman_composite_trapezoids

> yum update pixman pixman-devel

- vnc could not open default font 'fixed'

> yum install libXfont



