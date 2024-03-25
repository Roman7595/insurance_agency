from tkinter import *
from views import Sql_quary_output_view
from utils import My_utils as u
from utils import quary_enum

def get_answer_to_quary(window, quary_type, sql_query_info):
    u.clear_window(window)
    Sql_quary_output_view.main(window, quary_type, sql_query_info)

def fill_main_frame(window):
    create_sql_query(window)
    all_contr_by_clients_query(window)

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
    button = Button(sql_frame, text='Выполнить запрос', command= lambda : get_answer_to_quary(window, quary_enum.quary_enum['raw'], [sql_query.get()]) )
    button.grid(column=2,row=0, padx=20)

def all_contr_by_clients_query(window):
    sql_frame = LabelFrame(window, text='Получить все договоры конкретного клиента')
    sql_frame.pack(fill='both')

    sql_label = Label(sql_frame, text='Введите id клиента: ')
    sql_label.grid(padx=20, pady=20)

    sql_query = Entry(sql_frame)
    sql_query.grid(column=1,row=0)
    button = Button(sql_frame, text='Выполнить', command= lambda : get_answer_to_quary(window, quary_enum.quary_enum['contr_by_client'], [sql_query.get()]) )
    button.grid(column=2,row=0, padx=20)


