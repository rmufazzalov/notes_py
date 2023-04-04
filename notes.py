from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import filedialog
from tkinter import messagebox
from tkinter.messagebox import showinfo
import os
file_name = None


def new_file():
    global file_name
    file_name = 'Без названия'
    text.delete('1.0', END)  # очищаем текстовое окно


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.json')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror('Не получилось сохранить файл')


def delete_file():
    rmfile = filedialog.askopenfilename()
    try:
        os.remove(rmfile)
        showinfo(title='Файл удалён', message=rmfile)
    except Exception:
        messagebox.showerror('Не получилось удалить файл')


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
text.pack()  # вставляем текстовое окно

menu_bar = Menu(root)
file_menu = Menu(menu_bar)

# добавляем меню
file_menu.add_command(label='Новый', command=new_file)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить как', command=save_as)
file_menu.add_command(label='Удалить файл', command=delete_file)
menu_bar.add_cascade(label='Файл', menu=file_menu)
root.config(menu=menu_bar)
root.mainloop()
