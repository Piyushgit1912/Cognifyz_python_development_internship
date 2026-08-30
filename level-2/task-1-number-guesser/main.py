import random

def main():
    secret = random.randint(1, 100)
    print('Guess the number between 1 and 100!')
    while True:
        guess = int(input('Enter your guess: '))
        if guess < secret: print('Too low!')
        elif guess > secret: print('Too high!')
        else:
            print('Congratulations! You guessed it.')
            break

if __name__ == '__main__':
    main()
