
import pandas as pd

# Load the dataset
file_path = 'data/supply_chain_logistics_problem.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print('First 5 rows of the dataset:')
print(df.head())

# Display basic information about the DataFrame
print('\nInformation about the dataset:')
print(df.info())

# Display descriptive statistics
print('\nDescriptive statistics of the dataset:')
print(df.describe())


