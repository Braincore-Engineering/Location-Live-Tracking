from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Tracker(Base):
    __tablename__ = 'trackers'

    id = Column(Integer, primary_key=True)
    tracker_id = Column(Integer, unique=True, nullable=False)
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)

# Note: You may want to include the following code in a separate script to create the database tables
if __name__ == "__main__":
    engine = create_engine('sqlite:///data.db')
    Base.metadata.create_all(engine)
