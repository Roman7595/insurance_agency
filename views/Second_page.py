from tkinter import *
from tkinter import ttk
from utils import My_utils as u
from views import Main_view
from views import Third_view as T
from backend import Repositories
def back_to_main_menu(window):
    u.clear_window(window)
    Main_view.fill_main_frame(window)
def next_view(window):
    u.clear_window(window)
    T.fill_third_frame(window)

def fill_second_frame(window):
    payment_dict = Repositories.get_all_payments()
    reason_dict = Repositories.get_all_reasons()
    update_reason_of_payment_query(window,payment_dict,reason_dict)
    auto_dict = Repositories.get_all_autos()
    region_dict = Repositories.get_all_regions_name()
    add_contract_query(window,auto_dict,region_dict)
    contract_dict = Repositories.get_all_contract()
    delete_contract_query(window, contract_dict)
    # count_contract_by_users_quary(window)
    # count_contract_where_payments_quary(window)



    button_frame = Frame(window)
    button_frame.pack(fill='both', pady=20)

    button = Button(button_frame, text='Пред. страница',
                    command=lambda: back_to_main_menu(window))
    button.grid(row=0,column=0, padx=100)

    button = Button(button_frame, text='След. страница',
                    command=lambda: next_view(window))
    button.grid(row=0,column=1, padx=100)

def update_reason_of_payment_query(window, payment_dict, reason_dict):
    sql_frame = LabelFrame(window, text='Изменить причину выплаты ')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Введите выплату: ')
    sql_label.grid(padx=20, pady=10)
    payment_name = ttk.Combobox(sql_frame,state="readonly")
    payment_name['values'] = list(payment_dict.keys())
    payment_name.grid(column=1, row=0)

    sql_label = Label(sql_frame, text='Выберете новую причину выплаты: ')
    sql_label.grid(padx=20, pady=10, row=1)
    reason_name = ttk.Combobox(sql_frame, state="readonly")
    reason_name['values'] = list(reason_dict.keys())
    reason_name.grid(column=1, row=1)

    button = Button(sql_frame, text='Выполнить',
                    command=lambda: Main_view.get_answer_to_quary(window, u.quary_enum['update_reason'], [payment_dict[int(payment_name.get())], reason_dict[reason_name.get()]]))
    button.grid(column=2, row=2, padx=20, pady=10)

def add_contract_query(window,auto_dict,region_dict):

    sql_frame = LabelFrame(window, text='Добавить новый договор')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Выберете автомобиль по номеру: ')
    sql_label.grid(padx=20, pady=5)
    auto_name = ttk.Combobox(sql_frame,state="readonly")
    auto_name['values'] = list(auto_dict.keys())
    auto_name.grid(column=1, row=0)

    sql_label = Label(sql_frame, text='Выберете регион по названию: ')
    sql_label.grid(padx=20, pady=5)
    region_name = ttk.Combobox(sql_frame,state="readonly")
    region_name['values'] = list(region_dict.keys())
    region_name.grid(column=1, row=1)

    sql_label = Label(sql_frame, text='Введите дату начала временного периода \n(в формате ГГГГ-ММ-ДД): ')
    sql_label.grid(padx=10, pady=5, column=0, row=2)
    start_time = Entry(sql_frame)
    start_time.grid(padx=10, column=1, row=2)

    sql_label = Label(sql_frame, text='Введите дату окончания временного периода \n(в формате ГГГГ-ММ-ДД): ')
    sql_label.grid(padx=10, pady=5, column=0, row=3)
    expiration_time = Entry(sql_frame)
    expiration_time.grid(padx=10, column=1, row=3)

    sql_label = Label(sql_frame, text='Введите страховую премию: ')
    sql_label.grid(padx=10, pady=5, column=0, row=4)
    insurance_premium = Entry(sql_frame)
    insurance_premium.grid(padx=10, column=1, row=4)

    sql_label = Label(sql_frame, text='Введите лимит ответственности: ')
    sql_label.grid(padx=10, pady=5, column=0, row=5)
    liability_limit = Entry(sql_frame)
    liability_limit.grid(padx=10, column=1, row=5)

    button = Button(sql_frame, text='Выполнить',
                    command= lambda: u.null_check([auto_name.get(),
                                                   region_name.get(),
                                                   start_time.get(),
                                                   expiration_time.get(),
                                                   insurance_premium.get(),
                                                   liability_limit.get()],
                    lambda: u.verify_positive([int(insurance_premium.get()), int(liability_limit.get())],
                    lambda: u.verify_date([start_time.get(), expiration_time.get()],
                                                  lambda: Main_view.get_answer_to_quary(window, u.quary_enum['add_contract'],
                                                                                        [auto_dict[auto_name.get()],
                                                                                         region_dict[region_name.get()],
                                                                                         start_time.get(),
                                                                                         expiration_time.get(),
                                                                                         insurance_premium.get(),
                                                                                         liability_limit.get()])))))
    button.grid(column=2, row=5, padx=20, pady=10)

def delete_contract_query(window, contract_dict):
    sql_frame = LabelFrame(window, text='Удалить договор ')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Выберете номер договора: ')
    sql_label.grid(padx=20, pady=10)

    contract_number = ttk.Combobox(sql_frame,state="readonly")
    contract_number['values'] = list(contract_dict.keys())
    contract_number.grid(column=1, row=0)

    button = Button(sql_frame, text='Выполнить',
                    command=lambda: Main_view.get_answer_to_quary(window, u.quary_enum['delete_contract'], [contract_dict[int(contract_number.get())]]))
    button.grid(column=2, row=0, padx=20)

# def count_contract_by_users_quary(window):
#     sql_frame = LabelFrame(window, text='Количество договоров на человека ')
#     sql_frame.pack(fill = 'both')
#
#     button = Button(sql_frame, text='Выполнить',
#                     command=lambda: Main_view.get_answer_to_quary(window, u.quary_enum['count_contract_user'],
#                                                                   []))
#     button.grid(column=2, row=0, padx=20, pady=10)
#
# def count_contract_where_payments_quary(window):
#     sql_frame = LabelFrame(window, text='Договоры где есть выплата')
#     sql_frame.pack(fill = 'both')
#
#     button = Button(sql_frame, text='Выполнить',
#                     command=lambda: Main_view.get_answer_to_quary(window, u.quary_enum['count_contract_payment'],
#                                                                   []))
#     button.grid(column=2, row=0, padx=20, pady=10)
#
