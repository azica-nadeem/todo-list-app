from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Colorful To-Do List")
root.geometry("500x600")
root.configure(bg="#F5EFFF")

# Functions
def add_task():
    task = task_entry.get()

    if task.strip() == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        task_listbox.insert(END, "✔ " + task)
        task_entry.delete(0, END)

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

# Heading
title = Label(
    root,
    text="📝 My To-Do List",
    font=("Arial", 24, "bold"),
    bg="#F5EFFF",
    fg="#6A0DAD"
)
title.pack(pady=20)

# Entry Frame
entry_frame = Frame(root, bg="#F5EFFF")
entry_frame.pack(pady=10)

task_entry = Entry(
    entry_frame,
    width=25,
    font=("Arial", 14),
    bd=3
)
task_entry.grid(row=0, column=0, padx=5)

add_btn = Button(
    entry_frame,
    text="Add",
    font=("Arial", 12, "bold"),
    bg="#7ED957",
    fg="white",
    padx=10,
    command=add_task
)
add_btn.grid(row=0, column=1)

# Listbox
task_listbox = Listbox(
    root,
    width=40,
    height=15,
    font=("Arial", 13),
    bg="white",
    fg="#333333",
    selectbackground="#FF69B4",
    bd=3
)
task_listbox.pack(pady=20)

# Buttons Frame
btn_frame = Frame(root, bg="#F5EFFF")
btn_frame.pack()

delete_btn = Button(
    btn_frame,
    text="🗑 Delete",
    font=("Arial", 12, "bold"),
    bg="#FF4D6D",
    fg="white",
    padx=15,
    command=delete_task
)
delete_btn.grid(row=0, column=0, padx=10)

exit_btn = Button(
    btn_frame,
    text="❌ Exit",
    font=("Arial", 12, "bold"),
    bg="#4D96FF",
    fg="white",
    padx=15,
    command=root.destroy
)
exit_btn.grid(row=0, column=1, padx=10)

# Footer
footer = Label(
    root,
    text="Stay Organized ✨",
    font=("Arial", 11, "italic"),
    bg="#F5EFFF",
    fg="#777777"
)
footer.pack(side=BOTTOM, pady=15)

root.mainloop()