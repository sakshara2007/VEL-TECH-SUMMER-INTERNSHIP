# Day 2 - Multiplication Table Generator

# Function to generate multiplication table
def times_table(number):

    # Display table heading
    print("\nMultiplication Table of", number)

    # Loop from 1 to 10
    for i in range(1, 11):

        # Calculate multiplication result
        result = number * i

        # Display result
        print(f"{number} x {i} = {result}")

# Generate table for 2
times_table(2)

# Generate table for 5
times_table(5)

# Generate table for 10
times_table(10)

# End of program