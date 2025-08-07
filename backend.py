from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# File to store the reports
REPORTS_FILE = 'reports.json'

# Ensure the file exists
if not os.path.exists(REPORTS_FILE):
    with open(REPORTS_FILE, 'w') as f:
        json.dump([], f)

@app.route('/submit_report', methods=['POST'])
def submit_report():
    try:
        # Parse the incoming JSON data
        data = request.get_json()

        # Validate the required fields
        if not data or not all(key in data for key in ('category', 'description', 'location')):
            return jsonify({"success": False, "message": "All fields are required."}), 400

        # Load existing reports
        with open(REPORTS_FILE, 'r') as f:
            reports = json.load(f)

        # Add the new report
        reports.append(data)

        # Save the updated reports back to the file
        with open(REPORTS_FILE, 'w') as f:
            json.dump(reports, f, indent=4)

        return jsonify({"success": True, "message": "Report submitted successfully."}), 201

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": "An error occurred while processing the request."}), 500

@app.route('/get_reports', methods=['GET'])
def get_reports():
    try:
        # Load existing reports
        with open(REPORTS_FILE, 'r') as f:
            reports = json.load(f)

        return jsonify(reports), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": "An error occurred while fetching reports."}), 500

if __name__ == '__main__':
    app.run(debug=True)
