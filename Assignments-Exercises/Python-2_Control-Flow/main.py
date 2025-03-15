# Try block to handle potential errors during input conversion
try:
    # Get user input and convert it to an integer
    age = int(input("Enter your age: "))
    
    # Check if age is negative (invalid)
    if age < 0:
        print("Invalid input: Age cannot be negative.")
    # Check if age is less than 13 (Child category)
    elif age < 13:
        print("You are categorized as: Child")
    # Check if age is less than 20 (Teenager category)
    elif age < 20:
        print("You are categorized as: Teenager")
    # Check if age is less than 60 (Adult category)
    elif age < 60:
        print("You are categorized as: Adult")
    # Age 60 and above (Senior category)
    else:
        print("You are categorized as: Senior")

# Catch ValueError if input cannot be converted to integer
except ValueError:
    print("Invalid input: Age cannot be a non-number.")