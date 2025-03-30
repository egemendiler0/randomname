from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql import func
from db.session import Base


class ExampleTable(Base):
    __tablename__ = "example_table"

    # Option 1: Use a fixed-length string (recommended)
    name = Column(String(255), primary_key=True, index=True)

    # OR Option 2: Use an auto-incrementing integer ID (alternative)
    # id = Column(Integer, primary_key=True, autoincrement=True)
    # name = Column(String(255), index=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(String(255))  # Also fixed length


def get_metadata():
    return Base.metadata