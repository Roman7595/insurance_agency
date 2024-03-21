from tkinter import *
from views import Sql_quary_output_view

def get_answer_to_quary(window):
    clear_window(window)
    Sql_quary_output_view.main(window)

def clear_window(window):
    for i in window.winfo_children():
        i.destroy()
def main():
    window = Tk()
    window.geometry("600x600")

    main_frame = Frame(window)
    main_frame.grid(column=0, row=0)

    create_sql_query(main_frame,0,0)

    window.mainloop()

def create_sql_query(window,col,row):

    sql_frame = Frame(window)
    sql_frame.grid(column=col,row=row)

    sql_label = Label(sql_frame, text='Напишите произвольный SQL запрос: ')
    sql_label.grid(column=0,row=0,padx=20, pady=20)

    sql_query = Entry(sql_frame)
    sql_query.grid(column=1,row=0)
    button = Button(sql_frame, text='Выполнить запрос', command= lambda : get_answer_to_quary(window) )
    button.grid(column=2,row=0, padx=20)



