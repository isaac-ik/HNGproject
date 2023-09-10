from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.now(pytz.utc).strftime('%A')

    # Get current UTC time with validation of +/-2 minutes
    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct GitHub URLs based on your project
    github_file_url = "https://github.com/isaac-ik/HNGproject/file.py"
    github_repo_url = "https://github.com/isaac-ik/HNGproject"

    # Prepare the JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Change the host and port as needed
