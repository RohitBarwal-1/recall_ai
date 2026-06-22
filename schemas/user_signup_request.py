import re
from pydantic import BaseModel, EmailStr, field_validator

PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$")

class UserSignupRequest(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str) -> str:
        if not PASSWORD_REGEX.match(password):
            raise ValueError(
                "Password must be at least 8 characters long and contain an uppercase letter, lowercase letter, digit, and special character"
            )
        return password