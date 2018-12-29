## Python tricks 101 by Gautham Santhosh [link](https://hackernoon.com/python-tricks-101-2836251922e0)

### Swapping Values
```python
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)
```

### Create a single string from all the elements in list
```python
a = ["Python", "is" "awesome"]
print(" ".join(a))
```

### Find the Most Frequent Value in List.
```python
a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(max(set(a),key = a.count))
""" using Counter from collections """

from collections import Counter
cnt = Counter(a)
print(cnt.most_common(3))
```

### Checking if two words are anagrams
```python
from collections import Counter

Counter(str1) == Counter(str2)
```

### Reverse a String
```python
""" reversing string with special case of slice step param"""
a = 'abcdefilksdflksdlfsdf'
print(a[::-1])

"""iterating over string contents in reverse efficiently."""
for char in reversed(a):
    print(char)
    
"""reversing an integer through type conversion and slicing."""
num = 123456789
print(int(str(num)[::-1]))
```

### Reverse a list
```python
"""reversing list with special case of slice step param"""
a = [5, 4, 3, 2, 1]
print(a[::-1])

"""iterating over list contents in reverse efficiently."""
for ele in reversed(a):
    print(ele)
```    
### Transpose 2d array
```python
"""transpose 2d array [[a,b], [c,d], [e,f]] -> [[a,c,e], [b,d,f]]"""
original = [['a','b'],['c','d'],['e','f']]
transposed = zip(*original)
print(list(transposed))
```

### Chained Comparison
```python
"""chained comparison with all kind of operators"""
b = 6
print(4 < b < 7)
print(1 == b < 20)
```

### Chained function call
```python
"""calling different functions with same arguments based on condition"""
def product(a, b):
    return a * b

def add(a, b):
    return a + b
    
b = True
print((product if b else add)(5,7))
```

### Copying List
```python
"""a fast way to make a shallow copy of a list"""
b = a
b[0] = 10
""" both a and b will be [10, 2, 3, 4, 5] """

b = a[:]
b[0] = 10
""" only b will change to [10, 2, 3, 4, 5] """

"""copy list by typecasting method"""
a = [1,2,3,4,5]
print(list(a))

"""using the list.copy() method (python3 only)"""
a = [1, 2, 3, 4, 5]
print(a.copy())

"""copy nested lists using copy.deepcopy"""

from copy import deepcopy

l = [[1,2], [3,4]]
l2 = deepcopy(l)
print(l2)
```

### Dictionary Get
```python
"""returning None or default value, when key is not in dict"""
d = { 'a': 1, 'b': 2 }
print(d.get('c', 3))
```

### Sort Dictionary by Value
```python
"""Sort a dictionary by its values with the built-in sorted() function and a 'key' argument."""
d = { 'apple': 10, 'orange': 20, 'banana': 5, 'rotten tomato': 1 }
print(sorted(d.items(), key=lambda x: x[1])

"""Sort using operator. itemgetter as the sort key instead of a lambda"""

from operator import itemgetter
print(sorted(d.items(), key=itemgetter(1)))

"""Sort dict keys by value"""
print(sorted(d, key=d.get))

```

### For Else
```python
"""else gets called when for loop does not reach break statement"""
a = [1,2,3,4,5]
for el in a:
    if el == 0:
        break
else:
    print('did not break out of for loop')
```

### Convert list to comma separated
```python
"""converts list to comma separated string"""
items = ['foo', 'bar', 'baz']
print(','.join(items))

"""list of numbers to comma seperated"""
numbers = [2,3,5,10]
print(','.join(map(str, numbers)))

"""list of mix data"""
data = [2, 'hello', 3, 3.4]
print(','.join(map(str, data)))
```

### Merge dict's
```python
"""merge dict's"""
d1 = {'a':1}
d2 = {'b':2}

"""python 3.5"""
print({**d1, **d2})
print(dict(d1.items() | d2.items()))

d1.update(d2)
print(d1)
```

### Min and Max index in List
```python
"""
Find Index of Min/Max Element.
"""

list = [40, 10, 20, 30]

def minIndex(list):
    return min(range(len(list)), key=list.__getitem__)
    
def maxIndex(list):
    return max(range(len(list)), key=list.__getitem__)
    
print(minIndex(list))
print(maxIndex(list))
```

## Remove duplicates from a list
```python
"""remove duplicate items from list. note: does not preserve the original list order"""
items = [2, 2, 3, 3, 1]

newitems = list(set(items))
print(newitems)

"""remove dups and keep order"""
from collections import OrderedDict
items = ["foo", "bar", "bar", "foo"]
print(list(OrderedDict.fromkeys(items).keys()))
```
