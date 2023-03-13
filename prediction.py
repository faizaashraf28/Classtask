import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv("C:/Users/DELL/Downloads/Salary_Data.csv")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data["YearsExperience"], data["Salary"], test_size=0.2, random_state=42)

# Create a linear regression model and train it on the training data
model = LinearRegression()
model.fit(X_train.values.reshape(-1, 1), y_train)

# Use the trained model to make predictions on the testing data
y_pred = model.predict(X_test.values.reshape(-1, 1))
