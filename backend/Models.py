from sqlalchemy import Column, ForeignKey, Integer, String, Date, Double
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from backend import connection

engine = create_engine(connection.conn, echo=True)

Base = declarative_base()

class Federal_regions(Base):
    __tablename__ = 'federal_regions'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    #region = relationship('regions')
    def __iter__(self):
        return [self.id, self.name].__iter__()


class Regions(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    federal_region_id = Column(Integer, ForeignKey("federal_regions.id"))
    name = Column(String(250), nullable=False)
    risk_factor = Column(Double, nullable=False)
    OKATO_region_code = Column(Integer,nullable=False)
    #federal_region = relationship('federal_regions')
    #contract = relationship('contracts')
    def __iter__(self):
        return [self.id,self.federal_region_id,self.name, self.risk_factor,self.OKATO_region_code].__iter__()


class Auto_types(Base):
    __tablename__ = 'auto_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    risk_factor = Column(Double, nullable=False)
    #auto = relationship('autos')
    def __iter__(self):
        return [self.id, self.name, self.risk_factor, self.auto].__iter__()


class Clients(Base):
    __tablename__ = 'clients'

    id = Column(Integer,primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=True)
    passport_number = Column(Integer,nullable=False)
    phone_number = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)
    passport_series = Column(Integer, nullable=False)
    #auto_type = relationship('autos')
    def __iter__(self):
        return [self.id, self.name, self.surname, self.last_name, self.passport_number, self.phone_number,
                self.email, self.passport_series].__iter__()


class Autos(Base):
    __tablename__ = 'autos'

    id = Column(Integer,primary_key=True)
    auto_type_id = Column(Integer,ForeignKey("auto_types.id"))
    client_id = Column(Integer,ForeignKey("clients.id"))
    number = Column(Integer,nullable=False)
    brand = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    VIN = Column(String(250), nullable=False)
    #auto_type = relationship('auto_types')
    #client = relationship('clients')
    #contract = relationship('contracts')
    def __iter__(self):
        return [self.id, self.auto_type_id, self.client_id, self.number, self.brand, self.model,
                self.VIN].__iter__()


class Contracts(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    auto_id = Column(Integer, ForeignKey("autos.id"))
    region_id = Column(Integer, ForeignKey("regions.id"))
    start_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)
    insurance_premium = Column(Double, nullable=False)
    liability_limit = Column(Double, nullable=False)
    #auto = relationship('autos')
    #region = relationship('regions')
    #reason = relationship('payments')
    def __iter__(self):
        return [self.id, self.auto_id, self.region_id, self.start_date, self.expiration_date, self.insurance_premium, self.liability_limit].__iter__()

class Reasons(Base):
    __tablename__ = 'reasons'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    risk_factor = Column(Double, nullable=False)
    #payment = relationship('payments')
    def __iter__(self):
        return [self.id, self.name, self.risk_factor].__iter__()


class Payments(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    reason_id = Column(Integer, ForeignKey("reasons.id"))
    contract_id = Column(Integer, ForeignKey("contracts.id"))
    date = Column(Date, nullable=False)
    payment_sum = Column(Double, nullable=False)
    #reason = relationship('reasons')
    #contract = relationship('contracts')
    def __iter__(self):
        return [self.id, self.reason_id, self.contract_id, self.date, self.payment_sum, self.reason_id].__iter__()


Base.metadata.create_all(engine)