import random
import string

# Function that generates random numbers, it will generate (length) amount of letters
def gen_random_num(length):
    num = ''
    for i in range(length):
        num += str(random.randint(0, 9))
    return num

# Function that generates random letters, it will generate (length) amount of letters
def gen_random_letter(length):
    letters = ''
    for i in range(length):
        random_letter = random.choice(string.ascii_letters)
        letters += random_letter
    return letters

# Function that generates random special characters, it will generate (length) amount of letters
def gen_random_special(length):
    special = ''
    for i in range(length):
        random_special = random.choice(string.punctuation)
        special += random_special
    return special

# Randomize the order of a string
def randomize_password_order(password):
    chars = list(password)
    random.shuffle(chars)
    return ''.join(chars)

# Collect an integer from the user
def collect_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return collect_int(prompt)

# The menu for the user to input the password requirements
def menu():
    print("Secure Password Generator")
    length = collect_int("Enter the total length of the password: ")
    letters = collect_int("Enter the number of letters: ")
    numbers = collect_int("Enter the number of numbers: ")
    specials = collect_int("Enter the number of special characters: ")

    if letters + numbers + specials != length:
        print("The sum of letters, numbers, and special characters must equal the total length.")
        menu()
        return

    password = ''
    password += gen_random_num(numbers)
    password += gen_random_letter(numbers)
    password += gen_random_special(specials)

    print("Your desired password is: " + randomize_password_order(password))
    print("- Letters: " + str(letters))
    print("- Digits: " + str(numbers))
    print("- Special Characters: " + str(specials))

if __name__ == "__main__":
    menu()