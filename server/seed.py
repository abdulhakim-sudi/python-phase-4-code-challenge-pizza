from server.app import app, db
from server.models import Restaurant, Pizza, RestaurantPizza

with app.app_context():
    print("Seeding data...")

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    r1 = Restaurant(name="Mama's Pizza", address="123 Pizza Street")
    r2 = Restaurant(name="Slice Heaven", address="456 Cheesy Blvd")

    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=12, pizza_id=p2.id, restaurant_id=r1.id)
    rp3 = RestaurantPizza(price=11, pizza_id=p2.id, restaurant_id=r2.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("✅ Seeded successfully!")
