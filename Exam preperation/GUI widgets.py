from tkinter import *


master = Tk()

t = 'Dette er en eksempeltekst!\n Sola skinner super mye!'

def vindu():
    nytt_vindu = Toplevel()
    tekst_vindu = Label(nytt_vindu, text='Velkommen her!')
    tekst_vindu.grid(row=0)

def endre(x='F'):
    global t
    if x == 'N':
        tekst.set(t)
    else:
        g = inp_v.get()
        v = t.translate({ord(i): g for i in 'aeiouyæøå'})
        t = v
        tekst.set(v)

def set_tekst():
    global t
    h = inp.get()
    t = h
    tekst.set(h)


tekst = StringVar()
tekst.set('Dette er en eksempeltekst!\nSola skinner super mye!')


verdi = IntVar()


knapp = Button(master, text="knapp1", command=vindu)  
knapp.grid(row=0, column=0)

radio1 = Radiobutton(master, text="Normal", value=0, variable=verdi, command=lambda: endre('N'))
radio1.grid(row=0, column=1)

radio2 = Radiobutton(master, text="A", value=1, variable=verdi, command=lambda: endre())
radio2.grid(row=0, column=2)

label = Label(master, textvariable=tekst, width=30)
label.grid(row=1, columnspan=4)

inp = Entry(master, width=25)
inp.grid(row=3, columnspan=4)

inp_v = Entry(master, width=10)
inp_v.grid(row=4, columnspan=4)

knapp = Button(master, text="Sett tekst", command=set_tekst)
knapp.grid(row=5, columnspan=4)


master.mainloop()
