import pandas as pd

# Load datasets with correct delimiter (tab)
literacy_data = pd.read_csv('literacy_rates.csv', delimiter='\t')
enrollment_data = pd.read_csv('enrollment_rates.csv', delimiter='\t')
spending_data = pd.read_csv('education_spending.csv', delimiter='\t')

# Check and fix column names
literacy_data.columns = literacy_data.columns.str.strip()
enrollment_data.columns = enrollment_data.columns.str.strip()
spending_data.columns = spending_data.columns.str.strip()

# Print column names to confirm consistency
print("Literacy Data Columns:", literacy_data.columns)
print("Enrollment Data Columns:", enrollment_data.columns)
print("Spending Data Columns:", spending_data.columns)

# Ensure 'Country' and 'Year' columns exist in all datasets
required_columns = ['Country', 'Year']
for dataset_name, dataset in zip(['Literacy', 'Enrollment', 'Spending'], 
                                 [literacy_data, enrollment_data, spending_data]):
    for column in required_columns:
        if column not in dataset.columns:
            raise KeyError(f"{column} is missing in {dataset_name} data.")

# Merge datasets
education_data = pd.merge(literacy_data, enrollment_data, on=['Country', 'Year'], how='inner')
education_data = pd.merge(education_data, spending_data, on=['Country', 'Year'], how='inner')

# Print merged dataset
print("Merged Education Data:")
print(education_data.head())

# Save the merged dataset to a new CSV file
education_data.to_csv('merged_education_data.csv', index=False)

# Visualization (optional, if needed for testing)
import matplotlib.pyplot as plt
import seaborn as sns

# Literacy Rates Over Time
plt.figure(figsize=(12, 6))
sns.lineplot(data=education_data, x='Year', y='Literacy_Rate', hue='Region')
plt.title('Global Literacy Rates Over Time')
plt.xlabel('Year')
plt.ylabel('Literacy Rate (%)')
plt.show()

# Education Spending vs Literacy Rate
plt.figure(figsize=(8, 6))
sns.scatterplot(data=education_data, x='Education_Spending (Billion USD)', y='Literacy_Rate', hue='Region')
plt.title('Education Spending vs Literacy Rate')
plt.xlabel('Spending (in Billion USD)')
plt.ylabel('Literacy Rate (%)')
plt.show()
