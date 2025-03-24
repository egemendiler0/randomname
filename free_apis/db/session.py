import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()

# Connection URL for SQLAlchemy (using pyodbc driver)
SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")

# Creating the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,  # This will log all SQL queries
)

# Creating a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_sql_server_version(db):
    result = db.execute("SELECT @@VERSION")
    return result.fetchone()
