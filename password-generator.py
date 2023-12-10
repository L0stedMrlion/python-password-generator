import json
import random

def generate_password(length, include_numbers=True, include_special_characters=True):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special_characters:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

language = input("🌐 Choose a language (en/cz/ru): ").lower()

with open(f"langs/{language}.json", "r", encoding="utf-8") as file:
    prompts = json.load(file)

try:
    length = int(input(prompts["length_prompt"]))
    if length <= 0:
        print(prompts["error_message"])
    else:
        include_numbers = input(prompts["numbers_prompt"]).lower() in ['yes', 'y', 'ano', 'a', 'да', 'д']

        include_special = input(prompts["special_prompt"]).lower() in ['yes', 'y', 'ano', 'a', 'да', 'д']

        password = generate_password(length, include_numbers=include_numbers, include_special_characters=include_special)
        print(prompts["generated_message"], password)
except ValueError:
    print(prompts["error_message"])
