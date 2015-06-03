---
Title: python long line wrap
Date: 2013-12-12 16:12
Category: python
---

## Long line with chained methods

Use additional __parenthesis__.

``` python
subkeyword = (
        Session.query(Subkeyword.subkeyword_id, Subkeyword.subkeyword_word)
        .filter_by(subkeyword_company_id=self.e_company_id)
        .filter_by(subkeyword_word=subkeyword_word)
        .filter_by(subkeyword_active=True)
        .one()
    )
```

## Long string

Python concatenates string literals which appear adjacent to each other.

``` python
def fun():
    print '{0} Here is a really long ' \
          'sentence with {1}'.format(3, 5)
```

