---
layout: post
title: "Object - javascript: the good part"
date: 2013-11-10 10:42
comments: true
categories: 
---

### Object Literals


``` js
var empty_object = {};

var stooge = {
    "first-name": "Jerome",
    "last-name": "Howard"
};

```

#### Property Name

- could be __any__ string including empty string;
- __the quote around the name is optional__, if the name is a legal Javascript  
  name (not a reserved word);

``` js
var flight = {
    airline: "Ocreanic",
    number: 815,
    departure: {
        IATA: "SYD",
        time: "2012-10-12 12:11",
        city: "Sydney"
    },
    arrival: {
        IATA: "LAX",
        time: "2012-10-13 12:10",
        city: "Los Angeles"
    }
};
```

### Retrieval

- Wrapping a string expression in a [] suffix;
- If the name is a legal Javascript name and not a reserved word,  then the `.`  
  notation can be used instead;
- The `.` notation is preferred beacuase it's more compact and it reads better;
- The `undefined` value is produced if an attempt is made to retrieve a nonexistent  
  member:
- Attempting to retrieve values from undefined will throw a TypeError exception;

``` js
stoog["first-name"]         // "Jerome"
flight.departure.city       // "Sydney"

flight.status               // undefined

flight.equipment.model      // throw "TypeError"
flight.equipment && flight.equipment.model // undefined
```

### Update

``` js
stoog["first-name"] = "Jack";// if the property name already exist, update the value;

stoog.sex = "Male";          // if the property name not exist, the object is augmented;
```

### Reference

Object is passed __BY REFERENCE__, never by copied.

``` js
var a = {}, b = {}, c = {};
    // refer to different empty objects

a = b = c = {};
    // refer to the same empty object
```

### Prototype

Every object is linked to a __prototype object__. All objects created from object literal `{}`  
are linked to `Object.prototype`.

The prototype link has no effect on updating. When we make changes to an object, the object's  
prototype is not touched.

The prototype relationship is a dynamic relationship. If we add a new property to a prototype,  
that property will immediately be visible in all the objects that are based on that prototype.

``` js
stooge.profession = 'actor';
another_stooge.profession // 'actor'
```

### Reflection

Check if the object has a property:

Use `typeof` operator.

``` js
typeof flight.number        // 'number'
typeof flight.status        // 'string'
typeof flight.manifest      // 'undefined'
```

Any property on the prototype chain can produce a value:

``` js
typeof flight.toString      // 'function'
```

Use `hasOwnProperty` method. This method does __NOT__ check the prototype chain.

``` js
flight.hasOwnProperty('number')     // true
flight.hasOwnProperty('toString')   // false
```

### Enumeration

Loop over all the property names in an object.

`for in` statement. The enumeration will include all of the properties (functions and  
properties in the prototype chain.)

``` js
var name;
for(name in another_stooge) {
    if(typeof another_stooge[name] !== 'function) {
        document.writeln(name + ': ' + another_stooge[name]);
    }
}
```

But there is __NO__ gurantee on the order of the names.

The better way is to created a property array and loop the array with the right order.

``` js
var i;
var properties = [
    'first-name',
    'last-name',
    'profession'
];

for(i = 0; i < properties.length; i += 1) {
    document.writeln(properties[i] + ': ' +
        another_stooge[properties[i]);
}
```

### Delete

The `delete` operator can be used to remove a property from a object. It does __NOT__ touch  
any object in the prototype linkage.

