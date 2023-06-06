#!/usr/bin/python3
import random
number = random.randint(-10, 10)
sign = "zero"
if (number > 0):
    sign = "positive"
elif number < 0:
    sign = "negative"
print(f"{number} is {sign}")
