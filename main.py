from flask import Flask, request, jsonify
from cleantext import preprocess_text
from train_categorizer import categorize_complaint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/categorize', methods=['POST'])
def categorize():
    data = request.json
    sample_text = data.get('text', '')
    clean_text = preprocess_text(sample_text)
    category, sub_category = categorize_complaint(clean_text)
    return jsonify({'category': category, 'subCategory': sub_category})

if __name__ == '__main__':
    app.run(debug=True)
