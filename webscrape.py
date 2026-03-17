import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def dataset(file_path):
    data = pd.read_csv(file_path, encoding='latin-1')

    print("First five rows of the dataset:")
    print(data.head())

    print("\nColumns in dataset:")
    print(data.columns)

    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) >= 2:
        x = numeric_cols[0]
        y = numeric_cols[1]

        plt.figure()
        sns.scatterplot(x=data[x], y=data[y])
        plt.title("Scatter Plot")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()

    if len(numeric_cols) >= 1:
        column = numeric_cols[0]

        plt.figure()
        sns.histplot(data[column], kde=True)
        plt.title("Histogram")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

    plt.figure()
    sns.heatmap(data[numeric_cols].corr(), annot=True)
    plt.title("Correlation Heatmap")
    plt.show()


file_path = input("Enter the CSV file path: ").strip('"')
dataset(file_path)
