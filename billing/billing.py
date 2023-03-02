from tkinter import *
import json
from tkinter import messagebox
from functools import partial
from tkinter import ttk
from turtle import bgcolor
order = {}
total=0
def Billing():
    window = Toplevel()
    window.geometry("1200x1200")
    window.configure(bg="sky blue")
    photo = PhotoImage(file = "image.png")
    window.iconphoto(False, photo)
    Label(window,text="WESTLAKE PHARMACY BILLING", bg="sky blue", height="2", font=("Calibri", 20,"bold")).grid(row=0,column=4)
    separator = ttk.Separator(window,orient='horizontal').grid(row=1,)    
    nameLabel = Label(window,text=" Customer Name ",font=("Calibri",15),bg="DodgerBlue2").grid(column=0, row=1, sticky=W, padx=5, pady=5)
    name = StringVar()
    nameEntry = Entry(window,font=("Calibri",15),textvariable=name).grid(column=1, row=1, sticky=W, padx=5, pady=5)
    contactLabel = Label(window,text=" Customer Contact Number ",font=("Calibri",15),bg="DodgerBlue2").grid(column=5, row=1,)
    contactno = StringVar()
    contactEntry = Entry(window,font=("Calibri",15),textvariable=contactno).grid(column=6, row=1,)
    Label(window,text="",bg="sky blue").grid()
    Label(window,text="",bg="sky blue").grid()
    Label(window,text="Enter the order below:",bg="sky blue",font=("Calibri",15)).grid()
    medicineidLabel = Label(window,text=" MEDICINE ID ",font=("Calibri",15,"bold"),bg="DodgerBlue2").grid(column=0, row=6,sticky=W, padx=5, pady=5)
    medicineid = StringVar()
    medicineidEntry = Entry(window,font=("Calibri",15),textvariable=medicineid)
    medicineidEntry.grid(column=1,row=6, sticky=W, padx=5, pady=5)
    Label(window,text="",bg="sky blue").grid()
    Label(window,text="",bg="sky blue").grid()
    quantityLabel = Label(window,text=" QUANTITY ",font=("Calibri",15,"bold"),bg="DodgerBlue2").grid(column=0, row=9,sticky=W, padx=5, pady=5)
    Quantity=StringVar()
    quantityEntry = Entry(window,font=("Calibri",15),textvariable=Quantity)
    quantityEntry.grid(column=1, row=9, sticky=W, padx=5, pady=5)
    Label(window,text="",bg="sky blue").grid()
    Label(window,text="",bg="sky blue").grid()
    def reset(txt):
        quantityEntry.delete(0,END)
        quantityEntry.insert(0,txt)
        medicineidEntry.delete(0,END)
        medicineidEntry.insert(0,txt)
    def next(medicineid,Quantity):
        medicine_id=medicineid.get()
        quantity=Quantity.get()
        reset("")
        global order
        global total
        import datetime
        with open("data\medicine_stock.json", "r") as read_it:
            medicine_stock = json.load(read_it)
        if medicine_id not in medicine_stock:
            messagebox.showerror("WESTLAKE PHARMACY BILLING ERROR", "INVALID MEDICINE ID")
        else:
            if quantity.isdigit():
                if medicine_stock[medicine_id]["quantity"] >= int(quantity):
                    expiry_date_list = medicine_stock[medicine_id]["expiry date"].split("-")
                    expiry_date = datetime.datetime(int(expiry_date_list[0]), int(expiry_date_list[1]), int(expiry_date_list[2]))
                    current_time = datetime.datetime.now()
                    today = datetime.datetime(
                        current_time.year, current_time.month, current_time.day)
                    if today < expiry_date:
                        if medicine_id not in order:
                            order[medicine_id] = int(quantity)
                        else:
                            order[medicine_id]+=int(quantity)
                        total += medicine_stock[medicine_id]["cost"]*int(quantity)
                        medicine_stock[medicine_id]["quantity"] -= int(quantity)
                        with open("data\medicine_stock.json", "w") as p:
                            json.dump(medicine_stock, p)
                        bin_no=medicine_stock[medicine_id]["bin no"]
                        messagebox.showinfo("WESTLAKE PHARMACY BILLING ERROR",f"Medicine available in {bin_no} bin no")
                    else:
                        messagebox.showerror("WESTLAKE PHARMACY BILLING ERROR", "Expired medicine not available for sale")
                else:
                    temp=medicine_stock[medicine_id]["quantity"]
                    messagebox.showerror("WESTLAKE PHARMACY BILLING ERROR", f"Not enough stock available!\nOnly {temp} stock available")  
    Next=partial(next,medicineid,Quantity)
    nextButton = Button(window, text="Add more",font=("Calibri", 15),command=Next).grid(column=0, row=11,sticky=W, padx=5, pady=5)
    Label(window,text="",bg="sky blue").grid()
    Label(window,text="",bg="sky blue").grid()
    def total_billing(medicineid,Quantity):
        next(medicineid,Quantity)
        with open("data\medicine_stock.json", "r") as read_it:
            medicine_stock = json.load(read_it)
        global total
        with open("data\\report_data.json","r") as f:
            dates = json.load(f)
        from datetime import date
        today = date.today()
        if total!=0:
            if str(today) not in dates:
                dates[str(today)]=str(total)
            else:
                dates[str(today)]+=str(total)
            with open("data\\report_data.json","w") as f:
                json.dump(dates,f)
            headings = ["MEDICINE NAME", "QUANTITY", "COST PER UNIT", "AMOUNT"]
            row_headings = ["name", "quantity", "cost","amount"]

            class Table:
                def __init__(self, root):
                    self.e = Entry(root, width=25, justify="left", fg='black', font=('Arial', 12, 'bold'))
                    self.e.grid(row=0, column=0)
                    self.e.insert(END, f"Customer Name:{name.get()}")
                    self.e = Entry(root, width=25, justify="left", fg='black', font=('Arial', 12, 'bold'))
                    self.e.grid(row=0, column=3)
                    self.e.insert(END, f"Customer No:{contactno.get()}")
                    for j in range(0, total_columns):
                        self.e = Entry(root, width=20, justify="center", fg='black',
                                    bg='darkorange', font=('Arial', 12, 'bold'))
                        self.e.grid(row=2, column=j)
                        self.e.insert(END, headings[j])
                    for index,i in enumerate(order):
                        for j in range(0, total_columns):
                            self.e = Entry(root, width=17, justify="center",
                                        fg='black', bg='tan', font=('Arial', 16, 'bold'))
                            self.e.grid(row=index+3, column=j)
                            if j == 3:
                                self.e.insert(END, str(medicine_stock[i]["cost"]*order[i]))
                            elif j == 1:
                                self.e.insert(END, order[i])
                            else:
                                self.e.insert(END, str(medicine_stock[i][row_headings[j]]))
                    self.e = Entry(root, width=17, justify="center",
                                fg='white', bg='red', font=('Arial', 16, 'bold'))
                    self.e.grid(row=total_rows+3,column=3)
                    self.e.insert(END, f"Total ={total}")
            
            total_rows = len(order)
            total_columns = 4
        else:
            messagebox.showinfo("Billing", "No items added for billing")

        root = Toplevel(window)
        root.title('WESTLAKE PHARMACY BILL')
        t = Table(root)
        root.mainloop()
    Total=partial(total_billing,medicineid,Quantity)
    totalButton=Button(window, text="Total",font=("Calibri", 15),command=Total).grid(column=0, row=14,sticky=W, padx=5, pady=5)
    
    window.mainloop()
    
#Billing()