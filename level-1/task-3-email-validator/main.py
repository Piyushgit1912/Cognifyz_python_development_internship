import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def main():
    email = input('Enter email to validate: ')
    print('Valid!' if is_valid_email(email) else 'Invalid!')

if __name__ == '__main__':
    main()
