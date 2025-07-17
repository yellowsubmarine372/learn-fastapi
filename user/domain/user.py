from dataclasses import dataclass
from datetime import datetime
from typing import Any

from utils.db_utils import row_to_dict

@dataclass
class Profile:
    name: str
    email: str
    memo: str | None = None

@dataclass
class User:
    id: int
    profile: Profile
    password: str
    created_at: datetime
    updated_at: datetime
    
    @staticmethod
    def from_row(row: Any) -> "User":
        data = row_to_dict(row)
        return User(
            id=data["id"],
            profile=Profile(
                name=data["name"],
                email=data["email"],
                memo=data.get("memo")
            ),
            password=data["password"],
            created_at=data["created_at"],
            updated_at=data["updated_at"]
        )