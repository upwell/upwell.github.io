---
layout: post
title: "c++ string / file practice"
date: 2013-10-29 15:10
comments: true
categories: 
---

Read one line from file each time
-----

``` c++
ifstream in("a.txt");
std::string line;
std::getline(in, line);
```

Trim space from string
-----

[original source][1]

``` c++
#include <algorithm>
#include <functional>
#include <cctype>
#include <locale>

static inline std::string &ltrim(std::string &s) {
        s.erase(s.begin(),
                std::find_if(s.begin(), s.end(),
                    std::not1(std::ptr_fun<int, int>(std::isspace))));
        return s;
}

static inline std::string &rtrim(std::string &s) {
        s.erase(std::find_if(s.rbegin(), s.rend(),
                    std::not1(std::ptr_fun<int, int>(std::isspace))).base(), s.end());
        return s;
}

static inline std::string &trim(std::string &s) {
        return ltrim(rtrim(s));
}

```

Merge two vectors
-----

Merge operation will remove duplicated elements.

``` c++
std::vector<std::string> tmp_urls;
tmp_urls.reserve(urls.size() + old_urls.size());
std::merge(old_urls.begin(), old_urls.end(),
        urls.begin(), urls.end(),
        std::back_inserter(tmp_urls));
```

Append with operations on each element
-----

``` c++
std::string append_arrow(std::string &str)
{
    return str + "->";
}

std::vector<std::string> tmp_urls;
std::vector<std::string> content;

std::transform(tmp_urls.begin(), tmp_urls.end(),
        std::back_inserter(content),
        append_arrow);
```

Write vector to file
-----

``` c++
ofstream out("a.txt");
std::vector<std::string> content;

std::ostream_iterator<std::string> output_iter(out, "\n");
std::copy(content.begin(), content.end(), output_iter);
```


[1]: http://stackoverflow.com/questions/216823/whats-the-best-way-to-trim-stdstring

