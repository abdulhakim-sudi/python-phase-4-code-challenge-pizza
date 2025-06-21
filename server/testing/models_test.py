import pytest
from server.app import create_app, db
from server.models import Restaurant, Pizza, RestaurantPizza

@pytest.fixture
def app():
    test_config = {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "TESTING": True
    }
    return create_app(test_config)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def setup_db(app):
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()

def test_model_creation(client):
    from server.models import Restaurant, Pizza, RestaurantPizza

    new_restaurant = Restaurant(name="Dominos", address="123 Street")
    new_pizza = Pizza(name="Cheese", ingredients="Cheese, Tomato")
    new_rp = RestaurantPizza(price=9.99, restaurant=new_restaurant, pizza=new_pizza)

    db.session.add_all([new_restaurant, new_pizza, new_rp])
    db.session.commit()

    assert Restaurant.query.count() == 1
    assert Pizza.query.count() == 1
    assert RestaurantPizza.query.count() == 1
