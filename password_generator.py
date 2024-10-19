import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine all chosen character sets
    all_characters = lowercase_letters + uppercase_letters + numbers + symbols

    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 1): "))
            if length < 1:
                print("Password length must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get user input for character set preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    # Generate the password
    try:
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
