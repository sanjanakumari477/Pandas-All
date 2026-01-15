import pandas as pd
data = {
    'Name': ['Sana', 'Ananya', 'Ravi', 'Sneha'],
    'Age': [22, 25, 22, 24],
    'City': ['Delhi', 'Mumbai', 'Chennai', 'Bangalore']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Display basic info
print("\nBasic Information:")
print(df.info())

# Describe numerical columns
print("\nStatistics:")
print(df.describe())

# Access specific column
print("\nNames column:")
print(df['Name'])

# Filter data
print("\nPeople older than 23:")
print(df[df['Age'] > 23])
