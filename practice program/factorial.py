def factorial(n):
    for i in range(1,n):
        n=n*i
    print(n)
    return n
n=int(input("Enter factorial value"))
factorial(n)
