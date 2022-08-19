Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=(1,2,3)
type(t)
<class 'tuple'>
print(t)
(1, 2, 3)
x=list(t)
type(t)
<class 'tuple'>
type(x)
<class 'list'>
x[0]=888
print(x)
[888, 2, 3]
print(t)
(1, 2, 3)
t=tuple(x)
print(t)
(888, 2, 3)
s1={1,2,3}
print(s1)
{1, 2, 3}
s2={3,4,5}
print(s2)
{3, 4, 5}
print(s1)
{1, 2, 3}
print(s2)
{3, 4, 5}
type(s2)
<class 'set'>
type(s1)
<class 'set'>
s1.union(s2)
{1, 2, 3, 4, 5}
s1.intersection(s2)
{3}
s1=65.6
type(s1)
<class 'float'>
s1.difference(s2)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s1.difference(s2)
AttributeError: 'float' object has no attribute 'difference'
s3={3,4,5}
print(s3)
{3, 4, 5}
s4={4,5,6}
s3.difference(s4)
{3}
s3-s4
{3}
s4-s3
{6}
s3.update({6,7,8})
print(s3)
{3, 4, 5, 6, 7, 8}
s3.difference update(s4)
SyntaxError: invalid syntax
s3.differenceupdate(s4)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s3.differenceupdate(s4)
AttributeError: 'set' object has no attribute 'differenceupdate'. Did you mean: 'difference_update'?
