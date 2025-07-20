import pytest
from app.schemas import ReturnUser
from jose import jwt
from app.config import settings

def test_create_user(client):
    res = client.post('/user/', json={"email": "hope1@gmail.com", "password":"123", "phone_number":"1232qw12"})
    user_data = ReturnUser(**res.json())
    assert res.status_code == 201
    
    
def test_login_user(client, user_data):
    res = client.post('/login', data={"username":user_data["email"], "password":user_data["password"]})
    data = res.json()
    payload = jwt.decode(data["access_token"], settings.SECRET_KEY, settings.ALGORITHM)
    id = payload.get("user_id")
    email = payload.get("user_email")
    assert res.status_code == 200
    assert id == user_data["id"]
    assert email == user_data["email"]
    assert data["token_type"] == "bearer"
    