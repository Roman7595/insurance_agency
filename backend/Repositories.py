from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from backend import connection
from backend import Models

engine = create_engine(connection.conn, echo=True)

session = sessionmaker(bind=engine)
s = session()



def get_all_reasons():
    return dict(s.query(Models.Reasons.name, Models.Reasons.id).order_by(Models.Reasons.id))
def get_all_clients_name():
    return dict(map(
        lambda x: (f'{x[0]} {x[1]}' + (f' {x[2]}' if x[2] else ''), x[3]),
        s.query(Models.Clients.name, Models.Clients.surname, Models.Clients.last_name, Models.Clients.id)
        .order_by(Models.Clients.id)))

def get_all_regions_name():
    return dict(s.query(Models.Regions.name, Models.Regions.id)
                .order_by(Models.Regions.id))

def get_all_federal_regions_name():
    return dict(s.query(Models.Federal_regions.name, Models.Federal_regions.id)
                .order_by(Models.Federal_regions.id))

def get_all_contract():
    return dict(s.query(Models.Contracts.id, Models.Contracts.id)
                .order_by(Models.Contracts.id)) # contr number

def get_all_payments():
    return dict(s.query(Models.Payments.id, Models.Payments.id)
                .order_by(Models.Payments.id)) # payment number

def get_all_autos():
    return dict(s.query(Models.Autos.number, Models.Autos.id)
                .order_by(Models.Autos.number)) # payment number

def get_contracts_by_client(client_id):
    return s.query(Models.Contracts).join(Models.Autos)\
        .filter(Models.Autos.client_id == int(client_id))
def get_contracts_columns():
    return Models.Contracts.__table__.columns.keys()


def get_autos_by_client(client_id):
    return s.query(Models.Autos).join(Models.Clients).filter(Models.Autos.client_id == int(client_id))
def get_autos_columns():
    return Models.Autos.__table__.columns.keys()

def get_contracts_by_federal_region(federal_region_id):
    return s.query(Models.Contracts).join(Models.Regions).filter(Models.Regions.federal_region_id == int(federal_region_id))

def get_contracts_by_time(start, end):
    return  s.query(Models.Contracts).filter(Models.Contracts.start_date < end).filter(Models.Contracts.expiration_date > start).order_by(Models.Contracts.start_date)

def get_reasons_columns():
    return Models.Reasons.__table__.columns.keys()

def get_reasons_by_contract(contract_id):
    return s.query(Models.Reasons.id, Models.Reasons.name, Models.Reasons.risk_factor).join(Models.Payments).join(Models.Contracts).filter(Models.Contracts.id == int(contract_id))

def count_contracts_by_client():
    return s.query(Models)

def get_payment_by_id(payment_id):
    return s.query(Models.Payments).filter(Models.Payments.id == int(payment_id)).one()

def update_reason_of_payment(payment_id, new_reason_id):
    payment = get_payment_by_id(payment_id)
    old_reason_id = payment.reason_id
    reasons_dict = get_all_reasons()
    new_reason_name = list(reasons_dict.keys())[list(reasons_dict.values()).index(int(new_reason_id))]
    old_reason_name = list(reasons_dict.keys())[list(reasons_dict.values()).index(int(old_reason_id))]
    print('-'*50+'\n',old_reason_id, old_reason_name, new_reason_name)
    payment.reason_id = new_reason_id
    s.commit()
    return (payment.id, old_reason_name, new_reason_name)
def add_contract(auto_id, region_id, start_date, expiration_date, insurance_premium, liability_limit):
    try:
        new_contract = Models.Contracts(auto_id, region_id, start_date, expiration_date, insurance_premium, liability_limit)
        s.add(new_contract)
        s.commit()
        return new_contract.id
    except:
        s.close()

def select_all(table_name):
    columns = s.execute(text("select column_name from information_schema.columns where table_name = :table_name"), {"table_name": table_name})
    values = s.execute(text("select * from :table_name"), {"table_name": table_name})
    return (columns,values)

def delete_contract(contract_id):
    s.query(Models.Payments).filter(Models.Payments.contract_id == contract_id).delete()
    s.query(Models.Contracts).filter(Models.Contracts.id == contract_id).delete()
    s.commit()
    return contract_id

def multi_reasons(reasons):
    columns = ["AUTO_TYPES.NAME", "COUNT(CONTRACTS.ID)"]

    args =""
    args_values = dict()
    for i in range(len(reasons)):
        args += f":reasons_id{i}, "
        args_values.update({f"reasons_id{i}": reasons[i]})

    sql_text = text(f"SELECT AUTO_TYPES.NAME, "
                    +   "COUNT(CONTRACTS.ID) "
                    +"FROM AUTO_TYPES "
                    +"JOIN AUTOS ON AUTOS.AUTO_TYPE_ID = AUTO_TYPES.ID "
                    +"JOIN CONTRACTS ON CONTRACTS.AUTO_ID = AUTOS.ID "
                    +"WHERE EXISTS "
                    +    "(SELECT * "
                    +        "FROM PAYMENTS "
                    +        "JOIN REASONS ON PAYMENTS.REASON_ID = REASONS.ID "
                    +        f"WHERE REASONS.ID IN ({args[:-2]}) "
                    +        "AND PAYMENTS.CONTRACT_ID = CONTRACTS.ID) "
                    +"GROUP BY AUTO_TYPES.NAME;")

    values = s.execute(sql_text, args_values)
    return (columns, values)