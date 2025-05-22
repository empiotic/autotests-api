import httpx

# GET запрос на получение токена
data = {
    "email": "user@example.com",
    "password": "string"
}

response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=data)

print(response.status_code)
response_json = response.json()
print(response.json())

access_token = response_json.get('token', {}).get('accessToken')

# POST запрос на получение данных пользователя

headers = {"Authorization": f"Bearer {access_token}"}
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(response.status_code)
print(response.json())