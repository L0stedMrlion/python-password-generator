import random
import string

def generate_password(length, include_numbers=True, include_special_characters=True):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special_characters:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

try:
    length = int(input("🔐 How many characters do you want your password to be? "))
    if length <= 0:
        print("❌ Please enter a positive integer for the password length.")
    else:
        include_numbers = input("🔢 Include numbers in the password? (yes/no): ").lower() in ['yes', 'y']

        include_special = input("🎨 Include special characters like {}[]()? (yes/no): ").lower() in ['yes', 'y']

        password = generate_password(length, include_numbers=include_numbers, include_special_characters=include_special)
        print("🔑 Generated Password:", password)
except ValueError:
    print("❌ Please enter a valid integer for the password length.")
