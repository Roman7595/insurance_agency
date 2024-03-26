from tkinter import *
from tkinter import ttk
from utils import My_utils as u
from views import Main_view

def back_to_main_menu(window):
    u.clear_window(window)
    Main_view.fill_main_frame(window)

def fill_second_frame(window):
    update_reason_of_payment(window)
    # all_contr_by_clients_query(window)
    # all_auto_by_clients_query(window)
    # all_contr_by_fed_region_query(window)
    # all_contr_by_time_query(window)
    # all_reasons_by_contr_query(window)

    button_frame = Frame(window)
    button_frame.pack(fill='both', pady=20)

    button = Button(button_frame, text='Пред. страница',
                    command=lambda: back_to_main_menu(window))
    button.pack(anchor='sw', padx=20)

def update_reason_of_payment(window):
    sql_frame = LabelFrame(window, text='Изменить причину выплаты ')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Введите выплату: ')
    sql_label.grid(padx=20, pady=20)

    client_name = ttk.Combobox(sql_frame)
    client_name['values'] = [['Роман','vddfsdfd','sdgsdfbdfd'], 'dвтмыл']  # TODO: get payments with contr num
    client_name.grid(column=1, row=0)

    button = Button(sql_frame, text='Выполнить запрос',
                    command=lambda: Main_view.get_answer_to_quary(window, u.quary_enum['raw'], [client_name.get()]))
    button.grid(column=2, row=0, padx=20)