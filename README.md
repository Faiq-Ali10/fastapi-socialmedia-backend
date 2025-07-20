# FastAPI Social Media Backend 🚀

A **FastAPI-based backend** for a simple social media clone application. This project provides **RESTful APIs** to manage users, posts, votes (likes), and authentication with modern web development practices.

## ✨ Features

- 🔐 **User Authentication** - Registration and login with JWT tokens
- 🔒 **Security** - Password hashing with Bcrypt
- 📝 **Post Management** - Full CRUD operations for posts
- 👍 **Voting System** - Upvote/downvote functionality
- 🗄️ **PostgreSQL Database** - Reliable relational database
- 🐳 **Docker Support** - Containerized deployment
- 🔄 **CI/CD Pipeline** - Automated testing and deployment
- 🧪 **Testing Suite** - Comprehensive tests with Pytest

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Migrations**: Alembic
- **Testing**: Pytest
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **Authentication**: JWT (JSON Web Tokens)

## 📁 Project Structure

```text
.
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── oauth2.py
│   ├── routers/
│   │   ├── posts.py
│   │   ├── users.py
│   │   ├── auth.py
│   │   └── votes.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_posts.py
│   ├── test_users.py
│   └── test_votes.py
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
├── alembic.ini
├── .gitignore
└── README.md

---

## 🚀 Getting Started (Local)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-socialmedia-backend.git
cd fastapi-socialmedia-backend
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Setup environment variables
Create a .env file in the root directory and add the following:

env
Copy
Edit
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=your_db_name
DATABASE_USERNAME=your_db_user
DATABASE_PASSWORD=your_db_password
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

GitHub: https://github.com/Faiq-Ali10
LinkedIn: https://www.linkedin.com/in/faiq-ali-83462a255
