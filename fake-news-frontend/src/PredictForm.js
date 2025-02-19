import React, { useState } from "react";
import axios from "axios";  // Import axios for making API requests

const PredictForm = () => {
  const [text, setText] = useState("");  // State to store input text
  const [prediction, setPrediction] = useState(null);  // State to store the prediction result
  const [model, setModel] = useState("nb");  // Default model is Naïve Bayes, can switch to "rf" for Random Forest

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();  // Prevent the default form submission

    try {
      // Send POST request to Flask API with the text and selected model
      const response = await axios.post("http://127.0.0.1:5000/predict", {
        text: text,
        model: model,  // Send the selected model type ("nb" or "rf")
      });

      // Store the response (prediction) in the state
      setPrediction(response.data);
    } catch (error) {
      console.error("Error making prediction:", error);
      alert("An error occurred while fetching the prediction.");
    }
  };

  return (
    <div>
      <h1>Fake News Detection</h1>
      <form onSubmit={handleSubmit}>
        {/* Text input */}
        <div>
          <label>Enter News Text:</label>
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}  // Update the text state as user types
            rows="4"
            cols="50"
            required
          />
        </div>

        {/* Model selection */}
        <div>
          <label>Select Model:</label>
          <select
            onChange={(e) => setModel(e.target.value)}  // Update model state on selection change
            value={model}
          >
            <option value="nb">Naïve Bayes</option>
            <option value="rf">Random Forest</option>
          </select>
        </div>

        {/* Submit button */}
        <button type="submit">Predict</button>
      </form>

      {/* Display the prediction result */}
      {prediction && (
        <div>
          <h3>Prediction: {prediction.prediction}</h3>
          <p>Model used: {prediction.model_used}</p>
        </div>
      )}
    </div>
  );
};

export default PredictForm;