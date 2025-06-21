from server.app import db

class Restaurant(db.Model):
    __tablename__ = "restaurants"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String)
    restaurant_pizzas = db.relationship("RestaurantPizza", backref="restaurant")

class Pizza(db.Model):
    __tablename__ = "pizzas"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    restaurant_pizzas = db.relationship("RestaurantPizza", backref="pizza")

class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizzas"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))
