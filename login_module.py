from tkinter import *
from functools import partial
import tkinter.messagebox
import datastructure
stack1 = datastructure.Stack()
#function to get all saved login_details saved in system
def read_saved_login_details():
    file1 = open("login_details.txt", "r+")
    saved_login_details_draft = file1.read().split()
    for i in range(0, len(saved_login_details_draft), 2):
        curr_login = {}
        username = saved_login_details_draft[i]
        password = saved_login_details_draft[i+1]
        curr_login[username] = password
        stack1.push(curr_login)
    file1.close()

#function to login to Westlake pharmacy 
def login():
    def openMenuWindow():
        newWindow = Toplevel()
        newWindow.title("WESTLAKE PHARMACY MENU")
        newWindow.geometry("1200x800")
        newWindow.configure(bg="sky blue")
        photo = PhotoImage(file = "image.png")
        newWindow.iconphoto(False, photo)
        
        
        Label(newWindow,text="Welcome to Westlake Pharmacy", bg="sky blue", height="2", font=("Calibri", 20,"bold")).pack()
        import billing
        BillingButton = Button(newWindow, text="Billing",command=billing.Billing,font=("Calibri",13,"bold")).pack()
        Label(newWindow,text="",bg="sky blue").pack()
        import display_expired_medicines as ex
        Label(newWindow,text="",bg="sky blue").pack()
        DisplayExpiredButton = Button(
            newWindow, text="Veiw Expired Medicines", command=ex.display_expired_medicines,font=("Calibri",13,"bold")).pack()
        Label(newWindow,text="",bg="sky blue").pack()
        Label(newWindow,text="",bg="sky blue").pack()
        import display_low_stock_medicine as low
        DisplayLowStockButton = Button(
            newWindow, text="Veiw Low Stock Medicines", command=low.display_low_stock_medicines,font=("Calibri",13,"bold")).pack()
        Label(newWindow,text="",bg="sky blue").pack()
        Label(newWindow,text="",bg="sky blue").pack()
        import display_stock as display
        DisplayStock = Button(
            newWindow, text="Display Current Stock", command=display.display_stock,font=("Calibri",13,"bold")).pack()
        Label(newWindow,text="",bg="sky blue").pack()
        Label(newWindow,text="",bg="sky blue").pack()
        import report_data
        DisplayAnnualSales = Button(newWindow, text="Display Annual Sales Report",font=("Calibri",13,"bold"), command=report_data.report_gen_annual).pack()
        Label(newWindow,text="",bg="sky blue").pack()
        Label(newWindow,text="",bg="sky blue").pack()
        DisplayMonthlySales = Button(newWindow, text="Display Month-wise Report",font=("Calibri",13,"bold"), command=report_data.report_gen_monthly).pack()
        Label(newWindow,text="",bg="sky blue").pack()
        Label(newWindow,text="",bg="sky blue").pack()
        DisplayAnnualSales = Button(
            newWindow, text="Display Day-wise Report",font=("Calibri",13,"bold"), command=report_data.report_gen_daily).pack()
        Label(newWindow,text="",bg="sky blue").pack()
        Label(newWindow,text="",bg="sky blue").pack()
    def validateLogin(username, password):
        username_entered = username.get()
        password_entered = password.get()
        read_saved_login_details()
        saved_login_usernames = [username for data in stack1.data for username in data]
        n=len(stack1)
        res="INALID USERNAME"
        for i in range(n):
            check=stack1.pop()
            check_username=list(check.keys())[0]
            check_password=check[check_username]
            if str(check_username) == username_entered:
                if check_password == password_entered:
                    res="LOGIN SUCCESSFUL"
                    break
                else:
                    res = "INCORRECT PASSWORD"
        print(res)
        if res == "LOGIN SUCCESSFUL":
            openMenuWindow()
        else:
            tkinter.messagebox.showinfo("LOGIN", res)

    tkWindow = Tk()
    tkWindow.geometry('1400x1200')
    tkWindow.title('WESTLAKE PHARMACY LOGIN PORTAL')
    photo = PhotoImage(file = "image.png")
    tkWindow.iconphoto(False, photo)
    img = PhotoImage(file='800533.png')
    label17 = Label(tkWindow, image=img)
    label17.place(x=0, y=0)
    Label(text="WESTLAKE PHARMACY STAFF LOGIN PAGE", width="50", height="2", font=("Questrial", 35,"bold"),bg="LightBlue2").grid(padx=0)
    usernameLabel = Label(tkWindow, width="25",text=" User Name ",font=("Calibri",15),
                          bg="DodgerBlue2").grid(padx=4,pady=20)
    username = StringVar()
    usernameEntry = Entry(
        tkWindow, width="25",font=("Calibri",15),textvariable=username).grid(padx=4,pady=25)
    passwordLabel = Label(tkWindow, width="25",text=" Password  ",font=("Calibri",15),
                          bg="DodgerBlue2").grid(padx=6,pady=20)
    password = StringVar()
    passwordEntry = Entry(tkWindow, width="25",textvariable=password,font=("Calibri",15),
                          show='*').grid(padx=6,pady=25)

    validateLogin = partial(validateLogin, username, password)
    loginButton = Button(tkWindow, text="Login",font=("Calibri", 20,"bold"),
                         command=validateLogin,bg="snow3").grid(padx=10)
    

    def openNewWindow():
        def validate_password(password):
            num_count = 0
            char_count = 0
            for i in password:
                if i.isdigit():
                    num_count += 1
                if i in ["@", "$", "!", "%", "_"]:
                    char_count += 1
            return len(password) >= 6 and len(password) <= 12 and num_count >= 1 and char_count >= 1

        def validate_username(username):
            for i in username:
                if not i.isalpha():
                    if i != "_":
                        return False
                if i.isalpha():
                    if i.isupper():
                        return False
            return True

        def validate_user_creation(username, password, repassword):
            username1 = username.get()
            repassword1 = repassword.get()
            password1 = password.get()
            res = "Registration failed"
            if password1 == repassword1:
                if validate_password(password1):
                    if validate_username(username1):
                        usernames = [
                            username for data in stack1.data for username in data]
                        if username1 not in usernames:
                            new_user = {}
                            file1 = open("login_details.txt", "a+")
                            file1.write("\n"+username1+" "+password1)
                            new_user[username1] = password1
                            stack1.push(new_user)
                            file1.close()
                            res = "Registration successful"
                        else:
                            res = "Username already exists!"
                    else:
                        res = "Invalid Username!"
                else:
                    res = "Invalid Password!"
            else:
                res = "Password not matching in both cases!"
            print(res)
            tkinter.messagebox.showinfo("NEW ACCOUNT CREATION STATUS", res)
        newWindow = Toplevel(tkWindow)
        newWindow.title("WESTLAKE PHARMACY NEW USER REGISTRATION")
        newWindow.geometry("1200x1200")
        newWindow.configure(bg="sky blue")
        photo = PhotoImage(file = "image.png")
        newWindow.iconphoto(False, photo)
        Label(newWindow,text="WESTLAKE PHARMACY STAFF NEW ACCOUNT CREATION PAGE", bg="sky blue", width="75", height="2", font=("Calibri", 25,"bold")).grid(padx=0)
        Label(newWindow, text="WESTLAKE STORE NEW USER REGISTRATION\nUsername should have only lowercase letters and underscore\nPassword should contain minimum 6 characters and maximum\n 12 characters with atleast 1 digit and 1 special character( @ , $ , ! , % , _ )", bg="snow3",font=("Calibri", 10)).grid(padx=1)
        usernameLabel1= Label(newWindow, width="25",text=" User Name ",font=("Calibri",15),
                          bg="DodgerBlue2").grid(padx=2,pady=20)
        username = StringVar()
        usernameEntry = Entry(newWindow, width="25",font=("Calibri",15),textvariable=username).grid(padx=2,pady=21)
        passwordLabel1= Label(newWindow, width="25",text=" Password ",font=("Calibri",15,),
                          bg="DodgerBlue2").grid(padx=4,pady=20)
        password = StringVar()
        passwordEntry = Entry(newWindow, width="25",font=("Calibri",15),textvariable=password).grid(padx=4,pady=21)
        repasswordLabel1= Label(newWindow, width="25",text=" Re enter Password ",font=("Calibri",15),
                          bg="DodgerBlue2").grid(padx=6,pady=20)
        repassword = StringVar()
        repasswordEntry = Entry(newWindow, width="25",font=("Calibri",15),textvariable=repassword).grid(padx=6,pady=21)
        validate_user_creation = partial(
            validate_user_creation, username, password, repassword)
        CreateAccountButton = Button(newWindow, text="Create Account",bg="snow3",
                             command=validate_user_creation,font=("Calibri",15,"bold")).grid(padx=8)
    createNewAccount = Button(tkWindow, text="Create New Account",bg="snow3",font=("Calibri", 20,"bold"),command=openNewWindow).grid(padx=10)
    tkWindow.mainloop()


login()
print("Exiting..")
