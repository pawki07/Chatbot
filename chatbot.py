from tkinter import *
root = Tk()
def send():
    send = "You => "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=='hello'):
        txt.insert(END,"\n"+"Bot => Hi")
    elif(e.get()=="hi"):
        txt.insert(END,"\n"+"Bot => Hello")
    elif(e.get()=="how are you"):
        txt.insert(END,"\n"+"Bot => Fine and you")
    elif(e.get()=="fine"):
        txt.insert(END,"\n"+"Bot => Nice to hear")
    elif(e.get()=="tell something about you"):
        txt.insert(END,"\n"+"Bot => I am a chatbot made using python. I will chat with you.")
    elif(e.get()=="that's great"):
        txt.insert(END,"\n"+"Bot => Yup")
    elif(e.get()=="Ok bye"):
        txt.insert(END,"\n"+"Bot => Bye, Have a good day!")
    else:
        txt.insert(END,"\n"+"Bot => Sorry I didn't get it")
    e.delete(0,END)
txt = Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop()