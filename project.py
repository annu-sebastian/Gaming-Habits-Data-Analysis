import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
file_name = "Gaming_Hours_Data_Cleaning.xlsx"
df = pd.read_excel(file_name)
print("🎯 Dataset successfully loaded!")

# 2. DATA CLEANING
# Replace the anomaly 'U0001' in Focus_Level with a standard value (e.g., 5)
df['Focus_Level'] = df['Focus_Level'].replace('U0001', 5)

# Convert the Focus_Level column to numeric type
df['Focus_Level'] = pd.to_numeric(df['Focus_Level']) 
print("✅ Data cleaning completed successfully!")

# 3. DATA VISUALIZATION
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Daily_Gaming_Hours', y='Sleep_Hours', hue='Performance_Impact')
plt.title('Impact of Daily Gaming Hours on Sleep Duration')
plt.xlabel('Daily Gaming Hours')
plt.ylabel('Sleep Hours')

# Save the generated chart as an image
plt.savefig('gaming_vs_sleep.png')
print("📊 Visualization saved as 'gaming_vs_sleep.png'!")

# 4. EXPORT CLEANED DATA
df.to_excel("Cleaned_Gaming_Data.xlsx", index=False)
print("💾 Cleaned dataset saved as 'Cleaned_Gaming_Data.xlsx'!")