import re

class UsernameContainsIllegalCharacter(Exception):
    """
    Exception of illegal character found in username
    Valid Characters: english chars, digits, underscore
    """
    def __init__(self, char, index):
        self._char = char
        self._i = index

    def __str__(self):
        return f'The username contains the illegal character "{self._char}" at index {self._i}'


class UsernameTooShort(Exception):
    """
    Exception of a username that is too short
    Minimum length: 3 
    """
    def __str__(self):
        return 'The username is too short, shorter than 3 chars'


class UsernameTooLong(Exception):
    """
    Exception of a username that is too long
    Maximum length: 16 
    """
    def __str__(self):
        return 'The username is too long, can\'t be longer than 16 chars'


class PasswordMissingCharacter(Exception):
    """
    Exception of a password that is missing a required character
    Required characters: Uppercase char, Lowercase char, a digit, and a special char (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
    """
    def __init__(self, missing):
        self._missing = missing

    def __str__(self):
        return f'The password is missing a character ({self._missing})'


class PasswordTooShort(Exception):
    """
    Exception of a password that is too short
    Minimum length: 8 
    """
    def __str__(self):
        return 'The password is too short, shorter than 8 chars'


class PasswordTooLong(Exception):
    """
    Exception of a password that is too long
    Maximum length: 40 
    """
    def __str__(self):
        return 'The password is too long, can\'t be longer than 40 chars'



def check_input(username, password):
    """
    Function to check if username and password are valid
    Username is valid if its length is bigger than 3 and smaller than 16, and only includes chars, digits and underscore
    Password is valid if its length is bigger than 8 and smaller than 40, and includes at least one Uppercase letter, one Lowercase letter, one Digit, and one Special character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
    if something is invalid, the function calls an execption specefic to whats invalid.
    if everything is valid, prints "OK"
    :param username: the username to check
    :type username: str
    :param password: the password to check
    :type password: str
    """
    # Username length
    if len(username) < 3:
        raise UsernameTooShort
    elif len(username) > 16:
        raise UsernameTooLong

    # Regex for chars, digits and underscore
    regex = re.compile(r'[a-zA-Z0-9_]')
    for i, char in enumerate(username):
        if not regex.match(char):
            raise UsernameContainsIllegalCharacter(char, i)

    # Password length
    if len(password) < 8:
        raise PasswordTooShort
    elif len(password) > 40:
        raise PasswordTooLong    

    # Password has all required chars
    if not re.compile(r'[a-z]').search(password):
        raise PasswordMissingCharacter("Lowercase")
    elif not re.compile(r'[A-Z]').search(password):
        raise PasswordMissingCharacter("Uppercase")
    elif not re.compile(r'[0-9]').search(password):
        raise PasswordMissingCharacter("Digit")
    elif not re.compile(r'[!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~]').search(password):
        raise PasswordMissingCharacter("Special")
    
    print("OK")


def main():
    input_approved = False
    while not input_approved:
        try:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            check_input(username, password)
            input_approved = True
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()