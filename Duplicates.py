# Write a function that takes a list of numbers and returns a list of all duplicate numbers (numbers that appear more than once). The output should not have duplicates itself.

# Should ask the user for inputs
# Should return a list of duplicate numbers
def find_duplicates(numbers):
    # Create a dictionary to store the count of each number
    count_dict = {}
    
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1  # Fix indentation

    # Create a list to store the duplicate numbers
    duplicate_list = []
    
    for num, count in count_dict.items():
        if count > 1:
            duplicate_list.append(num)  # Append all duplicates

    return duplicate_list  # Return outside the loop, after checking all numbers

# Ask the user for inputs
numbers = input("Enter a list of numbers in the format '1 2 3': ")
numbers = [int(x) for x in numbers.split()]

# Find the duplicate numbers
duplicate_numbers = find_duplicates(numbers)

# Display result
if duplicate_numbers:
    print("The duplicate numbers are:", duplicate_numbers)
else:
    print("No duplicates❌ .")


# Example output:
# Please enter a list of numbers separated by spaces: 1 2 2 3
# The duplicate numbers are:  [2]
