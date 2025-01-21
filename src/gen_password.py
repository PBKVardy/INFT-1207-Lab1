import random
import string

def gen_random_num(length):
    num = ''
    for i in range(length):
        num += str(random.randint(0, 9))
    return num