import os
from tkinter import *
from tkinter import filedialog, colorchooser, font


def change_font():
    text.config(font=(font_name.get(), font_size.get()))


def choose_color():
    color = colorchooser.askcolor(title='Pick a color!')
    text.config(fg=str(color[1]))


def bg_color():
    color = colorchooser.askcolor(title='Pick a color!')
    text.config(bg=str(color[1]))


def new_file():
    root.title('Untitled')
    text.delete(1.0, END)


def open_file():
    my_file = filedialog.askopenfilename(title='Open a file',
                                         defaultextension='.txt',
                                         filetypes=(('Text files', '*.txt'),
                                                    ('All files', '*.*'),
                                                    ('HTML file', '*.html'),),
                                         )
    try:
        root.title(os.path.basename(my_file))
        text.delete(1.0, END)
        my_file = open(my_file, "r")
        text.insert(1.0, my_file.read())
    except FileNotFoundError:
        pass
    except AttributeError:
        pass
    finally:
        try:
            my_file.close()
        except AttributeError:
            pass


def save_file():
    my_file = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                           defaultextension='.txt',
                                           filetypes=(('Text files', '*.txt'),
                                                      ('HTML file', '*.html'),
                                                      ('All files', '*.*')),
                                           )
    if my_file is None:
        return
    else:
        try:
            root.title(os.path.basename(my_file))
            my_file = open(my_file, 'w')
            my_file.write(text.get(1.0, END))
        except FileNotFoundError:
            pass
        except AttributeError:
            pass
        finally:
            try:
                my_file.close()
            except AttributeError:
                pass


def cut():
    text.event_generate("<<Cut>>")


def copy():
    text.event_generate("<<Copy>>")


def paste():
    text.event_generate("<<Paste>>")


def edit_quit():
    root.destroy()


root = Tk()
file = None

root.title('GT\'S TEXT EDITOR')
root.iconbitmap('D:\\Code\\Projetcs\\github\\text-editor\\images\\text.ico')

width = 500
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))

root.geometry(f"{width}x{height}+{x}+{y}")

font_name = StringVar(root)
font_name.set('Arial')

font_size = StringVar(root)
font_size.set('25')

text = Text(root, bg='#ffffdb', fg='black', font=(font_name.get(), font_size.get()))
text.grid(sticky=N + E + W + S)

scroll = Scrollbar(text, width=10, bg='grey', bd=1, command=text.yview, cursor="pirate")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set)

frame = Frame(root)
frame.grid()

bg_color_button = Button(frame, text='Background color', command=bg_color)
bg_color_button.grid(row=0, column=0)
color_button = Button(frame, text='Text color', command=choose_color)
color_button.grid(row=0, column=1)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=2)
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=3)
"""
# CREATING THE MENU
"""
menu_bar = Menu(root)
root.config(menu=menu_bar)
"""
# FILE MENU
"""
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=edit_quit)
"""
# EDIT MENU
"""
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=cut)
edit_menu.add_separator()
edit_menu.add_command(label='Copy', command=copy)
edit_menu.add_command(label='Paste', command=paste)

root.mainloop()
