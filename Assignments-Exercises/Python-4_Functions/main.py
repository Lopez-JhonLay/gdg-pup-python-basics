def create_greeting(name):
    # Simple function to make a welcome message with given name
    return f"Hi {name}! Welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"

# Get name and show greeting
name = input("What's your name? ")  # Ask for user's name

# Check if name is empty or just whitespace
if name.strip() == "":
    print("Invalid input: Please enter a valid name.")  # Error message for invalid input
else:
    message = create_greeting(name)  # Make the greeting with the name
    print(message)                  # Show the greeting