from ..utilities import db
from enum import Enum 
from datetime import datetime


class Sizes(Enum):
    SMALL = 'smaall'
    MEDIUM = 'medium'
    LARGE = 'large'
    EXTRA_LARGE = 'extra_large'

class OrderStatus(Enum):
    PENDING = 'pending'
    IN_TRANSIT = 'in-transit'
    DELIVERED = 'delivered'

class Order(db.Model):
    __tablename__='orders'
    # __table_args__ = {'schema': 'api'}
    
    id = db.Column(db.Integer(), primary_key=True)
    size = db.Column(db.Enum(Sizes), default=Sizes.SMALL)
    order_status = db.Column(db.Enum(OrderStatus), default=OrderStatus.PENDING)
    flavour = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer())
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    user = db.Column(db.Integer(), db.ForeignKey('users.id'))
    
    
    def __repr__(self):
        return f'<Order {self.id}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

