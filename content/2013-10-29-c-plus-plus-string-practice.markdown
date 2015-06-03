---
Title: c++ string / file practice
Date: 2013-10-29 15:10
Tags: c++
Category: tech
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

Concatenate two vectors
-----

``` c++
std::copy(source.begin(), source.end(), std::back_inserter(destination));
```

Merge two vectors
-----

`std::merge` conbines the elements in sorted range [first1, last1], [first2, last2], into a new  
range beginning at _result_ with all its elements sorted.

``` c++
std::vector<std::string> v1, v2, tmp;
tmp.reserve(v1.size() + v2.size());

std::sort(v1.begin(), v1.end());
std::sort(v2.begin(), v2.end());

std::merge(v1.begin(), v1.end(),
        v2.begin(), v2.end(),
        std::back_inserter(tmp));
```

Concatenate two vectors, and remove duplicate elements
-----

``` c++
std::vector<std::string> v1, v2, tmp;

tmp.reserve(v1.size() + v2.size());
std::sort(v1.begin(), v1.end());
std::sort(v2.begin(), v2.end());

std::set_union(v1.begin(), v1.end(),
            v2.begin(), v2.end(),
            std::back_inserter(tmp));
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

