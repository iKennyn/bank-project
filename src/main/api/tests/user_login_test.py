from main.api.models.create_user_request import UserRole
from main.api.models.login_user_request import LoginUserRequest


class TestUserLogin:
    def test_login_admin(self, api_manager):
        login_user_request = LoginUserRequest(username="admin", password="123456")
        response = api_manager.admin_steps.login_user(login_user_request)

        assert login_user_request.username == response.user.username
        assert response.user.role == UserRole.ROLE_ADMIN


    def test_login_user(self, api_manager, create_user):
        username = "ivan"
        password = "Pas!sw0rd"
        create_user(username, password, UserRole.ROLE_USER)

        login_user_request = LoginUserRequest(username=username,
                                              password=password)
        login_user_response = api_manager.user_steps.login_user(login_user_request)

        assert login_user_request.username == login_user_response.user.username
        assert login_user_response.user.role == UserRole.ROLE_USER
