from typing import List, Any, Optional
from pydantic import BaseModel, Field

class BFHLRequest(BaseModel):
    data: List[Any] = Field(..., description="Array of items (strings/numbers/symbols)")

class BFHLBase(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str

class BFHLResponse(BFHLBase):
    odd_numbers: List[str]
    even_numbers: List[str]
    alphabets: List[str]
    special_characters: List[str]
    sum: str
    concat_string: str

class BFHLError(BFHLBase):
    error: Optional[str] = None
