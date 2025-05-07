import pandas as pd

# Load the Shark Tank dataset
file_path = r"C:\ELEVATE LABS\Task 9, PROJECT\Shark Tank India.csv"
df = pd.read_csv(file_path)

# Selecting relevant columns for analysis
columns_required = [
    'Season Number', 'Original Air Date', 'Startup Name', 'Industry', 'Business Description',
    'Original Ask Amount', 'Original Offered Equity', 'Valuation Requested',
    'Received Offer', 'Accepted Offer', 'Total Deal Amount', 'Total Deal Equity',
    'Invested Guest Name', 'All Guest Names',
    'Number of Presenters', 'Male Presenters', 'Female Presenters',
    'Pitchers Average Age', 'Pitchers City', 'Pitchers State'
]
df_cleaned = df[columns_required].copy()

# Converting air date to datetime format
df_cleaned['Original Air Date'] = pd.to_datetime(df_cleaned['Original Air Date'], errors='coerce')

# Clean string/text columns
text_columns = [
    'Startup Name', 'Industry', 'Business Description',
    'Pitchers City', 'Pitchers State', 'Invested Guest Name', 'All Guest Names'
]
df_cleaned[text_columns] = df_cleaned[text_columns].applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Save cleaned data to CSV
df_cleaned.to_csv("CLEAN_DATA.csv", index=False)

print("✅ Data cleaned and saved as 'CLEAN_DATA.csv'")
