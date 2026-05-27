from tkinter import *

window = Tk()
window.geometry("1280x720")
window.title("Task Tracker")



# FUNCTION TO CHANGE BACKGROUND
def change_mode(selected_color):
    window.config(background=selected_color)

    # optional: update label backgrounds too
    label.config(bg=selected_color)


# DEFAULT MODE
mode = "lightblue"

# VARIABLE
mode_var = StringVar(value=mode)


# LABEL
label = Label(
    window,
    text="Task Tracker",
    font=("Arial", 40, "bold"),
    bg=mode
)

label.pack(pady=20)


# DROPDOWN MENU
mode_menu = OptionMenu(
    window,
    mode_var,
    "lightblue",
    "lightgray",
    "lightyellow",
    "lightgreen",
    "lightpink",
    command=change_mode
)

mode_menu.config(
    font=("Arial", 12),
    bg="white",
    fg="black"
)

mode_menu.pack(pady=10)


window.config(background=mode)





# ---------------- FUNCTIONS ---------------- #

def save_tasks():
    tasks = task_listbox.get(0, END)

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            for task in tasks:
                task_listbox.insert(END, task.strip())

    except FileNotFoundError:
        pass


def submit():
    task = entry.get()

    if task != "":
        task_listbox.insert(END, task)
        entry.delete(0, END)
        save_tasks()


def delete_task():
    task_listbox.delete(ANCHOR)
    save_tasks()


def complete_task():
    selected = task_listbox.curselection()

    if selected:
        index = selected[0]
        task = task_listbox.get(index)

        if not task.startswith("✔ "):
            task_listbox.delete(index)
            task_listbox.insert(index, "✔ " + task)

            task_listbox.itemconfig(index, fg="gray")

        save_tasks()


# ---------------- UI ---------------- #




entry = Entry(
    window,
    font=("Arial", 30),
    fg="black",
    bg="white",
    width=30
)
entry.pack(pady=10)


submit_button = Button(
    window,
    text="Add Task",
    command=submit,
    font=("Arial", 20),
    fg="black",
    bg="#1E90FF"
)
submit_button.pack(pady=10)


task_listbox = Listbox(
    window,
    font=("Arial", 20),
    bg="white",
    fg="black",
    width=50,
    height=10
)
task_listbox.pack(pady=20)


delete_button = Button(
    window,
    text="Delete Task",
    command=delete_task,
    font=("Arial", 20),
    fg="black",
    bg="#FF6347"
)
delete_button.pack(pady=10)


complete_button = Button(
    window,
    text="Complete Task",
    command=complete_task,
    font=("Arial", 20),
    fg="black",
    bg="#32CD32"
)
complete_button.pack(pady=10)

save_button = Button(
    window,
    text="Save Tasks",
    command=save_tasks,
    font=("Arial", 20),
    fg="black",
    bg="#FFD700"
)

save_button.pack(pady=10)


# ---------------- STARTUP LOAD ---------------- #

load_tasks()

window.mainloop()