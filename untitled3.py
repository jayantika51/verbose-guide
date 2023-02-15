from tkinter import*

root=Tk()
root.title("Ascii")

root.geometry("500x500")
root.configure(background='red')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.5,anchor=CENTER)
#label
label=Label(root, text="Name in ASCII :",bg="light yellow", fg="black")

#function
def asciiConverter():
    
    #input_box
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) +"  "
        
        #button
        btn=Button(root,text="Show name in Ascii",command=asciiConverter, bg='gold',fg='blue')
        btn.place(relx=0.5, rely=0.5,anchor=CENTER)
        
        #LABEL
        label.place(relx=0.5,rely=0.5,anchor=CENTER)
         #End of funtion
        
root.mainloop()