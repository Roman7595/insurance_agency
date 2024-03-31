from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from utils import My_utils as u
from views import Main_view

def back_to_main_menu(window):
    u.clear_window(window)
    Main_view.fill_main_frame(window)

def main(window, type, sql_query_info):
    output = type[1](sql_query_info)
    if type[0] == 0:
        label = Label(window, text= f'Результаты по запросу "{sql_query_info[0]}":')
    else:
        label = Label(window, text=f'Результаты по запросу №{type[0]}:')

    label.pack(side='top')

    table_frame = Frame(window)
    table_frame.pack(fill='both')



    table = ttk.Treeview(table_frame, selectmode='browse')
    table.pack(side='left',fill='both')

    # TODO: scrollbar style
    vert_bar = ttk.Scrollbar(table_frame, orient='vertical', command=table.yview)
    vert_bar.pack(side='right', fill='y')

    table.configure(xscrollcommand=vert_bar.set)

    button = Button(window, text='Назад', command=lambda: back_to_main_menu(window))
    button.pack(anchor='se')
    try:
        (columns, values) = output

        table['columns'] = columns
        table['show'] = 'headings'
        for i in table['columns']:
            table.column(i, width=(550//len(table['columns'])), anchor='c')
            table.heading(i, text=i)

        for i in values:
            print(1, list(i))
            table.insert('', 'end', values=list(i))

    except TypeError:
        messagebox.showerror('Error', 'По данному запросу ничего не найдено')
        return


