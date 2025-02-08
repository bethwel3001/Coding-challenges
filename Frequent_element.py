# Write a function that takes a list of numbers as input and returns the most frequently occurring number. If multiple numbers have the same highest frequency, return any one of them.

# should take the input from the user
numbers = input("Enter a list of numbers separated by space: ")
numbers = [int(num) for num in numbers.split()]
def most_frequent(numbers):
    count = {}
    for num in numbers:
        if num in count:
            count[num] += 1
            else:
count[num] = 1
max_count = max(count.values())
most_frequent_num = [num for num, freq in count.items() if freq == max_count
                     return most_frequent_num[0]
]
