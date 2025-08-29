BFHL — FastAPI on Vercel (Python, Serverless)

Build-and-host solution for the VIT BFHL assignment.
Production-ready FastAPI (ASGI) app deployed as a Vercel Python Serverless Function with clean separation of logic, schemas, and config.

✨ Features

Public route: POST /bfhl (via vercel.json rewrite)

Strict schema with Pydantic

Deterministic output per assignment:

user_id = {full_name_ddmmyyyy} (lowercase full name)

Numbers returned as strings

Split into odd_numbers, even_numbers, alphabets (uppercased), special_characters

sum as string

concat_string: all letters from the input, reversed, alternating caps starting with Upper

Graceful errors with is_success=false but still returning identity fields

CORS enabled for quick browser testing (tighten later)

Unit-testable core logic

🧱 Tech Stack

Python 3.12 (Vercel runtime)

FastAPI (+ Pydantic v2)

Serverless via Vercel Functions (no uvicorn needed in prod)

Optional local dev via uvicorn --reload

📁 Project Structure
.
├─ api/
│  └─ bfhl.py            # ASGI entrypoint; Vercel loads app from here
├─ bfhl/
│  ├─ __init__.py
│  ├─ config.py          # env-driven identity settings
│  ├─ logic.py           # pure functions (classification, concat logic)
│  └─ schemas.py         # Pydantic request/response models
├─ tests/
│  └─ test_logic.py      # sanity tests for examples
├─ .env                  # local-only (FULL_NAME, DOB_DDMMYYYY, etc.)
├─ requirements.txt
├─ vercel.json           # /bfhl rewrite + runtime settings
└─ .vscode/
   └─ launch.json        # F5 debug: uvicorn api.bfhl:app --reload

🔌 API
POST /bfhl

Request body

{
  "data": ["a","1","334","4","R","$"]
}


Response (example)

{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334","4"],
  "alphabets": ["A","R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}


The app also exposes GET / locally (and /api/bfhl on Vercel) for a simple health check returning {"operation_code": 1}.

🔐 Environment Variables

Set these in Vercel → Project → Settings → Environment Variables, and locally in .env:

FULL_NAME → e.g., john_doe (lowercase, required by spec)

DOB_DDMMYYYY → e.g., 17091999

EMAIL → your email

ROLL_NUMBER → your roll number

▶️ Local Development

Python venv & install:

python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt


Create .env:

FULL_NAME=john_doe
DOB_DDMMYYYY=17091999
EMAIL=john@xyz.com
ROLL_NUMBER=ABCD123


Run (choose one):

CLI:

uvicorn api.bfhl:app --reload


VS Code: open the folder → Run and Debug → FastAPI (uvicorn) — local → F5.

Test:

Swagger UI: http://127.0.0.1:8000/docs

cURL:

curl -s -X POST "http://127.0.0.1:8000/" \
  -H "content-type: application/json" \
  -d '{"data":["a","1","334","4","R","$"]}'


Locally the POST path is / because Vercel’s rewrite is applied only in production (/bfhl → /api/bfhl).