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

with open("langs/lang.json", "r", encoding="utf-8") as lang_file:
    lang_data = json.load(lang_file)

print("🌐 Available Languages:")
for code, name in lang_data.items():
    print(f"{code}: {name}")

selected_lang_code = input("🌐 Choose a language code (e.g., en/cz/ru): ").lower()

if selected_lang_code not in lang_data:
    print("❌ Invalid language code.")
    exit()

with open(f"langs/{selected_lang_code}.json", "r", encoding="utf-8") as prompts_file:
    prompts = json.load(prompts_file)

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
