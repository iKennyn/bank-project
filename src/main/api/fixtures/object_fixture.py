from typing import Any, List
from main.api.foundation.endpoint import Endpoint
from main.api.foundation.requesters.crud_requester import CrudRequester
from main.api.models.create_user_request import CreateUserRequest
from main.api.specs.request_specs import RequestSpecs
from main.api.specs.response_specs import ResponseSpecs


import pytest


@pytest.fixture
def created_obj():
    objects: List[Any] = []
    yield objects
    clean_user(objects)

# Создание пользователя для запросов
@pytest.fixture
def create_user(api_manager):
    def _create(username, password, role):
        request = CreateUserRequest(username=username, password=password, role=role)
        return api_manager.user_steps.create_user(request)
    return _create

# Удаление пользователя после выполнения теста
def clean_user(objects: List[Any]):
    for user_id in objects:
        CrudRequester(
            request_spec=RequestSpecs.admin_auth_header(),
            endpoint=Endpoint.DELETE_USER,
            response_spec=ResponseSpecs.request_ok(),
        ).delete(user_id)
