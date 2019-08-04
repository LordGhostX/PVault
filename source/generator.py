# Password Generator
import string
import random

def generate_password(minimum=16, maximum=25):
    uppercase, lowercase =  string.ascii_letters[:26], string.ascii_letters[26:]
    char_list = ""
    while len(char_list) < maximum:
        for chars in [uppercase, lowercase, string.digits, string.punctuation]:
            char_list += "".join(random.sample(chars, random.randint(1, 3)))

    password = "".join(random.sample(char_list, random.randint(minimum, maximum)))
    return password
