
#  Write a Python function to find the second largest number in a list of integers.

def second_largest(numbers):
    # Sort the list in descending order
    numbers.sort(reverse=True)
    
    # If the list has less than two distinct elements, return None
    if len(set(numbers)) < 2:
        return None
    
    # Return the second largest number
    return numbers[1]

# Test the function
print(second_largest([4, 2, 9, 6, 5,
                      1, 8, 3, 7]))  # Output: 8

#  Write a Python function to find the second largest number in a list of integers.



