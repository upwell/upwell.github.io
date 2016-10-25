Title: mongodb 初识
Date: 2016-10-21 11:15
Tags: mongodb
Category: tech


# mongodb 基本概念

## document
关系数据库表的单条记录(`record`)对应到`mongodb`就是单个`document`。

`document`的结构类似`JSON`的对象，里面是一个个`KEY/VALUE`対。`Value`可以是的`document, array, arrays of documents`。

```
{
   "_id" : ObjectId("54c955492b7c8eb21818bd09"),
   "address" : {
      "street" : "2 Avenue",
      "zipcode" : "10075",
      "building" : "1480",
      "coord" : [ -73.9557413, 40.7720266 ]
   }
}
```

## collection
关系数据库表的表(`table`)对应到`mongodb`就是`collection`。区别在于`collection`不要求里面的`documents`有相同的`schema`。

存储在`collection`中的`documents`必须要有一个唯一的`_id`作为主键(`primary key`)。
