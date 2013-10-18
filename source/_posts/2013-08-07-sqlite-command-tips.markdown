---
layout: post
title: "SQLite command tips"
date: 2013-08-07 13:26
comments: true
categories: 
---

### Use a database file

```
    sqlite <database_file>
```

### Get table information

```
    .tables
```

### Get schema information

```
    .schema
    .schema table_name
```

### Get help

```
    .help
```

### Write result to a file

```
    .mode list
    .separator |
    .output result.data
    select * from table_name;
    .exit
```

### Exit

```
    .exit
```

### More

[sqlite official site help](http://www.sqlite.org/sqlite.html)

