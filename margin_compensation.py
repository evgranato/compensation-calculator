# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()

# def calculator(cost, margin):
#     answer = round(int(cost) / (1 - int(margin)/100), 2)
#     compensation = round((answer-int(cost)) * .20, 2)
#     return f"The quoted price should be ${answer} and your compensation will be ${compensation}"

# cost = input("What's the cost of the product?  ")
# margin = input("What's the margin?  ") 

# print(calculator(cost, margin))
import tkinter as tk

master = tk.Tk()
tk.Label(master, text="Enter Cost of Product").grid(row=0)
tk.Label(master, text="What's the margin").grid(row=1)
tk.Label(master, text="                                                                                    ").grid(row=2)

def calculator():
    answer = round(int(e1.get()) / (1 - int(e2.get())/100), 2)
    compensation = round((answer-int(e1.get())) * .20, 2)
    e3 = (f"The quoted price should be ${answer} and your compensation will be ${compensation}")
    tk.Label(master, text=e3).grid(row=3)
    
def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=5, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Result', command=calculator).grid(row=5, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.mainloop()