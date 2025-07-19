from dataclasses import dataclass
from datetime import datetime
from typing import Any

from utils.db_utils import row_to_dict

@dataclass
class User:
    id: int
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime
    memo: str | None = None

    @staticmethod
    def from_row(row: Any) -> "User":
        data = row_to_dict(row)
        return User(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            memo=data.get("memo"),
            password=data["password"],
            created_at=data["created_at"],
            updated_at=data["updated_at"]
        )