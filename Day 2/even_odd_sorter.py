# Day 2 - Even/Odd Sorter

# Function to separate even and odd numbers
def sort_numbers(numbers):

    # Create empty list for even numbers
    even = []

    # Create empty list for odd numbers
    odd = []

    # Loop through each number
    for num in numbers:

        # Check if number is even
        if num % 2 == 0:

            # Add to even list
            even.append(num)

        else:

            # Add to odd list
            odd.append(num)

    # Return both lists
    return even, odd

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call function
even, odd = sort_numbers(numbers)

# Display even numbers
print("Even Numbers:", even)

# Display odd numbers
print("Odd Numbers:", odd)

# End of program
