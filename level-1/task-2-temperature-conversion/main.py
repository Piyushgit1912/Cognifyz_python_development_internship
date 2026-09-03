def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

c = float(input('Enter temperature in Celsius: '))
print(f'Fahrenheit: {celsius_to_fahrenheit(c)}')

