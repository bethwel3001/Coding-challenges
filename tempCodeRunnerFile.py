# Get user input
numbers = input("Enter a list of numbers separated by space: ")
numbers = [int(num) for num in numbers.split()]

# Find and print the most frequent number
print("The most frequent number is:", most_frequent(numbers))
