import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv('alcohol_consumption_data.csv')  # Replace with your actual file path

# Inspect the first few rows of the dataset
print(data.head())

# Check for any missing values and general info
print(data.info())

# Drop any rows with missing values (or impute them if necessary)
data = data.dropna()

# Encode categorical variables (Gender as an example)
data['Gender'] = data['Gender'].map({'Male': 1, 'Female': 0})

# Select relevant features: Alcohol_Consumption, Gender, and Study_Hours
X = data[['Alcohol_Consumption', 'Gender', 'Study_Hours']]  # Independent variables
Y = data['GPA']  # Dependent variable: GPA

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Make predictions on the test set
Y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

# Output model coefficients and intercept
print(f'Mean Squared Error: {mse}')
print(f'R² Score: {r2}')
print(f'Intercept (β0): {model.intercept_}')
print(f'Coefficients (β1 for Alcohol_Consumption, β2 for Gender, β3 for Study_Hours): {model.coef_}')

# Visualizing the model’s predictions vs actual values
plt.figure(figsize=(8, 6))
plt.scatter(Y_test, Y_pred, color='blue', label='Predicted vs Actual', alpha=0.7)
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], color='red', linestyle='--', label='Perfect Prediction Line')
plt.title('Actual vs Predicted GPA')
plt.xlabel('Actual GPA')
plt.ylabel('Predicted GPA')
plt.legend()
plt.show()

# Plotting Alcohol Consumption vs GPA
plt.figure(figsize=(8, 6))
plt.scatter(data['Alcohol_Consumption'], data['GPA'], color='green', alpha=0.6)
plt.title('Alcohol Consumption vs GPA')
plt.xlabel('Alcohol Consumption')
plt.ylabel('GPA')
plt.show()

# Plotting Study Hours vs GPA
plt.figure(figsize=(8, 6))
plt.scatter(data['Study_Hours'], data['GPA'], color='purple', alpha=0.6)
plt.title('Study Hours vs GPA')
plt.xlabel('Study Hours')
plt.ylabel('GPA')
plt.show()

# Gender vs GPA (Box Plot)
plt.figure(figsize=(8, 6))
sns.boxplot(x='Gender', y='GPA', data=data, palette="Set2")
plt.title('Gender vs GPA')
plt.xlabel('Gender')
plt.ylabel('GPA')
plt.show()

# Feature importance (Coefficients of the linear regression model)
features = ['Alcohol_Consumption', 'Gender', 'Study_Hours']
coefficients = model.coef_

plt.figure(figsize=(8, 6))
plt.barh(features, coefficients, color='teal')
plt.title('Feature Importance (Coefficients)')
plt.xlabel('Coefficient Value')
plt.show()
