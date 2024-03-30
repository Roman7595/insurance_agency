from sqlalchemy import Column, ForeignKey, Integer, String, Date, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:1111@localhost/insurance_agency',echo=True)

Base = declarative_base()

class Federal_region(Base):
    __tablename__ = 'Federal_regions'
    id = Column(Integer,primary_key=True)
    name = Column(String(250), nullable=False)
    region = relationship('Region')

class Region(Base):
    __tablename__ = 'Regions'

    id = Column(Integer, primary_key=True)
    federal_region_id = Column(Integer, ForeignKey("Federal_regions.id"))
    name = Column(String(250), nullable=False)
    risk_factor = Column(Double, nullable=False)
    OKATO_region_code = Column(Integer,nullable=False)
    federal_region = relationship('Federal_region')
    contract = relationship('Contract')

class Auto_type(Base):
    __tablename__ = 'Auto_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    risk_factor = Column(Double, nullable=False)
    auto = relationship('Auto')

class Client(Base):
    __tablename__ = 'Clients'

    id = Column(Integer,primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=True)
    passport_number = Column(Integer,nullable=False)
    phone_number = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)
    passport_series = Column(Integer, nullable=False)
    auto_type = relationship('Auto')

class Auto(Base):
    __tablename__ = 'Autos'

    id = Column(Integer,primary_key=True)
    auto_type_id = Column(Integer,ForeignKey("Auto_types.id"))
    client_id = Column(Integer,ForeignKey("Clients.id"))
    number = Column(Integer,nullable=False)
    brand = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    VIN = Column(String(250), nullable=False)
    auto_type = relationship('Auto_type')
    client = relationship('Client')
    contract = relationship('Contract')

class Contract(Base):
    __tablename__ = 'Contracts'

    id = Column(Integer,primary_key=True)
    auto_id = Column(Integer,ForeignKey("Autos.id"))
    region_id = Column(Integer, ForeignKey("Regions.id"))
    start_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)
    insurance_premium = Column(Double, nullable=False)
    liability_limit = Column(Double, nullable=False)
    auto = relationship('Auto')
    region = relationship('Region')
    reason = relationship('Payment')

class Reason(Base):
    __tablename__ = 'Reasons'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    risk_factor = Column(Double, nullable=False)
    payment = relationship('Payment')

class Payment(Base):
    __tablename__ = 'Payments'

    id = Column(Integer,primary_key=True)
    reason_id = Column(Integer, ForeignKey("Reasons.id"))
    contract_id = Column(Integer, ForeignKey("Contracts.id"))
    date = Column(Date, nullable=False)
    payment_sum = Column(Double, nullable=False)
    reason = relationship('Reason')
    contract = relationship('Contract')






Base.metadata.create_all(engine)