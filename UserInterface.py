from tkinter import *
from tkinter import messagebox

def get_num_faces():
    root = Tk()

    def get_count():
        file = open('data.txt', 'w')
        file.write(face_entry.get())
        root.destroy()
        file.close()

    frame = Frame(bg = '#262626')
    face_label = Label(frame, text = 'ENTER NUMBER OF FACES', font = 'serif 24', fg = '#ffa300', bg = '#262626', pady = 20)
    face_entry = Entry(frame, font = 'times 20')
    temp_label = Label(frame, text = '', bg = '#262626', pady = 10)
    ok_button = Button(frame, text = 'OK', font = 'tmes 15', command = get_count)

    face_label.grid(row = 1, column = 1)
    face_entry.grid(row = 3, column = 1)
    temp_label.grid(row = 4)
    ok_button.grid(columnspan = 2)

    frame.pack()

    root.title('Live Face Recognition')
    root.configure(background='#262626')
    root.geometry('400x200+750+400')
    root.mainloop()


def get_name():

    def get_text():
        file = open('data.txt', 'a')
        file.write(name_entry.get())
        file.write('\n')
        file.close()
        master.destroy()

    master = Tk()

    frame = Frame(bg = '#262626')
    name_label = Label(frame, text = 'ENTER NAME', font = 'serif 24', fg = '#ffa300', bg = '#262626', pady = 20)
    name_entry = Entry(frame, font = 'times 20')
    temp_label = Label(frame, text = '', bg = '#262626', pady = 10)
    ok_button = Button(frame, text = 'OK', font = 'tmes 15', command = get_text)

    name_label.grid(row = 1, column = 1)
    name_entry.grid(row = 3, column = 1)
    temp_label.grid(row = 4)
    ok_button.grid(columnspan = 2)

    frame.pack()

    master.title('Live Face Recignition')
    master.configure(bg = '#262626')
    master.geometry('400x200+750+400')
    master.mainloop()
