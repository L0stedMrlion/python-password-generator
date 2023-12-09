def generate_password(length, include_numbers=True, include_special_characters=True):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special_characters:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

language = input("🌐 Choose a language (en/cz/ru): ").lower()

if language in ['en', 'english']:
    prompt_length = "🔐 How many characters do you want your password to be? "
    prompt_numbers = "🔢 Include numbers in the password? (yes/no): "
    prompt_special = "🎨 Include special characters like {}[]()? (yes/no): "
    generated_message = "🔑 Generated Password:"
    error_message = "❌ Please enter a positive integer for the password length."

elif language in ['cz', 'czech']:
    prompt_length = "🔐 Kolik znaků má mít vaše heslo? "
    prompt_numbers = "🔢 Má obsahovat čísla? (ano/ne): "
    prompt_special = "🎨 Má obsahovat speciální znaky {}[]()? (ano/ne): "
    generated_message = "🔑 Vygenerované heslo:"
    error_message = "❌ Zadejte prosím kladné celé číslo pro délku hesla."

elif language in ['ru', 'russian']:
    prompt_length = "🔐 Сколько символов должен содержать ваш пароль? "
    prompt_numbers = "🔢 Включить цифры в пароль? (да/нет): "
    prompt_special = "🎨 Включить специальные символы типа {}[]()? (да/нет): "
    generated_message = "🔑 Сгенерированный пароль:"
    error_message = "❌ Пожалуйста, введите положительное целое число для длины пароля."

else:
    print("❌ Unsupported language. Please choose 'en' or 'english' for English, 'cz' or 'czech' for Czech, or 'ru' or 'russian' for Russian.")
    exit()

try:
    length = int(input(prompt_length))
    if length <= 0:
        print(error_message)
    else:
        include_numbers = input(prompt_numbers).lower() in ['yes', 'y', 'ano', 'a', 'да', 'д']

        include_special = input(prompt_special).lower() in ['yes', 'y', 'ano', 'a', 'да', 'д']

        password = generate_password(length, include_numbers=include_numbers, include_special_characters=include_special)
        print(generated_message, password)
except ValueError:
    print(error_message)