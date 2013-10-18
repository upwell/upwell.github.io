---
layout: post
title: "C++头文件include的顺序问题"
date: 2013-10-16 16:48
comments: true
categories: 
---

问题
----
遇到一个很奇怪的问题，在工程中使用 stlport 的时候各种编译不过，即使仅仅是声明一个对象都会编译不过。
```
std::sstream mystream;
```
报的错误也很奇怪，是 stlport 内部的文件语法错误。

分析过程
----
1. 在工程外部，编写小程序，使用工程中的 stlport 来编译，正常编译通过，运行正常；
2. 怀疑工程中的 Makefile 对 stlport 编译时使用了特殊的选项，检查发现没有特殊的选项；
3. 怀疑工程中使用的 stlport 有问题，重新编译了一份 stlport 还是不行；
4. 检查stlport的源代码，出错的地方对 `#define XXX` 有依赖，同时检查了工程中的代码，发现 `include` std 头文件在所有 `include` 的最后面。
```
    #include "a.h"
    #include "b.h"
    #include <sstream>
```

5. 猜测可能前面的头文件中的 `#define` 影响了 sstream 中的设置，将 `#include <sstream>` 放到文件的最前面，问题解决；

```
    #include "a.h"
    #include "b.h"
    #include <sstream>
```

