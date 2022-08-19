Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s1={1,2,3,4}
s2={3,4,5,6}
s1.union(s2)
{1, 2, 3, 4, 5, 6}
s1.intersection(s2)
{3, 4}
s1-s2
{1, 2}
s2-s1
{5, 6}
s3={1,2}
print(s3)
{1, 2}
