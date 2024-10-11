import pandas as pd

# Load Excel file
data1 = pd.read_excel('C:\\Users\\NSL\\gumi_project\\1. +í¦--÷++¦¦++-+ +t+˜ -n+¬¦G+˜ +í¦--÷ ¦Ñ+¦+-\\data_one.xlsx')

# Preview the data
print(data1.head())

# Check for missing data
missing_data = data1.isnull().sum()
print(missing_data)

# Handle missing values by filling with median or mean
data1.fillna(data1.median(), inplace=True)

# Count of distinct values in each column
distinct_counts = data1.nunique()
print(distinct_counts)

# To see counts of distinct values for a specific column, e.g., 'Column_Name'
value_counts = data1['계측기명'].value_counts(dropna=False)
print(value_counts)

# Check data types of each column
print(data1.dtypes)

# Convert a specific column to numeric, errors='coerce' will set non-convertible values to NaN
data1['계측기명'] = pd.to_numeric(data1['계측기명'], errors='coerce')

# Fill NaN values with a number, for example, zero
data1['계측기명'].fillna(0, inplace=True)

# Preview the data
print(data1.head())

