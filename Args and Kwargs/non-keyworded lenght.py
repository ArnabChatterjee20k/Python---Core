def mul(*args):
    '''through args we are not dependent on the number of parameters passed'''
    a = 1
    for i in args:
        a*=i
    return [args,a]
# now number of arguments is not getting mattered
print(mul(1,1,2))
print(mul(1,1,2,4,2,))
print(mul(1,1,2,4,121,3))
print(mul(1,1,2,4,2,5,6,12,1))

# we can see args is just a tuple where we are iterating.


# using with list or tuple or dictionary
ls = [1,2,3]
tp = (3,4,5)
dc = {"a":1 , "b":2}

print(*[1,2,3]) # 1 2 3
print(*tp) # 3 4 5
print(*dc) # a b

# function
def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)

my_list = [2, 3]
some_args(1, *my_list) # last two arguments are getting passed by mylist.

# if mylist would have 3 elements then it would give error then  we have to pass only *mylist
