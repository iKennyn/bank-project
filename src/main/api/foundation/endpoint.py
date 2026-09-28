from dataclasses import dataclass
from enum import Enum
from typing import Optional, Type

from main.api.models.base_model import BaseModel
from main.api.models.login_user_request import LoginUserRequest
from main.api.models.login_user_response import LoginUserResponse


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
