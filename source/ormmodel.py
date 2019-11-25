from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, ForeignKey, String, Time
from sqlalchemy.orm import relationship

from source.db import PostgresDb

Base = declarative_base()

class ormPlace(Base):
    __tablename__ = 'place'

    place_name = Column(String(40), primary_key=True)
    place_site = Column(String(40), nullable=False)
    type_of_service = Column(String(40), nullable=False)
    #client = relationship("ormClient", back_populates="place")
    #queues = relationship("ormQueue", back_populates="place")

class ormClient(Base):
    __tablename__ = 'client'

    client_fullname = Column(String(40), nullable=False)
    client_documents = Column(String(40), primary_key=True)
    place_name = Column (String (40), ForeignKey('place.place_name'))
    date = Column(Date, ForeignKey('schedule.date'))
    #places = relationship("ormPlace", back_populates="client")
    #schedule = relationship("ormSchedule", back_populates="client")

class ormQueue(Base):
    __tablename__ = 'queue'

    date = Column(Date, ForeignKey('schedule.date'))
    place_name = Column(String(40), ForeignKey('place.place_name'))
    queue_name = Column(String(40), primary_key=True)
    queue_number = Column(Integer, nullable=False)
    number_of_people = Column(Integer, nullable=False)
    waiting_time = Column(Time, nullable=False)
    #place = relationship("ormPlace", back_populates="queue")
    #schedule_fk = relationship("ormSchedule", back_populates="queue")


class ormSchedule(Base):
    __tablename__ = 'schedule'

    date = Column (Date, primary_key=True)
    time_in_queue = Column(Time, nullable=False)
    push_notification = Column(String(40), nullable=False)
    #client_fk = relationship("ormClient", uselist=False, back_populates="schedule")
    #queue_fk = relationship("ormQueue", back_populates="schedule")



db = PostgresDb()

Base.metadata.create_all(db.sqlalchemy_engine)