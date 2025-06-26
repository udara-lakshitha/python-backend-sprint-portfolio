import random # For making random choices
import string # contains pre-made string of characters

# Define the character set we can use
LETTERS_LOWER = string.ascii_lowercase
LETTERS_UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation

def generate_password(length: int, use_upper: bool, use_digits: bool, use_symbols: bool) -> str:
    '''
    Generate a secure, random password based on user-specific criteria

    Args:
        length(int): the desired length of the password
        use_upper(bool): Whether to include upercase letters
        use_digits(bool): Whether to include numbers
        use_symbols(bool): Whether to include symbols

    Returns:
        str: The randomly generated password

    '''
    # Starts with mandatory lowercase letters
    char_pool = LETTERS_LOWER

    # Add othter character sets if user requested them
    if use_upper:
        char_pool += LETTERS_UPPER
    if use_digits:
        char_pool += DIGITS
    if use_symbols:
        char_pool += SYMBOLS

    password_chars = [] # Use a list to store the characters
    for _ in range(length):
        random_char = random.choice(char_pool)
        password_chars.append(random_char)

    # Join and return the password as a singnle string
    return "".join(password_chars)

if __name__ == "__main__":
    print("--- Monster Password Generation Toolkit ---")
    try:
        pass_length = int(input("Enter desired password length (e.g. 16): "))
    except ValueError:
        print("Invalid input. Please enter a number. Defaulting to 12")
        pas_length = 12

    # The .lower() in ['y', 'yes'] handles all 'y', 'yes', 'Y', 'Yes' etc
    include_upper = input('Include uppercase letters? (y/n): ').lower in ['y', 'yes']
    include_digits = input('Include numbers? (y/n): ').lower() in ['y', 'yes']
    include_symbols = input('Include symbols? (y/n): ').lower() in ['y', 'yes']

    # Call the function with user defined parameters
    final_password = generate_password(
        length = pass_length,
        use_upper = include_upper,
        use_digits = include_digits,
        use_symbols = include_symbols
    )

    # Display the final product
    print('\n' + '='*40)
    print(f' Your new secure password is {final_password}')
    print('='*40 + '\n')



