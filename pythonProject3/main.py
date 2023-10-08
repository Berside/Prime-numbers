from tkinter import *
root = Tk()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n
def Btn():
    bd = []
    min = int(minentry.get())
    max = int(maxentry.get())
    for min in range(max):
        a = is_prime(min)
        if a > 2:
            bd.append(a)
    for i in range(len(bd)):
        result.insert(END, f'{(str(bd[i]))} ')
    c['text'] = f'Найдено чисел:{(str(len(bd)))}'

root.geometry('640x480')
root.resizable(width=False, height=False)

minlabel = Label(root, text = "Min Value:")
minlabel.pack()
minentry = Entry(root)
minentry.pack()

maxlabel = Label(root, text = "Max Value:")
maxlabel.pack()
maxentry = Entry(root)
maxentry.pack()

btn = Button(root, text="Find Prime Numbers", command=Btn)
btn.pack()

c = Label(root, text="Найдено чисел:")
c.pack()
result = Text(root,wrap=WORD)
result.pack()

root.mainloop()