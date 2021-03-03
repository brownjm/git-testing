"""FizzBuzz!!!

If number mod 3 print Fizz
If number mod 5 print Buzz
If both print FizzBuzz
"""

for i in range(100):
    if i % 15 == 0: # both 3 and 5 divide i
        print("{: 3d} FizzBuzz".format(i))
    elif i % 3 == 0: # only 3 divides i
        print("{: 3d} Fizz".format(i))
    elif i % 5 == 0: # only 5 divides i
        print("{: 3d} Buzz".format(i))
    else: # neither 3 nor 5 divides i
        pass
