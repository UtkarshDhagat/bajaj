import os
from dataclasses import dataclass

# Optional: load .env if present (local dev convenience)
try:
    from dotenv import load_dotenv
    load_dotenv()  # no-op on Vercel (envs come from dashboard)
except Exception:
    pass

@dataclass(frozen=True)
class Settings:
    # NOTE: full_name must be lowercase per the assignment
    full_name: str = os.getenv("FULL_NAME", "john_doe").lower()
    dob_ddmmyyyy: str = os.getenv("DOB_DDMMYYYY", "17091999")
    email: str = os.getenv("EMAIL", "john@xyz.com")
    roll_number: str = os.getenv("ROLL_NUMBER", "ABCD123")

settings = Settings()
