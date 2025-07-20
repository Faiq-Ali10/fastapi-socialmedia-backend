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
