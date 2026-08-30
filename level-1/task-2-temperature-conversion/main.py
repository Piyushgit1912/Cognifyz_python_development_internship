def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

def main():
    c = float(input('Enter temperature in Celsius: '))
    print(f'Fahrenheit: {celsius_to_fahrenheit(c)}')

if __name__ == '__main__':
    main()
