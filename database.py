from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCEHMY_DATABASE_URL = "mysql+mysqldb://root:1234@127.0.0.1/fastapi-ca"
engine = create_engine(SQLALCEHMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()