from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    is_admin: bool
    is_active: bool
    account_age: int
    is_banned: bool
    country: str
    credit_score: int
    has_manual_override: bool
