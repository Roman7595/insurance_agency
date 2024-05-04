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

def update_reason_of_payment(data):#return to repo input:id,id output: New_name
    (payment_id, new_reason_id) = data
    return R.update_reason_of_payment(payment_id, new_reason_id)


def select_all(data):
    (table_name) = data[0]
    (columns, values) = R.select_all(table_name)

    parsed_columns=[]

    for i in columns:
        parsed_columns.append(i[0])

    parsed_values = []
    for i in values:
        parsed_values.append(i)

    return (parsed_columns, parsed_values)