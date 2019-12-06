# GUI OPPGAVER

from tkinter import *


class GUI:

    def __init__(self, master):
        self.vokaler = 'aeiouyæøå'
        self.master = master

        self.jio = 'Tre små kinesere på Højbro plass\nsatt og spilte på en kontrabass.\nSå kom en konstabel, spurte hva det var,\ntre små kinesere på Høybroplass'

        self.text = StringVar()
        self.text.set(self.jio)

        self.var = IntVar()

        self.r1 = Radiobutton(self.master, text='Normal', variable=self.var, value=0, command=lambda: self.vok('N'))
        self.r2 = Radiobutton(self.master, text='A', variable=self.var, value=1, command=lambda: self.vok('A'))
        self.r3 = Radiobutton(self.master, text='E', variable=self.var, value=2, command=lambda: self.vok('E'))
        self.r4 = Radiobutton(self.master, text='I', variable=self.var, value=3, command=lambda: self.vok('I'))
        self.r5 = Radiobutton(self.master, text='O', variable=self.var, value=4, command=lambda: self.vok('O'))
        self.r6 = Radiobutton(self.master, text='U', variable=self.var, value=5, command=lambda: self.vok('U'))
        self.r7 = Radiobutton(self.master, text='Y', variable=self.var, value=6, command=lambda: self.vok('Y'))
        self.r8 = Radiobutton(self.master, text='Æ', variable=self.var, value=7, command=lambda: self.vok('Æ'))
        self.r9 = Radiobutton(self.master, text='Ø', variable=self.var, value=8, command=lambda: self.vok('Ø'))
        self.r10 = Radiobutton(self.master, text='Å', variable=self.var, value=9, command=lambda: self.vok('Å'))

        self.r1.grid(row=0, column=0)
        self.r2.grid(row=0, column=1)
        self.r3.grid(row=0, column=2)
        self.r4.grid(row=0, column=3)
        self.r5.grid(row=0, column=4)
        self.r6.grid(row=0, column=5)
        self.r7.grid(row=0, column=6)
        self.r8.grid(row=0, column=7)
        self.r9.grid(row=0, column=8)
        self.r10.grid(row=0, column=9)

        self.lab = Label(self.master, textvariable=self.text, width=40)
        self.lab.grid(row=1, columnspan=40)

    def vok(self, x):
        if x == 'N':
            self.text.set(
                'Tre små kinesere på Højbro plass\nsatt og spilte på en kontrabass.\nSå kom en konstabel, spurte hva det var,\ntre små kinesere på Høybroplass')
        else:
            p = self.jio.translate({ord(i): x.lower() for i in self.vokaler})
            self.text.set(p)


k = Tk()
d = GUI(k)
k.mainloop()


