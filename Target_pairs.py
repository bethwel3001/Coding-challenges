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
# Get user input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target sum: "))

# Call the function
print("Pairs that sum to", target, ":", find_pairs(numbers, target))

# working 💯