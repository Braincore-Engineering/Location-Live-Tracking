# meant to be runned only once to create the database
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///data.db')

class Tracker(Base):
    __tablename__ = 'trackers'

    id = Column(Integer, primary_key=True)
    tracker_id = Column(Integer, unique=True, nullable=False)
    lat = Column(Float, unique=True, nullable=False)
    long = Column(Float, unique=True, nullable=False)
    # created_at = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example: Inserting a new tracker into the database
new_tracker = Tracker(tracker_id=1, lat=-6.1228, long=106.7890)
new_tracker = Tracker(tracker_id=2, lat=-6.1902, long=106.8404)

session.add(new_tracker)
session.commit()

session.close()