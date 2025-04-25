from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)

# Allow CORS for local development from various localhost URLs
CORS(app, origins=["http://0.0.0.0:5500", "http://localhost:5500", "http://127.0.0.1:5500"])

@app.route("/news", methods=["GET"])
def get_news_by_city():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City not specified"}), 400

    # Path to the CSV file containing the news data
    csv_path = os.path.join(os.path.dirname(__file__), "nature_news_india.csv")
    if not os.path.exists(csv_path):
        return jsonify({"error": "News data not found"}), 404

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Filter news by city (case-insensitive)
    filtered = df[df["City"].str.lower() == city.lower()]

    # Return the filtered news data as JSON
    return jsonify(filtered.to_dict(orient="records"))

if __name__ == "__main__":
    # Commented out to use Gunicorn or another WSGI server for production
    # app.run(debug=True)
    pass

