import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('sample_missing_values.csv')

# Fix the misaligned row (where 'Eve' appears in Age column)
# This happens because the Name was empty and values shifted left
mask = df['Name'].isna() & df['Age'].notna()
df.loc[mask, ['Name', 'Age', 'Gender', 'City', 'Score']] = [
    df.loc[mask, 'Age'].values[0],  # Move Age value to Name
    np.nan,                        # Set Age to NaN
    df.loc[mask, 'Gender'].values[0],  # Move Gender to correct position
    df.loc[mask, 'City'].values[0],    # Move City to correct position
    df.loc[mask, 'Score'].values[0]    # Move Score to correct position
]

# Now handle missing values properly
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Convert to numeric, forcing non-numeric to NaN
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age).astype(int)

mode_gender = df['Gender'].mode()[0]
df['Gender'] = df['Gender'].fillna(mode_gender).str.lower()

df['City'] = df['City'].fillna('Unknown').str.title()

mean_score = df['Score'].mean()
df['Score'] = df['Score'].fillna(mean_score)

# Standardize column names
df.columns = df.columns.str.lower()

# Display cleaned dataset
print(df.to_string(index=False))
