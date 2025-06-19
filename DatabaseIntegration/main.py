# from database import db_session, db_engine
# from models import Customer, Base
    
# def main():
#     Base.metadata.create_all(db_engine)
#     customer = Customer(name="Kukil", email="kukil@gmail.com", balance=100)
    
#     with db_session() as Session:
#         Session.add(customer)
#         Session.commit()
#         print(Session.query(Customer).all())
        
        
# if __name__ == "__main__":
#     main()
