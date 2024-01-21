"""
Created by Ignorant on 2024/1/20
Description: Dictionary
"""

# element: key-value
# no index / slice

'''
add
    1.dict[key] = value
        if key is exist, modify the value, else add the new key-value pair to the dictionary
    2.setdefault(self: MutableMapping[_KT, _T | None], __key: _KT, __default: None = None) -> _T | None
        add new key-value element but do not modify the existing one
    3.update
'''
dict1 = {"name": "Carl", "age": 18, "gender": 'M'}
dict1["age"] += 1
dict1["score"] = 95
print(dict1)
dict1.setdefault("id", 231880174)
print(dict1)
dict1.setdefault("id", 221550123)
print(dict1)

dict2 = {"a": 12345}
dict1.update(dict2)
print(dict1)
print()

'''
delete
    1.pop(self, __key: _KT) -> _VT
        Remove specified key and return the corresponding value.
        If key is not found, default is returned if given, otherwise KeyError is raised
    
    2.popitem(self) -> tuple[_KT, _VT]
        Remove the last element and return a tuple[_KT, _VT]
        Raise KeyError if the dictionary is empty.
    
    3.del
        del dict
        del dict[key]
    
    4.clear(self) -> None
'''

value = dict1.pop("a")
print(value)
print(dict1)

value = dict1.popitem()
print(value)
print(dict1)

del dict1["score"]
print(dict1)

dict1.clear()
print(dict1)
print()

'''
query
    get(self, __key: _KT) -> _VT | None
        Return the value for key if key is in the dictionary, else default(None if default).
'''
dict3 = {"name": "Three Body", "price": 20, "author": "CiXin Liu"}
value = dict3.get("name")
print(value)
value = dict3.get("name1", "Hello")
print(value)
print()

'''
iteration
    1.values(self): return an object providing a view on dictionary's values
    2.keys(self): return an object providing a view on dictionary's keys
    3.items(self): providing a view on D's items in the form of [(key, value), ...]
'''
for i in dict3:
    print(i)
print()

for i in dict3.values():
    print(i)
print()
# for i in dict3.keys():
#     print(i)

print(dict3.items())
for k, v in dict3.items():
    print(k + ": " + str(v))
print()

'''
fromkeys(cls,  __iterable: Iterable[_T], __value: None = None) -> dict[_T, Any | None] 
    Create a new dictionary with keys from iterable and values set to value.
'''
result = dict.fromkeys(['a', 'b'], [10, 20])
print(result)
