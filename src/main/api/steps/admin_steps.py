from main.api.foundation.endpoint import Endpoint
from main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from main.api.models.login_user_request import LoginUserRequest
from main.api.specs.request_specs import RequestSpecs
from main.api.specs.response_specs import ResponseSpecs
from main.api.steps.base_steps import BaseSteps


class AdminSteps(BaseSteps):
    def login_user(self, login_user_request: LoginUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.unauth_headers(),
            Endpoint.LOGIN_USER,
            ResponseSpecs.request_ok()
        ).post(login_user_request)
        return response