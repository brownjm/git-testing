"""FizzBuzz!!!

If number mod 3 print Fizz
If number mod 5 print Buzz
If both print FizzBuzz
"""

for i in range(100):
    result = ""
    if i % 3 == 0 and i % 5 == 0:
        result.append("FizzBuzz\n")
    elif i % 3 == 0:
        result.append("Fizz\n")
    elif i % 5 == 0:
        result.append("Buzz\n")
    elif i % 20:
        result.append("Mandy is c00l\n")
    else:
        result.append(i)

print(result)
