Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={}
type(d)
<class 'dict'>
d["name"]="sbcc"
print(d)
{'name': 'sbcc'}
d['rno']=76
print(d)
{'name': 'sbcc', 'rno': 76}
len(D)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    len(D)
NameError: name 'D' is not defined. Did you mean: 'd'?
len(d)
2
d['rno']=32
print(d)
{'name': 'sbcc', 'rno': 32}
d['con']=22
print(d)
{'name': 'sbcc', 'rno': 32, 'con': 22}
del(d['name'])
print(d)
{'rno': 32, 'con': 22}
d.popitem()
('con', 22)
print(d)
{'rno': 32}
d.pop('rno')
32
print(d)
{}
d=dict([(1,2),(3,4).(4,5)])
SyntaxError: invalid syntax
d=dict([(1,2),(3,4),(4,5)])
print(d)
{1: 2, 3: 4, 4: 5}
d.get()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d.get()
TypeError: get expected at least 1 argument, got 0
d.keys()
dict_keys([1, 3, 4])
d.values()
dict_values([2, 4, 5])
d.getitems()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d.getitems()
AttributeError: 'dict' object has no attribute 'getitems'
d.items()
dict_items([(1, 2), (3, 4), (4, 5)])
d["name"]="rani"
print(d)
{1: 2, 3: 4, 4: 5, 'name': 'rani'}
d.popitem()
('name', 'rani')
d.popitem(keys)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d.popitem(keys)
NameError: name 'keys' is not defined
d.popitems(keys)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d.popitems(keys)
AttributeError: 'dict' object has no attribute 'popitems'. Did you mean: 'popitem'?
