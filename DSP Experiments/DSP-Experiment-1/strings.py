Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c="rahelu"
print(c)
rahelu
c.capitalize()
'Rahelu'
s="rainy season is beautiful"
s.count(s)
1
s.count(e)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.count(e)
NameError: name 'e' is not defined
c.len()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    c.len()
AttributeError: 'str' object has no attribute 'len'
len(c)
6
c="rahelu"
c.endswith(u)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c.endswith(u)
NameError: name 'u' is not defined
c.endswith("u")
True
c.endswith("r")
False
c.startswith("r")
True
c.startswith("a")
False
s="apple"
s.index("p")
1
s.index("l")
3
x="abc123"
x.isalnum()
True
a="abc 123"
a.isalnum()
False
s="1223"
s.isalnum()
True
q="absid"
q.isalnum()
True
r="Rahelu"
r.isalpha()
True
s="varsha"
s.isalpha()
True
w="s180649"
w.isalpha()
False
w.isascii()
True
r.isascii()
True
s="124445"
s.isascii()
True
s.isdigit()
True
w.isdigit()
False
s.islower()
False
s.isupper()
False
s="varsha"
s.isupper()
False
s.islower()
True
x="PANDU"
x.lower()
'pandu'
x.upper()
'PANDU'
s.upper()
'VARSHA'
x.isspace()
False
s="r a h e l u"
s.isspace()
False
a=" "
a.isspace()
True
x.istitle()
False
s="Krishna Chaitanya"
s.istitle()
True
s="nikhil"
s.swapcase()
'NIKHIL'
v="roses are red"
v.partition("are")
('roses ', 'are', ' red')
