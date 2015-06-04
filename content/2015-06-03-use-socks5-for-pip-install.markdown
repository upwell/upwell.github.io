Title: Use socks5 proxy for pip install
Date: 2015-06-03 17:35
Tags: pip
Category: tech

### Issue
`pip install` doesn't provide the native socks5 proxy support.


### Solution
Use a tool named `proxychains` which chains the connection through proxy.

On Fedora, install via `sudo dnf install proxychains`.

To change the default socks5 proxy, modify `/etc/proxychains.conf`, under `[ProxyList]` add one line:
```
socks5 127.0.0.1 1080
```

How to use:
```
proxychains pip install requests
```

Done! Happy pip with socks5 proxy.
