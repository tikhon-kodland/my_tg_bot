import random

def generate_password(l):
    s = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(l):
        password += random.choice(s)
    
    return password
