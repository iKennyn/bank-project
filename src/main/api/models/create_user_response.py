from main.api.models.base_model import BaseModel


class CreateUserResponse(BaseModel):
    id: int
    username: str
    role: str