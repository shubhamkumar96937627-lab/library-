import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
   
try:
    df = pd.read_csv('library_data.csv')
except FileNotFoundError:
    data = {
        'Book_ID': [101, 102, 103],
        'Title': ['Python Basics', 'Data Science 101', 'Calculus III'],
        'Category': ['Tech', 'Tech', 'Math'],
        'Status': ['Available', 'Issued', 'Available']
    }
    df = pd.DataFrame(data)

def show_analytics():
    counts = df['Category'].value_counts()
    

    plt.figure(figsize=(8, 5))
    counts.plot(kind='bar', color='green')
    plt.title('Books per Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Books')
    plt.show()

print("--- Library Management System ---")
print(df)
show_analytics()