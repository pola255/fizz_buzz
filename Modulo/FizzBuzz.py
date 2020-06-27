"""
Write a program that prints the numbers from 1 to 100. But for multiples of three print 
“Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which 
are multiples of both three and five print “FizzBuzz”
"""


def number_generator():
    for number in range(1, 101):
        print(fizzBuzz(number))


def fizz_buzz(i):

    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i
