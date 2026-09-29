from typing import Optional

import allure

from main.api.configs.config import Config
from main.api.foundation.http_requester import HttpRequester
from main.api.foundation.requesters.crud_requester import CrudRequester
from main.api.models.base_model import BaseModel


# валидирует ответ на запрос, использует пайдантик
class ValidateCrudRequester(HttpRequester):
    def __init__(self, request_spec, endpoint, response_spec):
        super().__init__(request_spec, endpoint, response_spec)
        self.crud_requester = CrudRequester(
            request_spec=request_spec,
            endpoint=endpoint,
            response_spec=response_spec
        )

    def post(self, model: Optional[BaseModel] = None):
        response = self.crud_requester.post(model)
        with allure.step(f"POST {Config.fetch("backendUrl")}{self.endpoint.value.url} and Validated Model"):
            allure.attach(f"Validated Model response: {self.endpoint.value.response_model.__name__}")
        self.response_spec(response)
        return self.endpoint.value.response_model.model_validate(response.json())
