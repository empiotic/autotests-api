import httpx

from tools.fakers import get_random_email

# Запрос на создание пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
print(create_user_response.status_code)
print(create_user_response.json())

# Запрос на авторизацию пользователя
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(login_response.status_code)
print('Login data:', login_response_data)

# Запрос на обновление пользователя
access_token = login_response_data['token']['accessToken']
user_id = create_user_response.json()['user']['id']
headers = {"Authorization": f"Bearer {access_token}"}
update_user_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}


update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}", json=update_user_payload, headers=headers)
update_user_data = update_user_response.json()
print(update_user_response.status_code)
print('Updated user data:', update_user_data)
