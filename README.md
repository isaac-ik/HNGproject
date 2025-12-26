# HNGproject

# Flask API - Developer Information Endpoint

A simple REST API built with Flask that returns developer information along with current UTC time and day of the week.

## Description

This API provides a single endpoint that accepts query parameters and returns structured JSON data including the current day, UTC timestamp, and GitHub repository information. It's designed to demonstrate basic Flask API development and datetime handling.

## Features

- GET endpoint that accepts query parameters
- Real-time UTC time generation
- Current day of the week retrieval
- JSON response format
- Timezone-aware datetime handling

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/isaac-ik/HNGproject.git
   cd HNGproject
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install flask pytz
   ```

   Or if you have a `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

Start the Flask server:

```bash
python app.py
```

The server will start on `http://0.0.0.0:5000/`

### API Endpoint

**Endpoint:** `/api`  
**Method:** `GET`  
**Parameters:**
- `slack_name` (string, required) - Your Slack username
- `track` (string, required) - Your track (e.g., backend, frontend)

### Example Request

```bash
curl "http://localhost:5000/api?slack_name=john_doe&track=backend"
```

Or open in your browser:
```
http://localhost:5000/api?slack_name=john_doe&track=backend
```

### Example Response

```json
{
  "slack_name": "john_doe",
  "current_day": "Friday",
  "utc_time": "2025-12-26T15:30:45Z",
  "track": "backend",
  "github_file_url": "https://github.com/isaac-ik/HNGproject/file.py",
  "github_repo_url": "https://github.com/isaac-ik/HNGproject",
  "status_code": 200
}
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `slack_name` | string | The Slack username passed as query parameter |
| `current_day` | string | Current day of the week in UTC |
| `utc_time` | string | Current UTC time in ISO 8601 format |
| `track` | string | The track passed as query parameter |
| `github_file_url` | string | URL to the specific file in the repository |
| `github_repo_url` | string | URL to the GitHub repository |
| `status_code` | integer | HTTP status code (200 for success) |

## Technologies Used

- **Flask** - Web framework for Python
- **pytz** - Timezone handling library
- **datetime** - Python's built-in datetime module

## Project Structure

```
HNGproject/
│
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Configuration

You can modify the host and port in the `app.py` file:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Change as needed
```

## Error Handling

Currently, the API returns the response even if query parameters are missing. Consider adding validation for production use:

```python
if not slack_name or not track:
    return jsonify({"error": "Missing required parameters"}), 400
```

## Development

To run in debug mode (auto-reload on code changes):

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

**Note:** Never use `debug=True` in production!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Isaac IK**  
GitHub: [@isaac-ik](https://github.com/isaac-ik)
