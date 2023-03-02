import datetime
from tkinter import *
import json
from tkinter import messagebox
def display_expired_medicines():
    with open("data\medicine_stock.json", "r") as read_it:
        medicine_stock = json.load(read_it)
    expiredMedicines={}
    for medicine_id in medicine_stock:
        expiry_date_list = medicine_stock[medicine_id]["expiry date"].split("-")
        expiry_date = datetime.datetime(int(expiry_date_list[0]), int(
            expiry_date_list[1]), int(expiry_date_list[2]))
        current_time = datetime.datetime.now()
        today = datetime.datetime(
            current_time.year, current_time.month, current_time.day)
        if today > expiry_date:
            key=medicine_stock[medicine_id]["expiry date"]
            value=[medicine_id,medicine_stock[medicine_id]["name"],medicine_stock[medicine_id]["bin no"]]
            expiredMedicines[medicine_id]=medicine_stock[medicine_id]
    
    if len(expiredMedicines) > 0:
        headings = ["MEDICINE ID", "MEDICINE NAME", "BIN NUMBER"]
        row_headings = ["name", "bin no"]

        class Table:
            def __init__(self, root):
                for column_no in range(total_columns):
                    self.e = Entry(root, width=23, justify="center", fg='black',
                                   bg='DodgerBlue2', font=('Arial', 12, 'bold'))
                    self.e.grid(row=0, column=column_no)
                    self.e.insert(END, headings[column_no])
                row_no=1
                for medicine_id in expiredMedicines:
                    for column_no in range(total_columns):
                        self.e = Entry(root, width=17, justify="center",
                                       fg='black', bg='LightSkyBlue1', font=('Arial', 16, 'bold'))
                        self.e.grid(row=row_no, column=column_no)
                        if column_no == 0:
                            self.e.insert(END, medicine_id)
                        elif column_no ==1:
                            self.e.insert(END,expiredMedicines[medicine_id]["name"])
                        else:
                            self.e.insert(END, expiredMedicines[medicine_id]["bin no"])
                    row_no+=1
                self.e = Entry(root, width=32, justify="center",
                               fg='red', bg='gainsboro', font=('Arial', 16, 'bold'))
                self.e.grid(row=total_rows+1, column=1)
                self.e.insert(END, "Remove expired medicines from bins")
        total_rows = len(expiredMedicines)
        total_columns = 3
        root = Tk()
        root.title('WESTLAKE PHARMACY EXPIRED MEDICINES')
        root.configure(bg="gainsboro")
        t = Table(root)
        root.mainloop()
    else:
        messagebox.showinfo("Expired medicines review", "No expired medicines present in stock")
#display_expired_medicines()
