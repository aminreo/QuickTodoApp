import json
from tkinter import *
from tkinter import ttk
import uuid

def addTodoWindow():
     addTodoWindow_frame = Toplevel(padx=10,pady=10)
    #  addTodoWindow_frame.grid()
     ttk.Label(addTodoWindow_frame,text="add new habit").pack()
    #  .grid(column=0,row=0)
     entry= ttk.Entry(addTodoWindow_frame,textvariable=new_habit_var)
    #  entry.bind("<Return>",lambda e : saveNewTodo(new_habit_var.get()))
     entry.pack()
     ttk.Button(addTodoWindow_frame,text="save",command= lambda: saveNewTodo(new_habit_var.get())).pack()

    #  entry.grid(column=0,row=1)
     return
def save_to_json():
     with open ("text.json","w") as file:
             # file.write("[]")
             json.dump((habits_list_tmp),fp=file)

root = Tk(className="Welcome to the Todo App!")
new_habit_var = StringVar(value="")
main_frame = ttk.Frame(root,padding=10)
main_frame.grid()

ttk.Button(main_frame, text="add",command= addTodoWindow).grid(column=0, row=0)

frm = ttk.Frame(main_frame, padding=10)
frm.grid()
def saveNewTodo(s):
     #todo
     if not s:
          print("invalid input")
          return
     print(s)
     new_id= str(uuid.uuid4())
     habits_list_tmp.append({"id":new_id, "name":s,"done":False})
     save_to_json()
     render()
     return


def done(s):
    # print(f"id {s}")
    for todo in habits_list_tmp:
        if todo.get("id") == s:
            todo["done"]=True
    save_to_json()
    render()
            
def render():
    empty_list=True
    for item in frm.winfo_children():
        item.destroy()

    for i,todo in enumerate(habits_list_tmp):
                if todo.get("done") == True:
                    continue
                ttk.Label(frm, text=todo.get("name")).grid(column=0, row=i)
                todo_id=todo.get("id")
                ttk.Button(frm, text="completed",command=lambda id=todo_id : done(id)).grid(column=1, row=i)
                empty_list=False
    if empty_list:
            ttk.Label(frm, text="empty").grid(column=0, row=1)

    

# habits_list_tmp = [{"id":str(uuid.uuid4()),"name":"1","done":False},{"id":str(uuid.uuid4()),"name":"2","done":False},{"id":str(uuid.uuid4()),"name":"3","done":True}]

try:
    with open("text.json","r") as file:
        habits_list_tmp= json.load(file)
except (json.JSONDecodeError,FileNotFoundError): 
    habits_list_tmp=[]
    save_to_json()


render()
root.mainloop()
# json.dump(habits_list_tmp,fp=file)
