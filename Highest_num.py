
#  Write a Python function to find the second largest number in a list of integers.

# should take the list from a user as input
# should return the second largest number in the list
def second_largest(nums):
    # Check if the list has less than 2 elements
    if len(nums) < 2:
        return None
    # Remove duplicates by converting the list to a set
    unique_nums = set(nums)
    # Convert the set back to a list and find the largest number
    largest = max(unique_nums)
    # Remove the largest number from the list
    unique_nums.remove(largest)
    # Find the second largest number
    second_largest = max(unique_nums)
    return second_largest

# Get user input
nums = input("Enter a list of numbers separated by space: ").split()
nums = [int(num) for num in nums]
# Call the function and print the result starting with, the seconsd largest num is:

print("The second largest number in the list is:", second_largest(nums))




