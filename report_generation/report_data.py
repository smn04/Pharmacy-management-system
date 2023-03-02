from tkinter import *
import tkinter.messagebox
from functools import partial
import json

def report_gen_annual():#function to generate annual sales report
    with open("data\\report_data.json","r") as f:
        dates = json.load(f)
    years={}
    for date in dates:
        year = date.split('-')[0]
        years[year]=dates[date]
    import matplotlib.pyplot as plt
    plt.plot(years.keys(), years.values())
    plt.title("ANNUAL SALES REPORT")
    plt.ylabel("Sales in rupees")
    plt.xlabel("Years")
    plt.show()
#report_gen_annual()


def report_gen_monthly():#function to generate monthwise report of a given year
    with open("data\\report_data.json","r") as f:
        dates = json.load(f)
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
        import json
        from datetime import date
        if not invalid_year and len(year_input) == 4 and date.today().year >= int(year_input) > 2014:#existing data available only from 2015 onwards
            months = {}
            monthsnames = {'01': 'January', '02': 'Februrary', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                                '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
            for date in dates:
                date_temp=date.split('-')
                year = date_temp[0]
                if year == year_input:
                    month = date_temp[1]
                    monthname = monthsnames[month]
                    if monthname not in months:
                        months[monthname] = int(dates[date])
                    else:
                        months[monthname] += int(dates[date])
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



def report_gen_daily():#function to generate daily report of given month in given year
    with open("data\\report_data.json","r") as f:
        dates = json.load(f)
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
        from datetime import date
        if not invalid_year and len(year_input) == 4 and date.today().year >= int(year_input) > 2014:#exisiting data is available only from 2015 onwards
            daily_sales={}
            monthsnames = {'01': 'january', '02': 'februrary', '03': 'march', '04': 'april', '05': 'may', '06': 'june','07': 'july', '08': 'august', '09': 'september', '10': 'october', '11': 'november', '12': 'december'}
            if month_input.lower() in monthsnames.values():
                for date in dates:
                    date_temp=date.split('-')
                    year = date_temp[0]
                    if year == year_input:
                        month = monthsnames[date_temp[1]]
                        if month_input.lower() == month:
                            date_check = date_temp[2]
                            if date_check not in daily_sales:
                                daily_sales[date_check] = int(dates[date])
                            else:
                                daily_sales[date_check] += int(dates[date])
                import matplotlib.pyplot as plt
                plt.plot(daily_sales.keys(), daily_sales.values())
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


