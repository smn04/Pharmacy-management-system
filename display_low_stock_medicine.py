from tkinter import *
import json
from tkinter import messagebox


def display_low_stock_medicines():
    with open("medicine_stock.json", "r") as read_it:
        medicine_stock = json.load(read_it)
    low_stock_medicines = []
    for medicine_id in medicine_stock:
        if medicine_stock[medicine_id]["quantity"] <= 5:
            low_stock_medicines.append(medicine_id)
    if len(low_stock_medicines) > 0:
        headings = ["MEDICINE ID", "MEDICINE NAME", "QUANTITY"]
        row_headings = ["name", "quantity"]

        class Table:
            def __init__(self, root):
                for j in range(0, total_columns):
                    self.e = Entry(root, width=23, justify="center", fg='black',
                                   bg='DodgerBlue2', font=('Arial', 12, 'bold'))
                    self.e.grid(row=0, column=j)
                    self.e.insert(END, headings[j])
                for i in range(0, total_rows):
                    for j in range(0, total_columns):
                        self.e = Entry(root, justify="center", width=17,
                                       fg='black', bg='LightSkyBlue1', font=('Arial', 16, 'bold'))
                        self.e.grid(row=i+1, column=j)
                        if j == 0:
                            self.e.insert(END, low_stock_medicines[i])
                        else:
                            self.e.insert(
                                END, medicine_stock[low_stock_medicines[i]][row_headings[j-1]])
                self.e = Entry(root, width=25, justify="center",
                               fg='red', bg='gainsboro', font=('Arial', 16, 'bold'))
                self.e.grid(row=total_rows+1, column=1)
                self.e.insert(END, "Restock the above medicines soon")

        total_rows = len(low_stock_medicines)
        total_columns = 3
        root = Tk()
        root.title('WESTLAKE PHARMACY LOW STOCK MEDICINES')
        root.configure(bg="gainsboro")

        t = Table(root)
        root.mainloop()
    else:
        messagebox.showinfo("Low stock medicines review","No low stock medicines present in stock")


#display_low_stock_medicines()
