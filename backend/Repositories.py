from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend import connection
from backend import Models

engine = create_engine(connection.conn, echo=True)

session = sessionmaker(bind=engine)
s = session()


def commit():
    s.commit()
    return True
def get_all_reasons():
    return dict(s.query(Models.Reason.name, Models.Reason.id).order_by(Models.Reason.id))
def get_all_clients_name():
    return dict(s.query(Models.Client.name, Models.Client.id).order_by(Models.Client.id))

def get_all_regions_name():
    return dict(s.query(Models.Region.name, Models.Region.id).order_by(Models.Region.id))

def get_all_federal_regions_name():
    return dict(s.query(Models.Federal_region.name, Models.Federal_region.id).order_by(Models.Federal_region.id))

def get_all_contract():
    return dict(s.query(Models.Contract.id, Models.Contract.id).order_by(Models.Contract.id)) # contr number

def get_all_payments():
    return dict(s.query(Models.Payment.id, Models.Payment.id).order_by(Models.Payment.id)) # payment number

def get_all_autos():
    return dict(s.query(Models.Auto.number, Models.Auto.id).order_by(Models.Auto.number)) # payment number

def get_contracts_by_client(client_id):
    return s.query(Models.Contract).join(Models.Auto).filter(Models.Auto.client_id == int(client_id))
def get_contracts_columns():
    return Models.Contract.__table__.columns.keys()


def get_autos_by_client(client_id):
    return s.query(Models.Auto).join(Models.Client).filter(Models.Auto.client_id == int(client_id))
def get_autos_columns():
    return Models.Auto.__table__.columns.keys()

def get_contracts_by_federal_region(federal_region_id):
    return s.query(Models.Contract).join(Models.Region).filter(Models.Region.federal_region_id == int(federal_region_id))

def get_contracts_by_time(start,end):
    return  s.query(Models.Contract).filter(Models.Contract.start_date < end).filter(Models.Contract.expiration_date > start).order_by(Models.Contract.id)

def get_reasons_columns():
    return Models.Reason.__table__.columns.keys()

def get_reasons_by_contract(contract_id):
    return s.query(Models.Reason.id,Models.Reason.name,Models.Reason.risk_factor).join(Models.Payment).join(Models.Contract).filter(Models.Contract.id == int(contract_id))

def update_reason_of_payment():
    pass

def count_contracts_by_client():
    return s.query(Models)

def get_payment_by_id(payment_id):
    return s.query(Models.Payment).filter(Models.Payment.id == int(payment_id)).one()
