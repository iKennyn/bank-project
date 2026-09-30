from main.api.foundation.endpoint import Endpoint
from main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from main.api.models.create_user_request import CreateUserRequest
from main.api.specs.request_specs import RequestSpecs
from main.api.specs.response_specs import ResponseSpecs
from main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_user(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.admin_auth_header(), # либо вынесу в request_specs.py
            Endpoint.CREATE_USER,
            ResponseSpecs.request_ok()
        ).post(create_user_request)
        self.created_obj.append(response.id)
        return response
