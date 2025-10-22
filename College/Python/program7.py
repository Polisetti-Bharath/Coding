import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Original data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", None],
    "Age": [25, 30, None, 40, 22, 28],
    "Salary": [40000, 42000, 43000, 1000000, 45000, 47000],
    "Department": ["HR", "IT", "Finance", "IT", None, "HR"]
}

df = pd.DataFrame(data)

print("Dataset Overview")
print(df.head())
print("\nInfo:")
print(df.info())
print("\nSummary Stats:")
print(df.describe(include='all'))

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
df['Name'] = df['Name'].fillna('Unknown')

# Handle outliers in Salary using IQR
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df['Salary'] = np.where(df['Salary'] < lower_bound, lower_bound,
                        np.where(df['Salary'] > upper_bound, upper_bound, df['Salary']))

# Normalize Age and Salary using MinMaxScaler
scaler = MinMaxScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

# Encode Department -> create a new column instead of replacing
le = LabelEncoder()
df['Department_Encoded'] = le.fit_transform(df['Department'])

# Display final processed data
print("\nFinal Processed Data with Encoded Department Column:")
print(df)

print("\nDepartment and Encoded Values:\n")
print(df[['Department', 'Department_Encoded']])
