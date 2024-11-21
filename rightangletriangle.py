# My first leetcode solution to a coding problem
# Given an integer n, print a right angled triangle of height  n
# where the triangle is made up of the character X

# X
# XX
# XXX
# XXXX
# XXXXX

# Solution

# defining the triangle function
def print_triangle(n):

    # incrementing the value of i
    for i in range(1, n+1):

        # printing the value of i
        print("X" * i)

# print the triangle function
print_triangle(5)