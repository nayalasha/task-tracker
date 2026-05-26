from tkinter import *

window = Tk()
window.geometry("1280x720")
window.title("Task Tracker")
window.config(background="lightblue")


# FUNCTION
def submit():
    task = entry.get()

    # prevents empty tasks
    if task != "":
        task_listbox.insert(END, task)
        entry.delete(0, END)


# LABEL
label = Label(
    window,
    text="Task Tracker",
    font=("Arial", 40, 'bold'),
    fg="black",
    bg="lightblue",
    relief=RAISED,
    bd=10,
)

label.pack(pady=20)


# ENTRY BOX
entry = Entry(
    window,
    font=("Arial", 30),
    fg="black",
    bg="white",
    width=30
)

entry.pack(pady=10)


# BUTTON
submit_button = Button(
    window,
    text="Add Task",
    command=submit,
    font=("Arial", 20),
    fg="black",
    bg="#1E90FF",
    activeforeground="white",
    activebackground="#0b66d0",
    bd=4,
    relief=RAISED
)

submit_button.pack(pady=10)


# LISTBOX
task_listbox = Listbox(
    window,
    font=("Arial", 20),
    width=50,
    height=10
)

task_listbox.pack(pady=20)


window.mainloop()