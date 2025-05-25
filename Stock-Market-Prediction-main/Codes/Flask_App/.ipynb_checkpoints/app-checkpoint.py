"""
Flask Web Application for Predicting Stock Close Prices

This application loads pre-trained machine learning models from a specified directory
and uses them to predict stock close prices based on input features such as open price,
high price, low price, and volume. Users can select a company from a predefined list,
enter stock details, and get a prediction for the closing price.

The application consists of:
- A home route ("/") that renders the index page and accepts form submissions.
- A predict route ("/predict") that returns a JSON response with the predicted close price.
- Model loading logic to read and store machine learning models in memory.
"""

from flask import Flask, render_template, request, jsonify
import pickle  # For loading saved models
import os  # For directory and path handling
import numpy as np  # For array handling

app = Flask(__name__)

# Define the base directory and model directory paths
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
model_dir = os.path.join(base_dir, "Historical_Data_Analysis/Models/pkl_models")

# Mapping of company names to their ticker symbols
ticker_mapping = {
    "Apple": "AAPL",
    "Amazon": "AMZN",
    "Meta Platforms": "META",
    "Google": "GOOG",
    "Microsoft": "MSFT",
    "Netflix": "NFLX",
    "Nvidia": "NVDA",
    "Tata Consultancy Services (TCS)": "TCS",
}

# Dictionary to hold loaded models
models = {}

# Load all models from the specified directory
try:
    print("Loading models...")
    for filename in os.listdir(model_dir):
        if filename.endswith(
            "_Ensemble_Model.pkl"
        ):  # Load only models with this naming convention
            model_name = filename.split("_")[
                0
            ].lower()  # Extract the ticker symbol as the model name
            model_path = os.path.join(model_dir, filename)

            # Load the model using pickle and store it in the models dictionary
            with open(model_path, "rb") as model_file:
                models[model_name] = pickle.load(model_file)

            print(f"Model '{model_name.upper()}' loaded from {model_path}")
    print("All models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")

# Print loaded models' keys for debugging purposes
print(models.keys())


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Home route that renders the index page and handles form submissions for stock prediction.
    """
    selected_company = None
    close_value = None

    # Handle POST request (form submission)
    if request.method == "POST":
        selected_company = request.form.get()  # Get the selected company from the form
        print(f"Selected company (backend): {selected_company}")  # Debugging line

        if selected_company in models:
            try:
                # Retrieve the model for the selected company
                model = models[selected_company]

                # Get input values from the form and convert them to float
                open_price = float(request.form.get("open"))
                high_price = float(request.form.get("high"))
                low_price = float(request.form.get("low"))
                volume = float(request.form.get("volume"))

                # Prepare input data as a NumPy array
                input_data = np.array([[open_price, high_price, low_price, volume]])

                # Predict the close value using the model
                close_value = model.predict(input_data)[0]
            except ValueError:
                close_value = "Invalid input"  # Handle invalid input data
            except Exception as e:
                close_value = str(e)  # Handle unexpected errors
        else:
            close_value = "Model not found"  # Handle missing model

    # Render the index template with necessary data
    return render_template(
        "index.html",
        ticker_mapping=ticker_mapping,
        selected_company=selected_company,
        close_value=close_value,
    )


@app.route("/predict", methods=["POST"])
def predict():
    """
    Route for handling AJAX requests for stock predictions. Returns a JSON response.
    """
    selected_company = ticker_mapping[
        request.form.get("company").title()
    ]  # Map input to ticker
    print(
        f"Selected company for prediction (backend): {selected_company}"
    )  # Debugging line

    # Adjust the selected company to match model keys (lowercase)
    selected_company = selected_company.lower()

    if selected_company in models:
        try:
            # Retrieve the model for the selected company
            model = models[selected_company]

            # Get input values from the form and convert them to float
            open_price = float(request.form.get("open"))
            high_price = float(request.form.get("high"))
            low_price = float(request.form.get("low"))
            volume = float(request.form.get("volume"))

            # Prepare input data as a NumPy array
            input_data = np.array([[open_price, high_price, low_price, volume]])

            # Predict the close value using the model
            predicted_close = model.predict(input_data)[0]

            # Return the predicted value as JSON
            return jsonify(
                {
                    "success": True,
                    "predicted_close": predicted_close,
                    "company": selected_company.capitalize(),
                }
            )
        except ValueError:
            return jsonify(
                {"success": False, "error": "Invalid input"}
            )  # Handle input errors
        except Exception as e:
            return jsonify({"success": False})  # Handle unexpected errors
    else:
        return jsonify(
            {"success": False, "error": "Model not found"}
        )  # Handle missing model


# Run the app in debug mode for development
if __name__ == "__main__":
    app.run()
