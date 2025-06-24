
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset
file_path = '/home/ubuntu/logistics_data_science_project/data/supply_chain_logistics_problem.xlsx'
df = pd.read_excel(file_path)

# Feature Engineering (example: convert categorical to numerical)
df = pd.get_dummies(df, columns=[
    'Origin Port', 'Carrier', 'Service Level', 'Customer', 'Plant Code', 'Destination Port'
], drop_first=True)

# Drop columns that are not useful for prediction or are target/leakage
df = df.drop(columns=['Order ID', 'Order Date', 'Product ID'])

# Define features (X) and target (y)
X = df.drop(columns=['Ship Late Day count'])
y = df['Ship Late Day count']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse**0.5
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae:.2f}')
print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'Root Mean Squared Error (RMSE): {rmse:.2f}')
print(f'R-squared (R2): {r2:.2f}')

# Save model evaluation results to a file
with open('/home/ubuntu/logistics_data_science_project/reports/model_evaluation.txt', 'w') as f:
    f.write(f'Mean Absolute Error (MAE): {mae:.2f}\n')
    f.write(f'Mean Squared Error (MSE): {mse:.2f}\n')
    f.write(f'Root Mean Squared Error (RMSE): {rmse:.2f}\n')
    f.write(f'R-squared (R2): {r2:.2f}\n')


