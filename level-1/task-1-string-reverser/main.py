def reverse_string(text: str) -> str:
    return text[::-1]

def main():
    user_input = input('Enter a string to reverse: ')
    print(f'Reversed: {reverse_string(user_input)}')

if __name__ == '__main__':
    main()
