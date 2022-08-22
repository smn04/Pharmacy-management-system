from tkinter import *
import tkinter.messagebox
from functools import partial
#function to generate annual sales report
def report_gen_annual():
    f = open('reportdata.txt', 'r')
    content = f.read().split()
    years = {}
    for i in range(0, len(content), 2):
        year = content[i].split('-')[0]
        if year not in years:
            years[year] = int(content[i+1])
        else:
            years[year] += int(content[i+1])
    import matplotlib.pyplot as plt
    plt.plot(years.keys(), years.values())
    plt.title("ANNUAL SALES REPORT")

    plt.ylabel("Sales in rupees")
    plt.xlabel("Years")
    plt.show()
# report_gen_annual()
#function to generate monthwise report of a given year

def report_gen_monthly():
    f = open('reportdata.txt', 'r')
    tkWindow1 = tkinter.Toplevel()
    tkWindow1.geometry('1200x1200')
    tkWindow1.title("MONTHLY REPORT GENERATION")
    tkWindow1.configure(bg="sky blue")
    photo = PhotoImage(file = "image.png")
    tkWindow1.iconphoto(False, photo)
    def check_year(year):
        year_input=year.get()
        invalid_year=False
        for i in year_input:
            if not i.isdigit():
                invalid_year=True
        if not invalid_year and len(year_input) == 4 and 2023 > int(year_input) > 2014:
            content = f.read().split()
            months = {}
            monthsnames = {'01': 'January', '02': 'Februrary', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                                '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
            for i in range(0, len(content), 2):
                line = content[i].split("-")
                year = line[0]
                if year == year_input:
                    month = line[1]
                    monthname = monthsnames[month]
                    if monthname not in months:
                        months[monthname] = int(content[i+1])
                    else:
                        months[monthname] += int(content[i+1])
            import matplotlib.pyplot as plt
            plt.plot(months.keys(), months.values())
            plt.title(f"SALES REPORT FOR {year_input}")
            plt.ylabel("Sales in rupees")
            plt.xlabel("Months")
            plt.show()
        else:
            from tkinter import messagebox
            messagebox.showerror("WESTLAKE PHARMACY MONTHLY REPORT INPUT ERROR", "Invalid year entered")
            return
    Label(tkWindow1,text="VIEW MONTH-WISE SALES REPORT", bg="sky blue", width="50", height="2", font=("Calibri", 40)).pack()
    Label(tkWindow1,text="",bg="sky blue").pack()
    Label(tkWindow1,text="",bg="sky blue").pack()
    yearLabel = tkinter.Label(tkWindow1, text="Enter the year to see its monthly sales report", font=("Calibri", 20),bg="DodgerBlue2").pack()
    year = tkinter.StringVar()
    Label(tkWindow1,text="",bg="sky blue").pack()
    Label(tkWindow1,text="",bg="sky blue").pack()
    yearEntry = tkinter.Entry(tkWindow1, textvariable=year,font=("Calibri", 20)).pack()
    Label(tkWindow1,text="",bg="sky blue").pack()
    Label(tkWindow1,text="",bg="sky blue").pack()
    check_year=partial(check_year, year)
    loginButton = tkinter.Button(tkWindow1, text="View Report",command=check_year).pack()
    tkWindow1.mainloop()
            
#report_gen_monthly()


#function to generate daily report of given month in given year
def report_gen_daily():
    f = open('reportdata.txt', 'r')
    tkWindow1 = tkinter.Toplevel()
    tkWindow1.geometry('1200x1200')
    tkWindow1.title("DAY-WISE REPORT GENERATION")
    tkWindow1.configure(bg="sky blue")
    photo = PhotoImage(file = "image.png")
    tkWindow1.iconphoto(False, photo)
    def check_year_and_month(year,month):
        year_input=year.get()
        month_input=month.get()
        invalid_year=False
        for i in year_input:
            if not i.isdigit():
                invalid_year=True
        if not invalid_year and len(year_input) == 4 and 2023 > int(year_input) > 2014:
            content = f.read().split()
            monthsnames = {'01': 'january', '02': 'februrary', '03': 'march', '04': 'april', '05': 'may', '06': 'june','07': 'july', '08': 'august', '09': 'september', '10': 'october', '11': 'november', '12': 'december'}
            if month_input.lower() in monthsnames.values():
                dates = {}
                for i in range(0, len(content), 2):
                    line = content[i].split('-')
                    year = line[0]
                    if year == year_input:
                        month = monthsnames[line[1]]
                        if month_input.lower() == month:
                            date = line[2]
                            if date not in dates:
                                dates[date] = int(content[i+1])
                            else:
                                dates[date] += int(content[i+1])
                import matplotlib.pyplot as plt
                plt.plot(dates.keys(), dates.values())
                plt.title(f"SALES REPORT FOR {month_input.upper()} of {year_input}")

                plt.ylabel("Sales in rupees")
                plt.xlabel("Days")
                plt.show()
            else:
                from tkinter import messagebox
                messagebox.showerror("WESTLAKE PHARMACY DAILY REPORT INPUT ERROR", "Invalid month entered")
                return
        else:
            from tkinter import messagebox
            messagebox.showerror("WESTLAKE PHARMACY DAILY REPORT INPUT ERROR", "Invalid year entered")
            return
    Label(tkWindow1,text="VIEW DAY-WISE SALES REPORT", bg="sky blue", width="50", height="2", font=("Calibri", 40)).pack()
    Label(tkWindow1,text="",bg="sky blue").pack()
    Label(tkWindow1,text="",bg="sky blue").pack()
    yearLabel = tkinter.Label(tkWindow1, text="Enter the year to see its monthly sales report", font=("Calibri", 20),bg="DodgerBlue2").pack()
    year = tkinter.StringVar()
    yearEntry = tkinter.Entry(tkWindow1, textvariable=year,font=("Calibri", 20)).pack()
    Label(tkWindow1,text="",bg="sky blue").pack()
    Label(tkWindow1,text="",bg="sky blue").pack()
    monthLabel = tkinter.Label(tkWindow1, font=("Calibri", 20),text="Enter the month to see its monthly sales report", bg="DodgerBlue2").pack()
    month = tkinter.StringVar()
    monthEntry = tkinter.Entry(tkWindow1, textvariable=month,font=("Calibri", 20)).pack()
    Label(tkWindow1,text="",bg="sky blue").pack()
    Label(tkWindow1,text="",bg="sky blue").pack()
    check_year_and_month=partial(check_year_and_month, year,month)
    generatereportButton = tkinter.Button(tkWindow1, text="View Report",font=("Calibri", 15),command=check_year_and_month).pack()
    tkWindow1.mainloop()
#report_gen_daily()


