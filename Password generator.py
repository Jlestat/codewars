import random
import string

def password_gen():
    length = random.randint(6, 20)

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]
    characters = string.ascii_letters + string.digits
    password += random.choices(characters, k=length - 3)
    random.shuffle(password)
    return ''.join(password)