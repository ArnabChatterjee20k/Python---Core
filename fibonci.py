#0 1 1 2 3 5 8 11....n
def fibonci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        a= fibonci(n-1)+fibonci(n-2)
        return a
print(fibonci(7))
