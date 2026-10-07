from enum import Enum
from main.api.models.base_model import BaseModel


class UserRole(str, Enum):
    ROLE_USER = "ROLE_USER"
    ROLE_ADMIN = "ROLE_ADMIN"

class CreateUserRequest(BaseModel):
    username: str
    password: str
    role: UserRole
