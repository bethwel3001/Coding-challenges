# Write a Python program that prints the numbers from 1 to 100. But for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

# Example output

# 1  # 2 # Fizz # 4 # Buzz # Fizz # 7 # 8 # Fizz # Buzz # 11 # Fizz # 13 # 14 # FizzBuzz # ...

# The function FizzBuzz
def FizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:  # Check if divisible by both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Check if divisible by 3
            print("Fizz")
        elif i % 5 == 0:  # Check if divisible by 5
            print("Buzz")
        else:
            print(i)  # Print the number if none of the above conditions match

# Test the function
FizzBuzz(100)




