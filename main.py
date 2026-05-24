from tkinter import *
window=Tk()
window.geometry("1280x720")
window.title("Task Tracker")

# button
def click():
    print("Button Clicked")

def submit():
    task = entry.get()
    print(f"Task Added: {task}")



submit_button = Button(window,
                    text="Add Task",
                    command=submit,
                    font=("Arial", 20),
                    fg="black",
                    bg="#1E90FF",
                    activeforeground="white",
                    activebackground="#0b66d0",
                    bd=4,
                    relief=RAISED,
                    state=ACTIVE
                   )
submit_button.pack(side=RIGHT, padx=10)

# text box for task input

entry = Entry(window,
              font=("Arial", 
                    40,),
                fg="black",
                bg="white",


              )
entry.insert(0, "Enter your task here")
entry.pack(side=LEFT)

x = IntVar()

def display():
    if x.get() == 1:
        print("Task marked as completed")
    else:
        print("Task marked as not completed")

check_button = Checkbutton(window,
                           text="Mark as Completed",
                       font=("Arial", 20),
                          fg="black",
                            bg="lightblue",
                            variable= x,
                            onvalue=1,
                            offvalue=0,
                            command=display,
                            

                      )
check_button.pack(side=BOTTOM)
# use pack for consistent layout so the button's text is visible


window.config(background="lightblue")

# label
label = Label(window, text="Task Tracker",
               font=("Arial", 40,'bold')
               , fg="black", 
               bg="lightblue",
               relief=RAISED,
               bd=10,)


label.pack(pady=20)

# show the button below the label

# ensure the button is above other widgets and redraw immediately
submit_button.lift()
window.update()

window.mainloop()
