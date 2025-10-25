"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogpost" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Contactsubmission(BaseModel):
    """
    Contact submissions collection schema
    Collection name: "contactsubmission" (lowercase of class name)
    """
    name: str = Field(..., min_length=2, max_length=100, description="Full name")
    email: EmailStr = Field(..., description="Email address")
    subject: Optional[str] = Field(None, max_length=150, description="Subject line")
    message: str = Field(..., min_length=10, max_length=5000, description="Message body")
    consent: bool = Field(False, description="User consent to be contacted")
