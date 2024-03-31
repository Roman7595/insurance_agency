from backend import Repositories as R


def raw_sql(sql):
    return
    # values = R.get_contracts_by_client(sql)
    # columns = R.get_contracts_colums()
    #
    # if len(values):
    #     return (1, columns, values)
    # else:
    #     return (1)

def get_contracts_by_client(client_id):
    client_id = client_id[0]
    values = list(R.get_contracts_by_client(client_id))
    columns = R.get_contracts_columns()

    if len(values):
        return (columns, values)
    else:
        return

def get_autos_by_client(client_id):
    client_id = client_id[0]
    values = list(R.get_autos_by_client(client_id))
    columns = R.get_autos_columns()

    if len(values):
        return (columns, values)
    else:
        return

def get_contracts_by_federal_region(client_id):
    client_id = client_id[0]
    values = list(R.get_contracts_by_federal_region(client_id))
    columns = R.get_contracts_columns()

    if len(values):
        return (columns, values)
    else:
        return

def get_contracts_by_time(period):
    (start, end) = period
    values = list(R.get_contracts_by_time(start,end))
    columns = R.get_contracts_columns()

    if len(values):
        return (columns, values)
    else:
        return

def get_reasons_by_contract(contract_id):
    contract_id = contract_id[0]
    values = list(R.get_reasons_by_contract(contract_id))
    columns = R.get_reasons_columns()

    if len(values):
        return (columns, values)
    else:
        return

def update_reason_of_payment(data):
    (payment_id, reason_id) = data
    payment = R.get_payment_by_id(payment_id)
    # old_reason_id = payment.reason_id

    reasons_dict = R.get_all_reasons()
    new_reason_name = list(reasons_dict.keys())[list(reasons_dict.values()).index(int(reason_id))]
    # old_reason_name = list(reasons_dict.keys())[list(reasons_dict.values()).index(int(old_reason_id))]
    # print(old_reason_id, old_reason_name, new_reason_name)
    payment.reason_id = reason_id

    if(R.commit()):
        # print(old_reason_id, old_reason_name, new_reason_name)
        return (payment.id ,new_reason_name)
    else:
        return