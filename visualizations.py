
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/home/ubuntu/logistics_data_science_project/data/supply_chain_logistics_problem.xlsx'
df = pd.read_excel(file_path)

# Set style for plots
sns.set_style("whitegrid")

# Plot 1: Distribution of Ship Late Day count
plt.figure(figsize=(10, 6))
sns.histplot(df["Ship Late Day count"], bins=20, kde=True)
plt.title("Distribution of Ship Late Day Count")
plt.xlabel("Ship Late Day Count")
plt.ylabel("Frequency")
plt.savefig("reports/ship_late_day_count_distribution.png")
plt.close()

# Plot 2: Ship Late Day count by Origin Port
plt.figure(figsize=(12, 7))
sns.boxplot(x="Origin Port", y="Ship Late Day count", data=df)
plt.title("Ship Late Day Count by Origin Port")
plt.xlabel("Origin Port")
plt.ylabel("Ship Late Day Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/ship_late_day_count_by_origin_port.png")
plt.close()

# Plot 3: Ship Late Day count by Carrier
plt.figure(figsize=(12, 7))
sns.boxplot(x="Carrier", y="Ship Late Day count", data=df)
plt.title("Ship Late Day Count by Carrier")
plt.xlabel("Carrier")
plt.ylabel("Ship Late Day Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("reports/ship_late_day_count_by_carrier.png")
plt.close()

# Plot 4: Ship Late Day count by Service Level
plt.figure(figsize=(10, 6))
sns.boxplot(x="Service Level", y="Ship Late Day count", data=df)
plt.title("Ship Late Day Count by Service Level")
plt.xlabel("Service Level")
plt.ylabel("Ship Late Day Count")
plt.savefig("reports/ship_late_day_count_by_service_level.png")
plt.close()

print("Visualizations generated and saved in the reports directory.")


