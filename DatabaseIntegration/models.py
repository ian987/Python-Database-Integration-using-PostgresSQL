from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from database import db_session

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    name: Mapped[str]
    email: Mapped[str]
    balance: Mapped[int]
    
    def __repr__(self):
        return(f'CustomerModel(id={self.id}, name={self.name}, email={self.email}, balance={self.balance})')

customers = [
    Customer(name="Kukil", email="kukil@gmail.com", balance=200)
]   
    
def create_customers():
    with db_session() as session:
        for cus in customers:
            session.add(cus)
        session.commit()
        
# create_customers()
        
# with db_session() as session:
#     customer_records = session.query(Customer).all()
#     for eachCus in customer_records:
#         print(eachCus)
        
        
def transfer_amount(db, sender_id, receiver_id, amount: int):
    try:
        sender = db.query(Customer).filter(Customer.id == sender_id).first()
        receiver = db.query(Customer).filter(Customer.id == receiver_id).first()
        
        if int(sender.balance) < amount:
            raise Exception("Insufficient balance")
        
        sender.balance = int(sender.balance) - amount
        receiver.balance = int(receiver.balance) + amount 
        
        db.commit()
    except:
        db.rollback()
        raise Exception("Something went wrong!!!")
    
transfer_amount(db_session(), 2, 1, 50)
    
