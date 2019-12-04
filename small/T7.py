from tkinter import *


def click():
    counter.set(counter.get() + 1)


def Exit():
    exit()


if __name__ == '__main__':
    window = Tk()
    counter = IntVar()
    counter.set(0)

    frame = Frame(window)
    frame.pack()

    button = Button(frame, textvariable=counter, command=click, bg='#176db7', fg='#f3f3f3', width=6, height=3,
                    font=("Helvetica", 32))
    button.pack()

    exit_p = Button(frame, text='Gooooodbye', command=Exit, bg='#4e4e4e', fg='#f3f3f3', width=19, height=1,
                    font=("Helvetica", 10))
    exit_p.pack()

    window.mainloop()
