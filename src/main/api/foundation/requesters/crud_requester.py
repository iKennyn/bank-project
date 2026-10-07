from typing import Optional

import allure
import requests

from requests import Response

from main.api.configs.config import Config
from main.api.foundation.http_requester import HttpRequester
from main.api.foundation.requesters.logger_decorator import log_request_response
from main.api.models.base_model import BaseModel

# шлет хттп запрос, логирует в аллюр
class CrudRequester(HttpRequester):

    @log_request_response("POST")
    def post(self, model: Optional[BaseModel]) -> Response:
        body = model.model_dump() if model is not None else ""

        with allure.step(f"POST {Config.fetch("backendUrl")}{self.endpoint.value.url}"):
            allure.attach(str(body), "Request body", allure.attachment_type.JSON)
        response = requests.post(
            url=f"{Config.fetch("backendUrl")}{self.endpoint.value.url}",
            headers=self.request_spec,
            json=body
        )
        allure.attach(
            response.text,
            "Response body",
            allure.attachment_type.JSON
        )
        self.response_spec(response)
        return response


    def delete(self, user_id: int) -> Response:
        url = f"{Config.fetch('backendUrl')}{self.endpoint.value.url.format(user_id=user_id)}"

        with allure.step(f"DELETE {url}"):
            response = requests.delete(
                url=url,
                headers=self.request_spec,
            )
            allure.attach(
                response.text,
                "Response body",
                allure.attachment_type.JSON
            )
        self.response_spec(response)
        return response
