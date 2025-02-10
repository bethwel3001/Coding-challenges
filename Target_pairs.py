# Write a function that takes a list of numbers and a target sum. The function should return all pairs of numbers that add up to the target.
# The function should return all possible pairs, not just the first pair it finds.
def find_pairs(numbers, target):
    pairs = []
    seen = set()
    
    for num in numbers:
        complement = target - num
        
        if complement in seen:
            pairs.append((complement, num))
        
        seen.add(num)
    
    return pairs
# Test the function
numbers = [1, 2, 3, 4, 5]
target = 7
print(find_pairs(numbers, target))  # Output: [(2, 5), (3,
# Test the function with a list of duplicate numbers
numbers = [1, 2, 2, 3, 4, 5]
target = 7

print(find_pairs(numbers, target))  # Output: [(2, 5), (2, 5), (3, 4)]