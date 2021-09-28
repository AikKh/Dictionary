from tkinter import *  
alpha = 'abcdefghijklmnopqrstuvwxyz'

def DoneA():
    txt.focus()
    btnDone = Button(window, text="Done", command=choice_A)
    btnDone.grid(column=1, row=1) 

def DoneB():
    txt.focus()
    btnDone = Button(window, text="Done", command=choice_B)
    btnDone.grid(column=1, row=1) 

def DoneC():
    txt.focus()
    btnDone = Button(window, text="Done", command=choice_C)
    btnDone.grid(column=1, row=1) 

def choice_A():
    list_txt_A = txt.get()
    list_txt_A = list_txt_A.split(" ")
    list_txt_A.sort()
    list_txt_A = ', '.join(list_txt_A)
    lbl_A = Label(window, text=list_txt_A, font=("Arial Bold", 10))  
    lbl_A.grid(column=0, row=7)

def choice_B():
    list_txt_B = txt.get()
    x=7
    for i in alpha:
        count = list_txt_B.count(i) + list_txt_B.count(i.upper())
        if count == 0:
            continue
        lbl_B = Label(window, text=(("{} - {}".format(i.upper(), count))))
        lbl_B.grid(column=0, row=x)
        x+=1

def choice_C():
    count_letters = 0
    text = txt.get()
    x = 7
    for i in alpha:
        count_letter = text.count(i)
        count_letters = count_letters + count_letter
    totalLen = count_letters
    for j in alpha:
        count = text.count(j) + text.count(j.upper())
        if count == 0:
            continue
        formating = "{:.2f}".format(round((count/totalLen*100),2))
        percent = (("{0},{1} - {2}%".format(j.upper(), j, formating)))
        lbl_C = Label(window, text=percent, font=("Arial Bold", 10))
        lbl_C.grid(column=0, row=x)
        x+=1
    
  
window = Tk()  
window.title("Dictionary")  
window.geometry('400x450')


txt = Entry(window,width=10)  
txt.grid(column=0, row=1) 


btnA = Button(window, text="A", command=DoneA)
btnA.place(width=1000, height=1000)
btnA.grid(column=0, row=0) 
btnB = Button(window, text="B", command=DoneB)
btnB.grid(column=2, row=0)
btnC = Button(window, text="C", command=DoneC)
btnC.grid(column=4, row=0)

 
window.mainloop()