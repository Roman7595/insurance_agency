import datetime
from tkinter import messagebox
from backend import Services
def clear_window(window):
    for i in window.winfo_children():
        i.destroy()

quary_enum = {'raw': (0,lambda x: Services.select_all(x)),
              'contr_by_client': (1,lambda x: Services.get_contracts_by_client(x)),
              'auto_by_client': (2, lambda x: Services.get_autos_by_client(x)),
              'contr_by_fed': (3, lambda x: Services.get_contracts_by_federal_region(x)),
              'contr_by_time': (4, lambda x: Services.get_contracts_by_time(x)),
              'reasons_by_contr': (5, lambda x: Services.get_reasons_by_contract(x)),
              'update_reason': (6, lambda x: Services.update_reason_of_payment(x)),
              'add_contract': (7, lambda x: Services.add_cotract(x)),
              'delete_contract': (8, lambda x: Services.delete_contract(x)),
              'multi_reasons': 9,
              }

tables_names = ["autos","auto_types","clients","contracts","federal_regions","payments","reasons","regions"]

def verify_positive(nums, next):
    for i in nums:
        if i < 0:
            messagebox.showerror('Error', 'Страховая премия или лимит ответственности отрицательные')
            return
    if nums[0]>nums[1]:
        messagebox.showerror('Error', 'Страховая премия должна быть меньше чем лимит ответственности')
        return
    next()

def verify_date(date, next):
    for i in date:
        if not(is_date(i)):
            messagebox.showerror('Error', 'Не правильно указана дата')
            return
    if date[0]>date[1]:
        messagebox.showerror('Error', 'Дата окончания должна быть больше чем дата начала')
        return
    next()

def is_date(date):
    try:
        (datetime.datetime.strptime(date, '%Y-%m-%d'))
        return True
    except (ValueError):
        return False

def null_check(data, next):
    for i in data:
        if not(i):
            messagebox.showerror('Error', 'Не все значения заполнены')
            return
    next()

def verify_table_name(name, next):
    if not(name in tables_names):
        messagebox.showerror('Error', 'Не правильно указано название таблицы')
        return
    next()