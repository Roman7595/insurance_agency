from tkinter import *


def main():
    window = Tk()
    window.geometry("600x600")

    create_sql_query(window)

    window.mainloop()

def create_sql_query(window):

    sql_frame = Frame(window)
    sql_frame.grid(column=0,row=0)

    sql_label = Label(sql_frame, text='Напишите произвольный SQL запрос: ')
    sql_label.grid(column=0,row=0,padx=20, pady=20)

    sql_query = Entry(sql_frame)
    sql_query.grid(column=1,row=0)

    button = Button(sql_frame, text='Выполнить запрос')
    button.grid(column=2,row=0, padx=20)



