import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
dataset = pd.read_csv('Placement_Dataset.csv')

print(dataset.head())
print(dataset.shape)
print(dataset.isnull().sum())

# Visualization of missing data column (salary)
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data=dataset, x='salary', kde=True, ax=ax)
ax.set_title("Salary Distribution")
ax.set_xlabel("Salary")
plt.show()

# ================================
# Missing Value Imputation
# ================================

dataset['salary'].fillna(dataset['salary'].median(), inplace=True)

print(dataset.isnull().sum())

# ================================
# Reload dataset for dropping method
# ================================

salary_dataset = pd.read_csv('Placement_Dataset.csv')

print(salary_dataset.shape)
print(salary_dataset.isnull().sum())

# Drop rows with missing values
salary_dataset = salary_dataset.dropna(how='any')

print(salary_dataset.isnull().sum())
print(salary_dataset.shape)