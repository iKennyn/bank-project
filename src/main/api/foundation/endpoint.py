from dataclasses import dataclass
from enum import Enum
from typing import Optional, Type

from main.api.models.base_model import BaseModel
from main.api.models.login_user_request import LoginUserRequest
from main.api.models.login_user_response import LoginUserResponse
from main.api.models.create_user_request import CreateUserRequest
from main.api.models.create_user_response import CreateUserResponse
from main.api.models.delete_user_response import DeleteUserResponse

@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]

class Endpoint(Enum):

    LOGIN_USER = EndpointConfiguration(
        url="/auth/token/login",
        request_model=LoginUserRequest,
        response_model=LoginUserResponse
    )

    CREATE_USER = EndpointConfiguration(
        url="/admin/create",
        request_model=CreateUserRequest,
        response_model=CreateUserResponse
    )

    DELETE_USER = EndpointConfiguration(
        url='/admin/users/{user_id}',
        request_model = None,
        response_model= DeleteUserResponse
    )