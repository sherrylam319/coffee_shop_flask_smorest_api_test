import pytest
from flask_jwt_extended import create_access_token
from app import create_app
from db import db


@pytest.fixture()
def app():
    app = create_app("sqlite://")
    app.config.update(
        {"TESTING": True}
    )
    with app.app_context():
        db.create_all()

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()







