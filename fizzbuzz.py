"""FizzBuzz!!!

If number mod 3 print Fizz
If number mod 5 print Buzz
If both print FizzBuzz
"""

for i in range(100):
    if i % 15 == 0:
        print("{: 3d} FizzBuzz".format(i))
    elif i % 3 == 0:
        print("{: 3d} Fizz".format(i))
    elif i % 5 == 0:
        print("{: 3d} Buzz".format(i))
    else:
        pass
