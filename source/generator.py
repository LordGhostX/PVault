# Password Generator
import string
import random

def generate_password(minimum=16, maximum=25):
    # Generates a random password
    # specify all uppercase, lowercase, numeric and special characters so our passwords contain them
    uppercase, lowercase =  string.ascii_letters[:26], string.ascii_letters[26:]
    char_list = ""
    # this ensures that every generated password has uppercase, lowercase, numeric, special characters
    while len(char_list) < maximum:
        for chars in [uppercase, lowercase, string.digits, string.punctuation]:
            char_list += "".join(random.sample(chars, random.randint(1, 3)))

    password = "".join(random.sample(char_list, random.randint(minimum, maximum)))
    return password
