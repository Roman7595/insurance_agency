from tkinter import *
from tkinter import ttk
from utils import My_utils as u
from views import Main_view
def back_to_main_menu(window):
    u.clear_window(window)
    Main_view.fill_main_frame(window)

def main(window, type,sql_query_info):
    if type == 0:
        label = Label(window, text= f'Результаты по запросу "{sql_query_info[0]}":')
    else:
        label = Label(window, text=f'Результаты по запросу №{type}:, {sql_query_info}')
    label.pack(side='top')

    table_frame = Frame(window)
    table_frame.pack()


    table = ttk.Treeview(table_frame, selectmode='browse')
    table.pack(side='left')

    # TODO: scrollbar style
    vert_bar = ttk.Scrollbar(table_frame, orient='vertical', command=table.yview)
    vert_bar.pack(side='right', fill='y')

    table.configure(xscrollcommand= vert_bar.set)


    if type == 0:# TODO: backend function to get table
        pass
    elif type == 1:
        pass
    elif type == 1:
        pass
    elif type == 1:
        pass
    elif type == 1:
        pass
    elif type == 1:
        pass
    elif type == 1:
        pass
    else:
        pass #error
    table['columns'] = ('1','2','3')
    table['show'] = 'headings'
    table.column('1', width=90, anchor='c')
    table.column('2', width=90, anchor='c')
    table.column('3', width=90, anchor='c')
    table.heading('1', text='rgd')
    table.heading('2', text='sggbs')
    table.heading('3', text='sdbdb')
    for i in range(15):
        table.insert('', 'end', text='L1', values=(f'{i}',f'{i+1}',f'{i-1}'))


    button = Button(window,text='Назад', command= lambda : back_to_main_menu(window))
    button.pack()


