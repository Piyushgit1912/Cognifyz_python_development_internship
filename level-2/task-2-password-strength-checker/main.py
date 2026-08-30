import re

def check_password(pwd: str) -> str:
    if len(pwd) >= 8 and re.search(r'[A-Z]', pwd) and re.search(r'[0-9]', pwd) and re.search(r'[\W_]', pwd):
        return 'Strong Password'
    return 'Weak Password'

def main():
    pwd = input('Enter password to check: ')
    print(check_password(pwd))

if __name__ == '__main__':
    main()
