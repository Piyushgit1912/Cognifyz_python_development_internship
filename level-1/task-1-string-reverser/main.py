def reverse_string(text: str) -> str:
    return text[::-1]


user_input = input('Enter a string to reverse: ')
print(f'Reversed: {reverse_string(user_input)}')
