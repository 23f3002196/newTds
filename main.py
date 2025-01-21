from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# Load student marks from the JSON file
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

@app.route("/api", methods=["GET"])
def get_marks():
    # Get the list of names from the query parameters
    names = request.args.getlist("name")
    # Retrieve marks for the given names
    marks = [data["students"].get(name, None) for name in names]
    return jsonify({"marks": marks})  # Return marks in JSON format

if __name__ == "__main__":
    app.run()
