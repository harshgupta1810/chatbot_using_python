from tkinter import *
root = Tk()

def sent():
    sent = "You: "+ e.get()
    text.insert(END,"\n" + sent)
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Bot: hello")
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Bot: hi")
    elif (e.get() == 'how are you'):
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif (e.get() == "i'm fine too"):
        text.insert(END, "\n" + "Bot: nice to hear that")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didnt get it.")
text = Text(root, bg='blue', fg='white')
text.grid(row=0, column=0, columnspan=2)
e = Entry(root,width=80)
send = Button( root,text='Sent', bg='deeppink', fg='white', width=20, command=sent).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title( 'Desparete talks')
root.mainloop()

#understand