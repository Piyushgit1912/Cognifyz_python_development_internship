def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

def main():
    n = int(input('Enter number of terms: '))
    fibonacci(n)

if __name__ == '__main__':
    main()
