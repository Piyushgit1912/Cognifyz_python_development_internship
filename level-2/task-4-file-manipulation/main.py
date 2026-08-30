def main():
    filename = 'level-2/task-4-file-manipulation/sample.txt'
    with open(filename, 'w') as f:
        f.write('Hello Python Internship Cognifyz File Manipulation Task.')
    
    with open(filename, 'r') as f:
        content = f.read()
        print('File Content:', content)
        print('Word Count:', len(content.split()))

if __name__ == '__main__':
    main()
