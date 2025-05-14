# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset

try:
    
    df = pd.read_csv('iris.csv')
except FileNotFoundError:
    print("Dataset file not found. Please ensure the correct file path.")
    exit()


print("First few rows of the dataset:")
print(df.head())


print("\nData Types of the Columns:")
print(df.dtypes)

print("\nMissing Values in Each Column:")
print(df.isnull().sum())


print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis


print("\nBasic Statistics for Numerical Columns:")
print(df.describe())


grouped_df = df.groupby('species').mean()
print("\nMean of Numerical Columns Grouped by Species:")
print(grouped_df)


# Task 3: Data Visualization


plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='date', y='sales')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='petal_length', data=df)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.histplot(df['sepal_length'], kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal_length', y='petal_length', data=df, hue='species', palette='viridis')
plt.title('Relationship Between Sepal Length and Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend(title='Species')
plt.tight_layout()
plt.show()


try:
    df = pd.read_csv('iris.csv')
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

# Handling missing values (if not already done)
try:
    if df.isnull().sum().any():
        print("Warning: Missing values detected, filling with the mean...")
        df.fillna(df.mean(), inplace=True)
except Exception as e:
    print(f"Error occurred during cleaning: {e}")

