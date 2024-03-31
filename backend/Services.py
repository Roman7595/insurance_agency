from backend import Repositories as R

def get_contracts_by_client(client_id):
    values = list(R.get_contracts_by_client(client_id[0]))
    columns = R.get_contracts_colums()

    if len(values):
        return (columns, values)
    else:
        return


def raw_sql(sql):
    return
    # values = R.get_contracts_by_client(sql)
    # columns = R.get_contracts_colums()
    #
    # if len(values):
    #     return (1, columns, values)
    # else:
    #     return (1)