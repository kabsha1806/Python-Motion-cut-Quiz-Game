import random
import string

def generate_password(length=12):
    """
    Generate a random password of given length.

    Args:
    length (int): Length of the password. Default is 12.

    Returns:
    str: Random password.
    """
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords):
    """
    Generate multiple random passwords with different lengths.

    Args:
    num_passwords (int): Number of passwords to generate.

    Returns:
    list: List of tuples containing password and its length.
    """
    passwords = []
    for i in range(num_passwords):
        length = int(input(f"Enter the length for password {i + 1}: "))
        password = generate_password(length)
        passwords.append((password, length))
    return passwords

if __name__ == "__main__":
    num_passwords = int(input("Enter the number of passwords to generate: "))

    generated_passwords = generate_multiple_passwords(num_passwords)

    print("\nGenerated Passwords:")
    for password, length in generated_passwords:
        print(f"Password (length {length}): {password}")
