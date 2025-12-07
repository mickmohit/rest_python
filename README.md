# REST Python Project

A Python REST API project created with FastAPI.

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

```
uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000
