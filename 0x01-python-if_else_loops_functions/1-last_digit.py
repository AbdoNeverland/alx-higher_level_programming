#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = "0"
l = (number % 10)
if number < 0:
    l *= -1
if l > 5:
    s = "greater than 5"
elif l == 0:
    s = "0"
else:
    s = "less than 6 and not 0"
print(f"Last digit of {number} is {l} and is {s}")
