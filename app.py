# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

@app.route("/news", methods=["GET"])
def get_news_by_city():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City not specified"}), 400

    csv_path = os.path.join(os.path.dirname(__file__), "nature_news_india.csv")
    if not os.path.exists(csv_path):
        return jsonify({"error": "News data not found"}), 404

    df = pd.read_csv(csv_path)
    filtered = df[df["City"].str.lower() == city.lower()]
    return jsonify(filtered.to_dict(orient="records"))

if __name__ == "__main__":
    # Comment out the Flask development server for Gunicorn
    # app.run(debug=True) 
    pass

