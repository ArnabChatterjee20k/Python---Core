Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="ab cd ef gh ij kl"
>>> a.index("a")
0
>>> a.index("ab")
0
>>> a.index("cd")
3
>>> a.index("d")
4
>>> a.index("d ef")
4
>>> 