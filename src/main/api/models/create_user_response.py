from main.api.models.base_model import BaseModel
from main.api.models.user_role import UserRole


class CreateUserResponse(BaseModel):
    id: int
    username: str
    role: UserRole