import pytest
from flaskr import create_app
from flaskr.extensions import db


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture(scope='function')
def session(db, request):
    session = db.create_scoped_session()
    db.session = session

    def teardown():
        session.remove()

    request.addfinalizer(teardown)
    return session

