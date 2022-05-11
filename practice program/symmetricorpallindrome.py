#Python program to check whether the string is Symmetrical or Palindrome

a=input("Enter the str: ")

if a==a[::-1]:
    print(f"{a} is pallindrome")
if a[:(len(a)//2)]== a[(len(a)//2):]:
    print("Symmetric")
