import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input for password requirements
length = int(input("Enter the length of the password: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

# Generate the random password
password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)

print(f"Generated Password: {password}")
