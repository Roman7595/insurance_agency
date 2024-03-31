from tkinter import *
from tkinter import ttk

import backend.Repositories
from views import Sql_quary_output_view
from utils import My_utils as u
from views import Second_page as s


def get_answer_to_quary(window, quary_type, sql_query_info):
    u.clear_window(window)
    Sql_quary_output_view.main(window, quary_type, sql_query_info)

def second_view(window):
    u.clear_window(window)
    s.fill_second_frame(window)

def fill_main_frame(window):
    create_sql_query(window)

    client_name_dict = backend.Repositories.get_all_clients_name()
    all_contr_by_clients_query(window, client_name_dict)
    all_auto_by_clients_query(window, client_name_dict)

    region_name_dict = backend.Repositories.get_all_regions_name()
    all_contr_by_fed_region_query(window, region_name_dict)
    all_contr_by_time_query(window)

    contract_dict = backend.Repositories.get_all_contract()
    all_reasons_by_contr_query(window, contract_dict)

    button_frame = Frame(window)
    button_frame.pack(fill='both', pady=20)

    button = Button(button_frame, text='След. страница',
                    command=lambda: second_view(window))
    button.pack(anchor='se', padx=20)
def main():
    window = Tk()
    window.geometry("600x750")
    main_frame = Frame(window)
    main_frame.pack(padx=20, pady=20)
    fill_main_frame(main_frame)

    window.mainloop()

def create_sql_query(window):

    sql_frame = LabelFrame(window, text='Чистый SQL запрос')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Напишите произвольный SQL запрос: ')
    sql_label.grid(column=0,row=0,padx=20, pady=20)

    sql_query = Entry(sql_frame)
    sql_query.grid(column=1,row=0)

    button = Button(sql_frame, text='Выполнить запрос', command= lambda : get_answer_to_quary(window, u.quary_enum['raw'], [sql_query.get()]) )
    button.grid(column=2,row=0, padx=20)

def all_contr_by_clients_query(window, client_name_dict):
    sql_frame = LabelFrame(window, text='Получить все договоры конкретного клиента')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Введите имя клиента: ')
    sql_label.grid(padx=20, pady=20)

    client_name = ttk.Combobox(sql_frame, state="readonly")
    client_name['values'] = list(client_name_dict.keys())
    client_name.grid(column=1, row=0)



    button = Button(sql_frame, text='Выполнить', command= lambda : get_answer_to_quary(window, u.quary_enum['contr_by_client'], [client_name_dict[client_name.get()]]))
    button.grid(column=2,row=0, padx=20)

def all_auto_by_clients_query(window, client_name_dict):
    sql_frame = LabelFrame(window, text='Получить все автомобили конкретного клиента')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Введите имя клиента: ')
    sql_label.grid(padx=20, pady=20)

    client_name = ttk.Combobox(sql_frame, state="readonly")
    client_name['values'] = list(client_name_dict.keys())
    client_name.grid(column=1, row=0)

    button = Button(sql_frame, text='Выполнить', command= lambda : get_answer_to_quary(window, u.quary_enum['auto_by_client'], [client_name_dict[client_name.get()]]) )
    button.grid(column=2,row=0, padx=20)

def all_contr_by_fed_region_query(window, region_name_dict):
    sql_frame = LabelFrame(window, text='Получить все договоры по конкретному Федеральному Округу')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Введите название Федерального Округа: ')
    sql_label.grid(padx=20, pady=20)

    fed_region_name = ttk.Combobox(sql_frame,state="readonly")
    fed_region_name['values'] = list(region_name_dict.keys())
    fed_region_name.grid(column=1, row=0)

    button = Button(sql_frame, text='Выполнить', command= lambda : get_answer_to_quary(window, u.quary_enum['contr_by_fed'], [region_name_dict[fed_region_name.get()]]) )
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
                    command= lambda : u.verify_date([start_time.get(), expiration_time.get()],
                                                  lambda : get_answer_to_quary(window, u.quary_enum['contr_by_time'],
                                                                               [start_time.get(), expiration_time.get()])))
    button.grid(column=3,row=2, padx=10, pady=20)

def all_reasons_by_contr_query(window, contract_dict):
    sql_frame = LabelFrame(window, text='Получить все причины выплат по конкретному Договору')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Введите номер Договора: ')
    sql_label.grid(padx=20, pady=20)

    contr_number = ttk.Combobox(sql_frame, state="readonly")
    contr_number['values'] = list(contract_dict.keys())
    contr_number.grid(column=1, row=0)

    button = Button(sql_frame, text='Выполнить',
                    command=lambda: get_answer_to_quary(window, u.quary_enum['reasons_by_contr'], [contract_dict[int(contr_number.get())]]))
    button.grid(column=2, row=0, padx=20)

