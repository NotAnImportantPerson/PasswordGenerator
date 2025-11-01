import random
import string
def passwordgenerator():
    asciiv = string.ascii_letters + string.digits + string.punctuation
    randomv = random.randint(10, 12)
    password = ''.join(random.choice(asciiv) for _ in range(randomv))
    return password

print("Generated password:", passwordgenerator())