from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from utils import My_utils as u
from views import Second_page as s
from views import Main_view as M

REASONS =[]

def back(window):
    u.clear_window(window)
    s.fill_second_frame(window)

def fill_third_frame(window):
    all_contracts_where_reason_quary(window)

    button_frame = Frame(window)
    button_frame.pack(fill='both', pady=20)
    button = Button(button_frame, text='Пред. страница',
                    command=lambda: back(window))
    button.pack(anchor='sw', padx=20)


def all_contracts_where_reason_quary(window):
    sql_frame = LabelFrame(window, text='Договоры, по которым были сделаны данные выплаты')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Выберете количество выплат: ')
    sql_label.grid(padx=20, pady=20)

    count_reasons = Entry(sql_frame)
    count_reasons.grid(padx=10, column=1, row=0)

    reason_frame = Frame(sql_frame)
    reason_frame.grid(column=0,row=1,columnspan=2)

    button = Button(sql_frame, text='Ввести',
                    command=lambda: place_reasons(int(count_reasons.get()), reason_frame))
    button.grid(column=2, row=0, padx=20, pady=20)


    button = Button(sql_frame, text='Выполнить',
                    command= lambda: M.get_answer_to_quary(window, u.quary_enum['count_contract'],
                                                  [i.get() for i in REASONS]))
    button.grid(column=2, row=2, padx=20, pady=20)


def place_reasons(n, window):
    u.clear_window(window)
    reason_count = 5 #TODO: get all reasons count

    if n<=0 or n>reason_count:
        messagebox.showerror('Error', f'Количество причин должно быть натуральным числом не более чем {reason_count}')
        return
    global REASONS
    REASONS = []
    for i in range(n):
        sql_label = Label(window, text=f'Выберете тип выплаты {i}: ')
        sql_label.grid(column=0, row=i, padx=20, pady=20)

        REASONS.append(ttk.Combobox(window, state="readonly"))

        REASONS[-1]['values'] = [['Роман', 'vddfsdfd', 'sdgsdfbdfd'], 'dвтмыл']  # TODO: get payments with contr num
        REASONS[-1].grid(column=1, row=i)
