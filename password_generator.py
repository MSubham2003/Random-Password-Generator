from logging import exception
import random as r
lower ="abcdefghijklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number ="0123456789"
symbol ="@#$*"
all =lower + upper + number + symbol
try:
    length=int(input("Enter password length "))
    password= "".join(r.sample(all,length))
    print("Generated password is ",password)
except Exception as e:
    print("Please enter password length in numbers")

