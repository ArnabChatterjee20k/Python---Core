# me=1
# print("this is string %s"%me)
# al= "but dont use it"
#
# print("this is string %s %s"%(me, al))
import math

me = "Harry"
a1 =3
# a = "this is %s %s"%(me, a1)
# a = "This is {1} {0}"#### here 1 will be for al and 0 is for me
# b = a.format(me, a1)
# print(b)
a = f"this is {me} {a1} {math.cos(65)}"
# time
print(a)