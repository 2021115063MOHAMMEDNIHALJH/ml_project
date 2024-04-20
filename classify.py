import json
import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

def predict_class(input_json):
    try:
        input_data = json.loads(input_json)
    except json.JSONDecodeError:
        return "Invalid JSON format."
    
    required_fields = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth']
    for field in required_fields:
        if field not in input_data:
            return f"Missing required field: {field}"

    # Convert input features to numeric values
    try:
        features = [float(input_data[field]) for field in required_fields]
    except ValueError:
        return "Input features must be numeric."

    input_features = np.array(features).reshape(1, -1)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X, y)

    predicted_class = knn.predict(input_features)
    predicted_class_name = iris.target_names[predicted_class][0]
    return predicted_class_name
