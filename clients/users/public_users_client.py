from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient

class UserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: UserRequestDict) -> Response:
        """
        Метод выполняет запрос на создание пользователя
        :param request: Словарь с email, password и ФИО пользователя
        :return: Ответ от сервера в виде httpx.Response
        """
        return self.post("/api/v1/users", json=request)