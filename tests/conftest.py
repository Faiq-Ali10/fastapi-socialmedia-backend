from fastapi.testclient import TestClient
from app.main import app, models
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.config import settings
from app.database import get_db
import pytest
from app.oauth2 import create_access_token

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME_Test}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(bind=engine)
        
@pytest.fixture
def session():
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
            
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    
@pytest.fixture
def user_data(client):
    res = client.post('/user/', json={"email": "test@gmail.com", "password":"123", "phone_number":"123"})
    user_data = res.json()
    user_data["password"] = "123"
    assert res.status_code == 201
    return user_data

@pytest.fixture
def token(user_data):
    return create_access_token({"user_id" : user_data["id"], "user_email" : user_data["email"]})

@pytest.fixture
def authorized_user(client, token):
    client.headers = {**client.headers, "Authorization" : f"Bearer {token}"}
    return client
    
@pytest.fixture
def test_posts(authorized_user):
    authorized_user.post("/post/", json={"title":"test1", "content":"test"})
    authorized_user.post("/post/", json={"title":"test2", "content":"test"})
    authorized_user.post("/post/", json={"title":"test2", "content":"test"})
  
#Vote  
@pytest.fixture
def create_up_vote(authorized_user, test_posts):
    authorized_user.post("/vote/", json={"post_id":1, "direction":1})
    
@pytest.fixture
def create_down_vote(authorized_user, test_posts):
    authorized_user.post("/vote/", json={"post_id":1, "direction":-1})