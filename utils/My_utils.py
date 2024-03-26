import datetime
def clear_window(window):
    for i in window.winfo_children():
        i.destroy()

quary_enum = {'raw': 0,
              'contr_by_client': 1,
              'auto_by_client': 2,
              'contr_by_fed': 3,
              'contr_by_time':4,
              'reasons_by_contr':5,

              }

def is_date(date):
    try:
        (datetime.datetime.strptime(date, '%Y-%m-%d'))
        return True
    except (ValueError):
        return False