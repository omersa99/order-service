from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float, create_engine,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import current_app
import datetime


engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    stock_id = Column(Integer)
    type = Column(String)
    price = Column(Float)
    shares = Column(Integer)
    executed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)