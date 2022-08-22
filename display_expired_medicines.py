import datetime
from tkinter import *
import json
from tkinter import messagebox
def display_expired_medicines():
    with open("medicine_stock.json", "r") as read_it:
        medicine_stock = json.load(read_it)
    from heap import HeapPriorityQueue
    expiredMedicines=HeapPriorityQueue()
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
            expiredMedicines.add(key, value)
    
    if len(expiredMedicines) > 0:
        headings = ["MEDICINE ID", "MEDICINE NAME", "BIN NUMBER"]
        row_headings = ["name", "bin no"]

        class Table:
            def __init__(self, root):
                for j in range(total_columns):
                    self.e = Entry(root, width=23, justify="center", fg='black',
                                   bg='DodgerBlue2', font=('Arial', 12, 'bold'))
                    self.e.grid(row=0, column=j)
                    self.e.insert(END, headings[j])
                for i in range(1,total_rows+1):
                    key,value=expiredMedicines.remove_min()
                    for j in range(total_columns):
                        self.e = Entry(root, width=17, justify="center",
                                       fg='black', bg='LightSkyBlue1', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        if j == 0:
                            self.e.insert(END, value[0])
                        else:
                            self.e.insert(END, value[j])
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
