#  Today's Challenge: Find the Missing Number in an Array
#  You are given an array containing n distinct numbers taken from the range 0 to n (inclusive). Since one number is missing, write a function to find that missing number.

# Example 1:
# Input: [3, 0, 1]
# Output: 2

# solution
def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

# getting input from user
nums = list(map(int, input("Enter the numbers: ").split()))
print(find_missing_number(nums))  # Output: 2
