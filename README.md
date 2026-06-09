# Spam-Classifier-API

A small Flask-based API for detecting spam messages. It provides a single `/predict` endpoint that accepts JSON with a `text` field and returns a spam prediction.

**Features**

- Simple REST endpoint: `POST /predict`
- Returns label and confidence score

**Requirements**

- Python 3.8+
- See `requirements.txt` for exact dependencies

**Setup**

1. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\\venv\\Scripts\\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

**Run**
Start the API (example):

```powershell
python main.py
```

**Usage**
Send a POST request with JSON:

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"Free prize! Click here"}'
```

Response example:

```json
{ "label": "spam", "score": 0.92 }
```

**Notes**

- Update `main.py` if your app serves a different route or port.
- If the project uses another framework or startup command, replace the `Run` section accordingly.
