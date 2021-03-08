"""FizzBuzz!!!

If number mod 3 print Fizz
If number mod 5 print Buzz
if number mod 7 print FizzyBuzzy
If both print FizzBuzz
"""

def print_fizbuzz(number):
    for i in range(number):
        if i % 15 == 0: # both 3 and 5 divide i
            print("{: 3d} FizzBuzz".format(i))
        elif i % 7 == 0:
            print("{: 3d} FizzyBuzzy".format(i))
        elif i % 3 == 0: # only 3 divides i
            print("{: 3d} Fizz".format(i))
        elif i % 5 == 0: # only 5 divides i
            print("{: 3d} Buzz".format(i))
        elif i: #it's just i
            print(i)            
        else: # neither 3 nor 5 divides i
            pass

def gen_list_fizzbuzz(number):
    for i in range(number):
        result = ""
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz\n")
        elif i % 3 == 0:
            result.append("Fizz\n")
        elif i % 5 == 0:
            result.append("Buzz\n")
        elif i % 20 == 0:
            result.append("Mandy is cool!\n")
        else:
            result.append(i)
    return result
