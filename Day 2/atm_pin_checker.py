# Day 2 - ATM PIN Checker

# Store correct PIN
correct_pin = "1234"

# Initialize attempt counter
attempts = 0

# Allow maximum 3 attempts
while attempts < 3:

    # Ask user to enter PIN
    pin = input("Enter PIN: ")

    # Check if PIN is correct
    if pin == correct_pin:

        # Display success message
        print("Access Granted")

        # Exit loop
        break

    else:

        # Increase attempt count
        attempts += 1

        # Display error message
        print("Wrong PIN")

# Check if all attempts are used
if attempts == 3:

    # Display blocked message
    print("Card Blocked")

# End of program
