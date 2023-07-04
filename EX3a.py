from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load iris dataset
data = load_iris()
X, y = data.data, data.target

# Split dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Gaussian Naive Bayes model
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Predict labels for test set
y_pred = gnb.predict(X_test)

# Calculate accuracy of predictions
accuracy = accuracy_score(y_test, y_pred)

# Print results
print("Accuracy:", accuracy)

