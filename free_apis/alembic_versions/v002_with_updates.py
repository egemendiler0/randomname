from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from db.session import Base


class ExampleTable(Base):
    __tablename__ = "example_table"
    name = Column(String(255), primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(String(255))

    # New fields (not yet in database)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    updated_by = Column(String(255), nullable=True)


def get_metadata():
    return Base.metadata
