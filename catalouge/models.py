from enum import unique
from catalouge import app ,db 

class products(db.Model):

    _id = db.Column(db.Integer,primary_key=True)
    Product_id = db.Column(db.Interger, unique=True , nullable=False)
    product_name = db.Column(db.String(100),unique=True, nullable=False)
    Product_description = db.Column(db.String(100), unique=True, nullable=False)
