from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend import connection
from backend import Models

engine = create_engine(connection.conn, echo=True)

session = sessionmaker(bind=engine)
s = session()
def get_all_clients_name():
    return dict(s.query(Models.Client.name, Models.Client.id).order_by(Models.Client.id))

def get_all_regions_name():
    return dict(s.query(Models.Region.name, Models.Region.id).order_by(Models.Region.id))

def get_all_contract():
    return dict(s.query(Models.Contract.id, Models.Contract.id).order_by(Models.Contract.id)) # contr number

def get_all_payments():
    return dict(s.query(Models.Payment.id, Models.Payment.id).order_by(Models.Payment.id)) # payment number

def get_all_autos():
    return dict(s.query(Models.Auto.number, Models.Auto.id).order_by(Models.Auto.number)) # payment number

