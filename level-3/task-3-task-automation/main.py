import os

def main():
    print('Scanning current directory for automation...')
    for root, dirs, files in os.walk('.'):
        print(f'Directory: {root} contains {len(files)} files.')
        break

if __name__ == '__main__':
    main()
