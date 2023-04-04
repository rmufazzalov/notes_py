from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import messagebox
file_name = None


def new_file():
    global file_name
    file_name = 'Без названия'
    text.delete('1.0', END)  # очищаем текстовое окно


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror('Не получилось сохранить файл')


def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


root = Tk()  # окно заметок
root.title('Заметки')
root.geometry('400x400')

text = Text(root, width=400, height=400)
text.pack  # вставляем текстовое окно

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label='Файл', menu=file_menu)


root.config(menu=menu_bar)
root.mainloop()
