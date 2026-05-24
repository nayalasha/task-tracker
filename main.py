from tkinter import *
window=Tk()
window.geometry("500x500")
window.title("My First GUI")

# button
def click():
    print("Button Clicked")

button = Button(window,
                    text="Add Task",
                    command=click,
                    font=("Arial", 20),
                    fg="white",
                    bg="#1E90FF",
                    activeforeground="white",
                    activebackground="#0b66d0",
                    bd=4,
                    relief=RAISED,
                   )

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
button.pack(pady=10)
# ensure the button is above other widgets and redraw immediately
button.lift()
window.update()

window.mainloop()
