from main.api.models.create_user_request import CreateUserRequest
from main.api.models.user_role import UserRole


class TestUserCreate:
    def test_create_admin(self, api_manager):
        create_user_request = CreateUserRequest(username="ivan", password="Pas!sw0rd", role=UserRole.ROLE_USER)
        response = api_manager.user_steps.create_user(create_user_request)

        assert response.id
        assert create_user_request.username == response.username
        assert response.role == create_user_request.role
