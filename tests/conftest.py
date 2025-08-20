import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.base import base as Base
from src.db.base import get_db
from app import app
from fastapi.testclient import TestClient
from src.db.models import Task

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаём таблицы
Base.metadata.create_all(bind=engine)

# Фикстура для тестового клиента
@pytest.fixture()
def client():
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
    app.dependency_overrides[get_db] = override_get_db  # get_db — твой dependency
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="session", autouse=True)
def create_test_tables():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield

@pytest.fixture()
def get_random_uuid_in_db():
    db = TestingSessionLocal()
    task = Task(
        title="Sample Task",
        description="This is a sample task.",
        status="create",
        user_id=1
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    yield task.id