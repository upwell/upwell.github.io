Title: http api 设计中 GET 还是 POST
Date: 2016-01-26 18:03
Tags: http, api
Category: tech

### GET 用于安全的操作，POST 用于不安全的操作
`GET`有以下特性：
- GET requests can be cached
- GET requests can remain in the browser history
- GET requests can be bookmarked
- GET requests can be distributed & shared
- GET requests can be hacked (CSRF)

如果对于一个删除接口，例如：
```
GET /address/delete/<id>/
```
这样的接口会存在安全隐患，在用户登录状态下，点击链接就会触发接口的调用，容易被用于攻击。

接口设计时应该有这样的设定：

> 凡是对服务端数据进行修改的接口，使用 `POST`，而不是 `GET`。

### 对于参数多导致URL过长的场景应该使用 POST
虽然 RFC 没有 URL 长度的规定，但是老版 IE ，某些代理服务器，对 URL 的长度会有限制的，比如2048。

###  ajax 请求数据时尽量使用 GET
浏览器在处理 `XMLHttpRequest` 的时候，会分两步进行发送，先发头部，再发送数据，使用 `GET` 的话，可以更快的发送请求，获得响应。(待验证)
