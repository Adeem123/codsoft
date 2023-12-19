import random

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

num=int(input("Enter any number: "))
a=random.choices(abc, k = num)
c="".join(a)

print(c)
