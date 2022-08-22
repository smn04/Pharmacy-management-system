from tkinter import *
import json


def display_stock():
    with open("medicine_stock.json", "r") as read_it:
        medicine_stock = json.load(read_it)
    headings = ["MEDICINE ID", "MEDICINE NAME",
                "QUANTITY", "BIN NUMBER", "EXPIRY DATE", "COST"]
    row_headings = ["name", "quantity", "bin no", "expiry date", "cost"]
    medicine_ids = [id for id in medicine_stock]

    class Table:
        def __init__(self, root):
            for j in range(0, total_columns):
                self.e = Entry(root, width=20, justify="center", fg='black',
                               bg='DodgerBlue2', font=('Arial', 12, 'bold'))
                self.e.grid(row=0, column=j)
                self.e.insert(END, headings[j])
            for i in range(0, total_rows):
                for j in range(0, total_columns):
                    self.e = Entry(root, justify="center", width=15,
                                   fg='black', bg='LightSkyBlue1', font=('Arial', 16, 'bold'))
                    self.e.grid(row=i+1, column=j)
                    if j == 0:
                        self.e.insert(END, medicine_ids[i])
                    else:
                        self.e.insert(
                            END, medicine_stock[medicine_ids[i]][row_headings[j-1]])
    total_rows = len(medicine_stock)
    total_columns = 6
    root = Tk()
    root.title('WESTLAKE PHARMACY STOCK DISPLAY')
    root.configure(bg="gainsboro")
    t = Table(root)
    root.mainloop()


#display_stock()
