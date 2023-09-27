#!/usr/bin/python3
# print whether the number stored in the variable number is > 0 or < 0
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = digit * -1
if digit == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
