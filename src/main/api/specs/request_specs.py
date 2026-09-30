import requests

from main.api.models.login_user_request import LoginUserRequest
from main.api.models.login_user_response import LoginUserResponse


class RequestSpecs:

    # метод, возвращающий общие хедеры, которые есть во всех запросах
    @staticmethod
    def base_headers():
        return {
            "Content-Type": "application/json",
            "accept": "application/json"
        }

    @staticmethod
    def auth_headers(username: str, password: str):
        request = LoginUserRequest(username=username, password=password)
        response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json=request.model_dump(),
            headers=RequestSpecs.base_headers()
        )
        if response.status_code == 200:
            response_data = LoginUserResponse(**response.json())
            token = response_data.token
            headers = RequestSpecs.base_headers()
            headers["Authorization"] = f"Bearer {token}"
            return headers
        raise Exception("Failed login")

    # Метод, что бы не передавать каждый раз креды админа
    @staticmethod
    def admin_auth_header():
        return RequestSpecs.auth_headers('admin', '123456')

    @staticmethod
    def unauth_headers():
        return RequestSpecs.base_headers()