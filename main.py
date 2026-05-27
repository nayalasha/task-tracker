
from tkinter import *

window = Tk()
window.geometry("1920x1080")
window.title("Task Tracker")


# FUNCTION TO CHANGE BACKGROUND
# ---------------- FUNCTIONS ---------------- #
def change_mode(selected_color):
    window.config(background=selected_color)
    label.config(bg=selected_color)


# DEFAULT MODE
mode = "lightblue"

# VARIABLE
mode_var = StringVar(value=mode)


# SAVE TASKS
# ---------------- FUNCTIONS ---------------- #
def save_tasks():
    tasks = task_listbox.get(0, END)

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


# LOAD TASKS
# ---------------- FUNCTIONS ---------------- #
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            for task in tasks:
                task_listbox.insert(END, task.strip())

    except FileNotFoundError:
        pass


# ADD TASK
# ---------------- FUNCTIONS ---------------- #
def submit():
    task = entry.get()
    due_date = due_entry.get()
    priority = priority_var.get()

    if task != "":
        full_task = f"[{priority}] {task} | Due: {due_date}"

        task_listbox.insert(END, full_task)

        # COLOR CODE PRIORITIES
        index = task_listbox.size() - 1

        if priority == "High":
            task_listbox.itemconfig(index, fg="red")

        elif priority == "Medium":
            task_listbox.itemconfig(index, fg="orange")

        elif priority == "Low":
            task_listbox.itemconfig(index, fg="green")

        entry.delete(0, END)
        due_entry.delete(0, END)

        save_tasks()


# DELETE TASK
# ---------------- FUNCTIONS ---------------- #
def delete_task():
    task_listbox.delete(ANCHOR)
    save_tasks()


# COMPLETE TASK
# ---------------- FUNCTIONS ---------------- #
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

# LABEL
label = Label(
    window,
    text="Task Tracker",
    font=("Arial", 40, "bold"),
    bg=mode
)

label.pack(pady=20)


# DROPDOWN MENU FOR BACKGROUND
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


# TASK ENTRY
entry = Entry(
    window,
    font=("Arial", 30),
    fg="black",
    bg="white",
    width=30
)
entry.pack(pady=10)


# DUE DATE ENTRY
due_entry = Entry(
    window,
    font=("Arial", 20),
    fg="black",
    bg="white",
    width=25
)

due_entry.insert(0, "YYYY-MM-DD")
due_entry.pack(pady=5)


# PRIORITY DROPDOWN
priority_var = StringVar()
priority_var.set("Medium")

priority_menu = OptionMenu(
    window,
    priority_var,
    "Low",
    "Medium",
    "High"
)

priority_menu.config(
    font=("Arial", 12),
    bg="white",
    fg="black"
)

priority_menu.pack(pady=5)


# ADD TASK BUTTON
submit_button = Button(
    window,
    text="Add Task",
    command=submit,
    font=("Arial", 20),
    fg="black",
    bg="#1E90FF"
)
submit_button.pack(pady=10)


# TASK LISTBOX
task_listbox = Listbox(
    window,
    font=("Arial", 20),
    bg="white",
    fg="black",
    width=60,
    height=12
)

task_listbox.pack(pady=20)


# DELETE BUTTON
delete_button = Button(
    window,
    text="Delete Task",
    command=delete_task,
    font=("Arial", 20),
    fg="black",
    bg="#FF6347"
)

delete_button.pack(pady=10)


# COMPLETE BUTTON
complete_button = Button(
    window,
    text="Complete Task",
    command=complete_task,
    font=("Arial", 20),
    fg="black",
    bg="#32CD32"
)

complete_button.pack(pady=10)


# SAVE BUTTON
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

