# Resolve the problem!!
import string
import random
SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
UPPERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
LOWERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
NUMBERS = ['1','2','3','4','5','6','7','8','9','0']

def generate_password():
    # Start coding here
    characters = SYMBOLS + UPPERS + LOWERS + NUMBERS #This unifies all the characters availables in one variable
    password = []
    # This secures at least one character from the above lists (The problem is that there is a patron!)
    at_least_one_SYMBOL = random.choice(SYMBOLS)
    password.append(at_least_one_SYMBOL)
    at_least_one_UPPER = random.choice(UPPERS)
    password.append(at_least_one_UPPER)
    at_least_one_LOWER = random.choice(LOWERS)
    password.append(at_least_one_LOWER)
    at_least_one_NUMBER = random.choice(NUMBERS)
    password.append(at_least_one_NUMBER)

    for char in range(11):
        characters_random = random.choice(characters)# This makes a random choice from the characters
        password.append(characters_random) # Add it to the empty list
    
    print(password) # This is the pre-password 
    random.shuffle(password) # Here change the places of the characters to fix the problem from above
    password = "".join(password) #This makes the entire list one string, eliminating the commas, apostrophe and brackets. 
    print(password)

    return password

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
