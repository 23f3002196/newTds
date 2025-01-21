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
    
    # Find the marks for the requested names
    marks = []
    for name in names:
        # Find student by name in the list of dictionaries
        student = next((student for student in data if student["name"] == name), None)
        marks.append(student["marks"] if student else None)  # Append marks or None if not found

    return jsonify({"marks": marks})  # Return marks in JSON format

if __name__ == "__main__":
    app.run(debug=True)
