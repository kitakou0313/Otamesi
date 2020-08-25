import random
import string

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'


def genRandomLowerString():
    return ''.join(
        [random.choice(ascii_lowercase) for i in range(12)])
