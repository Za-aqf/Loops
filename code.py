# Filename: odd_even_list_check.py
# Description: This program creates a list of 15 numbers and uses a for loop
#              to determine if each number is odd or even.
# Author: [Your Name]
# Date: [Today's Date]

# Step 1: Create a list of 15 numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Step 2: Loop through each number in the list
for number in numbers:
    # Step 3: Use modulus operator to determine if number is even or odd
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
