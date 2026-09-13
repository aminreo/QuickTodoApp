import json
from tkinter import *
from tkinter import ttk

root = Tk(className="Welcome to the Todo App!")

main_frame = ttk.Frame(root,padding=10)
main_frame.grid()

ttk.Button(main_frame, text="add",command= lambda : addTodoWindow()).grid(column=0, row=0)

frm = ttk.Frame(main_frame, padding=10)
frm.grid()
def saveNewTodo():
     #todo
     return

def addTodoWindow():
     addTodoWindow_frame = Toplevel(padx=10,pady=10)
    #  addTodoWindow_frame.grid()
     ttk.Label(addTodoWindow_frame,text="add new habit").pack()
    #  .grid(column=0,row=0)
    #  entry=
     ttk.Entry(addTodoWindow_frame,textvariable="a").pack()
     ttk.Button(addTodoWindow_frame,text="save",command= lambda: saveNewTodo()).pack()

    #  entry.grid(column=0,row=1)
     return

def done(s):
    for todo in testing_list:
        if todo.get("id") == s:
            todo["done"]=True
    render()
            
def render():
    empty_list=True
    for item in frm.winfo_children():
        item.destroy()

    for i,todo in enumerate(testing_list):
                if todo.get("done") == True:
                    continue
                ttk.Label(frm, text=todo.get("name")).grid(column=0, row=i)
                todo_id=todo.get("id")
                ttk.Button(frm, text="done",command=lambda : done(todo_id)).grid(column=1, row=i)
                empty_list=False
    if empty_list:
            ttk.Label(frm, text="empty").grid(column=0, row=1)

    root.mainloop()

try:
    with open ("text.json","r") as file:
        json.load(file)
except json.JSONDecodeError: 
    with open ("text.json","w") as file:
        file.write("[]")

testing_list = [{"id":111,"name":"1","done":False},{"id":112,"name":"2","done":False},{"id":113,"name":"3","done":True}]

render()
