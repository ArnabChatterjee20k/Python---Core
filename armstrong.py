def order(num):
    digits=0
    while num>0:
        digits=+1
        num=num//10
    return digits
a=order(13)
print(a)
