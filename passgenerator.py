# Password generator using python

import random
import string

# Function to generate a random password
def generate_password(length, complexity):
    # Define character sets for different complexities
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Creating a pool of characters based on complexity level
    char_pool = lower_case
    if complexity >= 2:
        char_pool += upper_case
    if complexity >= 3:
        char_pool += digits
    if complexity >= 4:
        char_pool += special_characters

    # Generate the password by choosing random characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length and complexity
    try:
        length = int(input("Enter the desired password length: "))
        complexity = int(input("Enter the complexity level (1 = lowercase only, 2 = lowercase + uppercase, 3 = lowercase + uppercase + digits, 4 = full complexity): "))
        
        if length < 1:
            print("Password length must be at least 1.")
            return
        if complexity not in range(1, 5):
            print("Invalid complexity level. Please enter a value between 1 and 4.")
            return
        
        # Generate and display the password
        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
        
    except ValueError:
        print("Please enter valid numerical values for length and complexity.")

if __name__ == "__main__":
    main()
