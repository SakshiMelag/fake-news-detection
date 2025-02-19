from flask import Flask, request, jsonify
import joblib
from db import save_to_mongo
import os

app = Flask(__name__)

# Load both models and vectorizer
nb_model_path = os.path.join(os.path.dirname(__file__), "fake_news_nb_model.pkl")
rf_model_path = os.path.join(os.path.dirname(__file__), "fake_news_rf_model.pkl")
vectorizer_path = os.path.join(os.path.dirname(__file__), "tfidf_vectorizer.pkl")

nb_model = joblib.load(nb_model_path)  # Naïve Bayes
rf_model = joblib.load(rf_model_path)  # Random Forest
vectorizer = joblib.load(vectorizer_path)

@app.route('/predict', methods=['POST'])
def predict():
    """Receive text from frontend, predict using selected model (NB or RF)."""
    data = request.get_json()
    text = data.get("text", "")
    model_type = data.get("model", "nb")  # Default model is Naïve Bayes

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Vectorize the input text
    text_vectorized = vectorizer.transform([text])

    # Select model based on user choice
    if model_type == "rf":
        prediction = rf_model.predict(text_vectorized)[0]
    else:  # Default to Naïve Bayes
        prediction = nb_model.predict(text_vectorized)[0]

    # Convert prediction to readable format
    result = "Fake" if prediction == 1 else "Real"
    
    save_to_mongo(text, result, model_type)
     # Save prediction to the database (using the get_db function from db.py)
    #db = save_to_mongo()  # Get the database connection
   # collection = db['predictions']  # You can change this collection name as needed
    #collection.insert_one({"text": text, "prediction": result, "model_used": model_type})  # Save prediction

    return jsonify({"prediction": result, "model_used": model_type})

if __name__ == "__main__":
    app.run(debug=True)
