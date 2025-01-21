import random
import string

#Function that generates random numbers, it will generate (length) amount of letters
def gen_random_num(length):
    num = ''
    for i in range(length):
        num += str(random.randint(0, 9))
    return num

#Function that generates random letters, it will generate (length) amount of letters
def get_random_letter(length):
    random_letter = ''
    letters = ''
    for i in range(length):
        random_letter = random.choice(string.ascii_letters)
        letters += random_letter
    return letters

#Function that generates random special characters, it will generate (length) amount of letters
def get_random_special (length):
    random_special = ''
    special = ''
    for i in range(length):
        random_special = random.choice(string.punctuation)
        special += random_special
    return special

print(gen_random_num(10))
print(get_random_letter(10))
print(get_random_special(10))
