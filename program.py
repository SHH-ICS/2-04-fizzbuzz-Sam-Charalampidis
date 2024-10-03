# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32

result = ""
for myNumber in range(32):
  if (myNumber+1) % 15 == 0:
    result = str(result) + "FizzBuzz\n"
  elif (myNumber+1) % 5 == 0:
    result = str(result) + "Buzz\n"
  elif (myNumber+1) % 3 == 0:
    result = str(result) + "Fizz\n"
  else:
    result = str(result) + str(myNumber+1) + "\n"

print(result)
