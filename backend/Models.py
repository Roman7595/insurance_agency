from sqlalchemy import Column, ForeignKey, Integer, String, Date, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from backend import connection

engine = create_engine(connection.conn,echo=True)

Base = declarative_base()

class Federal_region(Base):
    __tablename__ = 'Federal_regions'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    region = relationship('Region')
    def __iter__(self):
        return [self.id, self.name].__iter__()


class Region(Base):
    __tablename__ = 'Regions'

    id = Column(Integer, primary_key=True)
    federal_region_id = Column(Integer, ForeignKey("Federal_regions.id"))
    name = Column(String(250), nullable=False)
    risk_factor = Column(Double, nullable=False)
    OKATO_region_code = Column(Integer,nullable=False)
    federal_region = relationship('Federal_region')
    contract = relationship('Contract')
    def __iter__(self):
        return [self.id,self.federal_region_id,self.name, self.risk_factor,self.OKATO_region_code].__iter__()


class Auto_type(Base):
    __tablename__ = 'Auto_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    risk_factor = Column(Double, nullable=False)
    auto = relationship('Auto')
    def __iter__(self):
        return [self.id, self.name, self.risk_factor, self.auto].__iter__()


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
    def __iter__(self):
        return [self.id, self.name, self.surname, self.last_name, self.passport_number, self.phone_number,
                self.email, self.passport_series].__iter__()


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
    def __iter__(self):
        return [self.id, self.auto_type_id, self.client_id, self.number, self.brand, self.model,
                self.VIN].__iter__()


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
    def __iter__(self):
        return [self.id,self.auto_id,self.region_id, self.start_date,self.expiration_date,self.insurance_premium,self.liability_limit].__iter__()

class Reason(Base):
    __tablename__ = 'Reasons'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    risk_factor = Column(Double, nullable=False)
    payment = relationship('Payment')
    def __iter__(self):
        return [self.id, self.name, self.risk_factor].__iter__()


class Payment(Base):
    __tablename__ = 'Payments'

    id = Column(Integer,primary_key=True)
    reason_id = Column(Integer, ForeignKey("Reasons.id"))
    contract_id = Column(Integer, ForeignKey("Contracts.id"))
    date = Column(Date, nullable=False)
    payment_sum = Column(Double, nullable=False)
    reason = relationship('Reason')
    contract = relationship('Contract')
    def __iter__(self):
        return [self.id, self.reason_id, self.contract_id, self.date, self.payment_sum, self.reason_id].__iter__()


Base.metadata.create_all(engine)