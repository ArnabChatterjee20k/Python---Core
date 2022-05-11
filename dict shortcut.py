Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=dict([1,2])
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=dict([1,2])
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> a=dict([(1,2)])
>>> a
{1: 2}
>>> 