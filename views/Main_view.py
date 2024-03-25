from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from views import Sql_quary_output_view
from utils import My_utils as u

def get_answer_to_quary(window, quary_type, sql_query_info):
    u.clear_window(window)
    Sql_quary_output_view.main(window, quary_type, sql_query_info)

def verify_date(date, next):
    for i in date:
        if not(u.is_date(i)):
            messagebox.showerror('Error', 'Не правильно указано дата')
            return
    if date[0]>date[1]:
        messagebox.showerror('Error', 'Дата окончания должна быть больше чем дата начала')
        return
    next()

def fill_main_frame(window):
    create_sql_query(window)
    all_contr_by_clients_query(window)
    all_auto_by_clients_query(window)
    all_contr_by_fed_region_query(window)
    all_contr_by_time_query(window)
def main():
    window = Tk()
    window.geometry("600x600")
    main_frame = Frame(window)
    main_frame.pack(padx=20, pady=20)
    fill_main_frame(main_frame)

    window.mainloop()

def create_sql_query(window):

    sql_frame = LabelFrame(window, text='Чистый SQL')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Напишите произвольный SQL запрос: ')
    sql_label.grid(column=0,row=0,padx=20, pady=20)

    sql_query = Entry(sql_frame)
    sql_query.grid(column=1,row=0)

    button = Button(sql_frame, text='Выполнить запрос', command= lambda : get_answer_to_quary(window, u.quary_enum['raw'], [sql_query.get()]) )
    button.grid(column=2,row=0, padx=20)

def all_contr_by_clients_query(window):
    sql_frame = LabelFrame(window, text='Получить все договоры конкретного клиента')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Введите id клиента: ')
    sql_label.grid(padx=20, pady=20)

    client_name = ttk.Combobox(sql_frame)
    client_name['values'] = ['Роман', 'dвтмыл']#TODO: get all client names
    client_name.grid(column=1, row=0)

    button = Button(sql_frame, text='Выполнить', command= lambda : get_answer_to_quary(window, u.quary_enum['contr_by_client'], [client_name.get()]))
    button.grid(column=2,row=0, padx=20)

def all_auto_by_clients_query(window):
    sql_frame = LabelFrame(window, text='Получить все автомобили конкретного клиента')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Введите id клиента: ')
    sql_label.grid(padx=20, pady=20)

    client_name = ttk.Combobox(sql_frame)
    client_name['values'] = ['Роман', 'dвтмыл']  # TODO: get all client names
    client_name.grid(column=1, row=0)

    button = Button(sql_frame, text='Выполнить', command= lambda : get_answer_to_quary(window, u.quary_enum['auto_by_client'], [client_name.get()]) )
    button.grid(column=2,row=0, padx=20)

def all_contr_by_fed_region_query(window):
    sql_frame = LabelFrame(window, text='Получить все договоры по конкретному Федеральному Округу')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Введите id Федерального Округа: ')
    sql_label.grid(padx=20, pady=20)

    fed_region_name = ttk.Combobox(sql_frame)
    fed_region_name['values'] = ['Роман', 'dвтмыл']  # TODO: get all client names
    fed_region_name.grid(column=1, row=0)

    button = Button(sql_frame, text='Выполнить', command= lambda : get_answer_to_quary(window, u.quary_enum['contr_by_fed'], [fed_region_name.get()]) )
    button.grid(column=2,row=0, padx=20)

def all_contr_by_time_query(window):
    sql_frame = LabelFrame(window, text='Получить все договоры по конкретному Федеральному Округу')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Введите дату начала временного периода \n(в формате ГГГГ-ММ-ДД): ')
    sql_label.grid(padx=10, pady=20, column=0, row=0)
    start_time = Entry(sql_frame)
    start_time.grid(padx=10, column=1, row=0)

    sql_label = Label(sql_frame, text='Введите дату окончания временного периода \n(в формате ГГГГ-ММ-ДД): ')
    sql_label.grid(padx=10, pady=20, column=0, row=1)
    expiration_time = Entry(sql_frame)
    expiration_time.grid(padx=10,column=1, row=1)

    button = Button(sql_frame, text='Выполнить',
                    command= lambda : verify_date([start_time.get(), expiration_time.get()],
                                                  lambda : get_answer_to_quary(window, u.quary_enum['contr_by_time'],
                                                                               [start_time.get(), expiration_time.get()])))
    button.grid(column=3,row=2, padx=10, pady=20)


