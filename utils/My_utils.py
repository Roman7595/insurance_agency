def clear_window(window):
    for i in window.winfo_children():
        i.destroy()