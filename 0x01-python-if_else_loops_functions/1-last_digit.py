#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number % 10
if number < 0:
    a = ((abs(number) % 10) * -1)
#    a = a * -1
#    print(f"Last digit of {number} is {a}")
if a > 5:
    print(f"Last digit of {number} is {a} and is greater than 5")
elif a == 0:
    print(f"Last digit of {number} is {a} and is 0")
elif a < 6 and not 0:
    print(f"Last digit of {number} is {a} and is less than 6 and not 0")
