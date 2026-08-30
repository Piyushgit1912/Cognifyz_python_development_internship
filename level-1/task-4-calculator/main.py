def main():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    op = input('Enter operator (+, -, *, /): ')
    if op == '+': print(f'Result: {a + b}')
    elif op == '-': print(f'Result: {a - b}')
    elif op == '*': print(f'Result: {a * b}')
    elif op == '/': print(f'Result: {a / b if b != 0 else \"Error: Division by zero\"}')
    else: print('Invalid operator')

if __name__ == '__main__':
    main()
