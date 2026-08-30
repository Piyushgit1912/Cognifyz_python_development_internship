import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {'Task': ['T1', 'T2', 'T3', 'T4'], 'Score': [85, 90, 95, 88]}
    df = pd.DataFrame(data)
    print(df)
    df.plot(kind='bar', x='Task', y='Score', legend=False)
    plt.title('Internship Scores')
    plt.show()

if __name__ == '__main__':
    main()
