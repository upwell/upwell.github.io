---
Title: python small tips
Date: 2015-02-28 10:09
Tags: python
Category: tech
---

### Join two lists
```python
a = [1, 2, 3]
b = [3, 4, 5]
c = a + b
[1, 2, 3, 3, 4, 5]
```

### Extend a list
```python
a = [1, 2, 3]
b = [3, 4, 5]
a.extend(b)
[1, 2, 3, 3, 4, 5]
```

### Join two dicts
```python
d1 = {1: 'a', 2: 'b'}
d2 = {3: 'c', 4: 'd'}
d1.update(d2)
# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
```

### Check if a list/dictionary/tuple is empty
```python
l = []      # same for {} and ()
if l:
    print 'list is not empty'
else:
    print 'list is empty'
```

### Iterate over dictionary
```python
d = {'a': 1, 'b': 2}
for key in d:
    print key, d[key]
```

```python
d = {'a': 1, 'b': 2}
for key, value in d.iteritems():
    print key, value
```

### Access the index while looping a list
```python
l = ['a', 'b', 'c', 'd']
for idx, value in enumerate(l):
    print idx, value
```

### Reverse range
```
>>> reversed(range(3))
[2, 1, 0]
```

### Select items from a list randomly

```python
import random

l = [1, 2, 3, 4, 6, 7]
print random.choice(l)         # select single item
print random.sample(l, 3)      # select 3 random items
```

### Intersection of sets
```python
set1 = set(1, 2, 3)
set2 = set(1, 3)
set3 = set(3, 4, 5)

set4 = set1.intersection(set2, set3)
```

### Split and convert to int

```python
c = '1,2,3,4'
c.split(',')				# ['1','2','3','4']
map(int, c.split(','))      # [1,2,3,4]
```

### Create a dict with default value for non-exist keys
```python
from collections import defaultdict
d = defaultdict(lambda: [], {})
d['a']  # => []
```

### Mutable and immutable
__Immutable__:

- integers and other numerical types
- string types like str and unicode
- tuples

__Mutable__: everything else, like,

- lists
- dicts
- class
- class instance
- etc.


### Double quote VS. single quote
- use double quotes around strings that are used for interpolation or that are natural language messages
- single quotes for small symbol-like strings
- use triple double quotes for docstrings and raw string literals
```
LIGHT_MESSAGES = {
    'English': "There are %(number_of_lights)s lights.",
    'Pirate':  "Arr! Thar be %(number_of_lights)s lights."
}

def lights_message(language, number_of_lights):
    """Return a language-appropriate string reporting the light count."""
    return LIGHT_MESSAGES[language] % locals()

def is_pirate(message):
    """Return True if the given message sounds piratical."""
    return re.search(r"(?i)(arr|avast|yohoho)!", message) is not None
```
