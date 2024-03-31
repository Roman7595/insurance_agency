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

    if type[0] <= 5 or type[0] >= 9:
        table = ttk.Treeview(table_frame, selectmode='browse')
        table.pack(side='left',fill='both')

        # TODO: scrollbar style
        vert_bar = ttk.Scrollbar(table_frame, orient='vertical', command=table.yview)
        vert_bar.pack(side='right', fill='y')

        table.configure(xscrollcommand=vert_bar.set)

        button = Button(window, text='Назад', command=lambda: back_to_main_menu(window))
        button.pack(anchor='se', pady=20)
        try:
            (columns, values) = output
            table['columns'] = columns
            table['show'] = 'headings'
            for i in table['columns']:
                table.column(i, width=(550//len(table['columns'])), anchor='c')
                table.heading(i, text=i)

            for i in values:
                table.insert('', 'end', values=list(i))
            return
        except TypeError:
            messagebox.showerror('Error', 'По данному запросу ничего не найдено')
            return
    elif type[0]==6:
        (number,new_name) = type[1](sql_query_info)
        out = Label(window, text=f'В выплате №{number} причина выплаты изменена на причину: "{new_name}"')
        out.pack(side='left', fill='both')
    elif type[0]==7:
        out = Label(window, text='Договор успешно добавлен под номером: {number}')
        out.pack(side='left', fill='both')
    elif type[0]==8:
        out = Label(window, text='Договор №{number} успешно удален')
        out.pack(side='left', fill='both')

    button = Button(window, text='Назад', command=lambda: back_to_main_menu(window))
    button.pack(anchor='se', pady=20, padx=20)