from flask import Flask, render_template, request
from classify import predict_class
import json  # Add import statement for the json module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    data = request.form.to_dict()
    input_json = json.dumps(data)  # Convert data to JSON string
    classification_result = predict_class(input_json)
    if classification_result:
        return render_template('result.html', result=classification_result)
    else:
        return "Error processing classification."

if __name__ == '__main__':
    app.run(debug=True)
