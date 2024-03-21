from tkinter import *
from views import Sql_quary_output_view
from utils import My_utils as u

def get_answer_to_quary(window, sql_query):
    u.clear_window(window)
    Sql_quary_output_view.main(window, sql_query)

def fill_main_frame(window):
    create_sql_query(window, 0, 0)

def main():
    window = Tk()
    window.geometry("600x600")
    main_frame = Frame(window)
    main_frame.pack(padx=20, pady=20)
    fill_main_frame(main_frame)

    window.mainloop()

def create_sql_query(window,col,row):

    sql_frame = Frame(window)
    sql_frame.grid(column=col,row=row)

    sql_label = Label(sql_frame, text='Напишите произвольный SQL запрос: ')
    sql_label.grid(column=0,row=0,padx=20, pady=20)

    sql_query = Entry(sql_frame)
    sql_query.grid(column=1,row=0)
    button = Button(sql_frame, text='Выполнить запрос', command= lambda : get_answer_to_quary(window, sql_query.get()) )
    button.grid(column=2,row=0, padx=20)



