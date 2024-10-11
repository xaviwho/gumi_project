import pandas as pd

# Load Excel file
data1 = pd.read_excel('C:\\Users\HP\\Downloads\\1. 에너지자급자족 사업 참여기업 에너지 데이터\\1. +í¦--÷++¦¦++-+ +t+˜ -n+¬¦G+˜ +í¦--÷ ¦Ñ+¦+-\\data_one.xlsx')

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

