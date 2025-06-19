from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://kukil:Admin123@localhost:5432/db_integration"

db_engine = create_engine(DATABASE_URL)
db_session = sessionmaker(bind=db_engine)
