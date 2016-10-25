Title: http post form 还是 json
Date: 2016-10-14 11:17
Tags: api
Category: tech

# 问题
我们在前后端交互的时候经常遇到往服务器发送数据时使用**什么格式**的问题，对于`POST`请求，最常见的两种格式是`form`和`json`。

以最常见的登录接口为例，`form`格式是浏览器默认的提交格式：
```
username=test&password=666666
```
`json`格式的数据是：
```
{"username": "test", "password": "666666"}
```

也并不存在大家有的误区，比如`ajax`就应该传`json`格式的数据。其实两种格式都可以，到底应该用哪种呢？


# 分析
来看看两种格式的优缺点：

### 优点
- `form`是默认的提交方式(更常见)，所有的浏览器和服务器都原生支持，不需要额外的`scripts`
- `json`支持结构化的数据，比如数组，多层级数据

### 缺点
- `form`结构化支持不好，遇到复杂的数据结构时，处理困难
- `json`构造数据需要额外的`scripts`，一些特殊场景（上传文件）处理困难

# 结论
其实抛开具体的场景，很难比较说哪种方式更好更适用，里面会涉及项目使用的前端技术、后端服务器、应用场景。

这里通过几个因素来判断：

### 前端使用的框架
- django form 默认提交的是 form 格式的数据，但也可以使用 jquery 转成 json 格式再提交
- jquery 默认发送 form 格式
- 目前流行的前端框架而言，`angular`、`vuejs`、`reactjs`，还有一些android和ios的库比如`okhttp`，默认发送的都是json格式

### 后端使用的框架
目前我最常用的 django，自带的 Form 都是使用 form 格式提交的，但在实际的使用中，我们的接口大部分都是自己写的，并没有使用 `Form`，对于客户端发过来的数据是 json 和 form 格式的并不敏感，都能容易的支持。

### 一致性
数据接口的一致性，在同一个的项目中尽量使用同一种数据格式

# 建议
- 接口是前后端约定的，尽量保证两边默认就有很好的支持
- 就目前流行的前端框架而言，使用`json`格式的数据更好
- 对于上传文件的场景，使用`form`格式
- 同一个的项目中尽量使用同一种数据格式

# 参考
<http://stackoverflow.com/questions/12042476/normal-form-submission-vs-json>
<http://stackoverflow.com/questions/13541542/posting-json-vs-traditional-form-encoded-data-as-the-data-format-for-submitting>
<http://john-sheehan.com/blog/dont-build-the-best-rest-api-build-the-best-http-api>
<http://homakov.blogspot.kr/2012/06/x-www-form-urlencoded-vs-json-pros-and.html>
