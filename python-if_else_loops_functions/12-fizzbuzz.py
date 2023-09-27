#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        mod3 = (number % 3)
        mod5 = (number % 5)
        if mod3 == 0:
            if mod5 == 0:
                print("FizzBuzz", end=" ")
            else:
                print("Fizz", end=" ")
        else:
            if mod5 == 0:
                print("Buzz", end=" ")
            else:
                print(number, end=" ")
