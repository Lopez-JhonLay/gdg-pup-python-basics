# Create a list of favorite foods
foods = ['Rice', 'Cake', 'Ice Cream', 'Carbonara', 'Fried Chicken']

# Print favorite foods using a for loop
print("Favorite foods:")
for food in foods:
    print(f"- {food}")  # Add bullet point before each food item

print()  # Add blank line between sections

# Get starting number and handle countdown
try:
    num = int(input("Enter countdown start (positive number): "))
    
    # Validate input is positive
    if num <= 0:
        print("Invalid input: Please enter a number greater than zero.")
    else:
        print("Countdown:")
        # Count down from num to 1 using while loop
        while num > 0:
            print(num)    # Display current number
            num -= 1      # Decrease number by 1
        print("Countdown complete!")    # Indicate countdown completion

# Catch non-numeric input errors
except ValueError:
    print("Error: Please enter a valid number.")