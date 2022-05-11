from collections import namedtuple

point= namedtuple("point",["x","y"]) # fields supplied can be iterable like list , string and tuple
a = point(1,2)
# print(a)

# another way to create named tuple.
student = namedtuple("student","class_ , roll , name")
stu = student(6,7,"arnab")
print(stu)

#creating named tuple by passing an iterable as an argument
stu1 = [1,2,"a"]
print(student._make(stu1))

#accessing the values by index , attributes
print(stu.name , stu[1],stu.class_)
print(getattr(stu,"name"))

# replacing value
stu = stu._replace(class_=12) #Return a new instance of the named tuple replacing specified fields with new values
print(stu)

#printing the fields
print(stu._fields)

#exporting it as dictionary format
print(stu._asdict())

# converting a dictionary to named tuple using **
stu2 = {"name":"arnab" , "roll":2 , "class_":12}
print(student(**stu2))

# creating named tuples with default values
programmer = namedtuple("Programmer",("language","skill"),defaults=(1,2))
p1=programmer(language="python")
print(p1)
print(p1._field_defaults) # field defaults in form of dictionary will get printed