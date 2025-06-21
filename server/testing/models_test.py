from server.app import create_app, db
from server.models import Restaurant, Pizza, RestaurantPizza

def test_model_creation():
    app = create_app()
    with app.app_context():
        new_restaurant = Restaurant(name="Dominos", address="123 Street")
        new_pizza = Pizza(name="Cheese", ingredients="Cheese, Tomato")
        new_rp = RestaurantPizza(price=9.99, restaurant=new_restaurant, pizza=new_pizza)

        db.session.add_all([new_restaurant, new_pizza, new_rp])
        db.session.commit()

        assert Restaurant.query.count() == 1
        assert Pizza.query.count() == 1
        assert RestaurantPizza.query.count() == 1
