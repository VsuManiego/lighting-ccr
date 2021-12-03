# Title of the Project:          Engineering Utilities Lighting Design by Zonal Cavity Method Virtual Assistant
# Author:                        Alyka M. Cruz, Miles B. Costillas, Dariel King S. Ramirez
# Date Created:                  2021/11/25

import math
import pandas as pd
import sqlite3

root = tk.Tk()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root.title("Zonal Cavity")
root = Tk()
root.title("Zonal Cavity")

width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#6666ff")

df = pd.read_excel(r'C:\Users\alyka\Downloads\Computer Fundamentals and Programming\Zonal Cavity MethodAnnex.xlsx')
print(df)

tab_control = ttk.Notebook(root)
tab_control.pack(pady=15)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Space and Occupancy Details")
tab_control.pack(expand=1, fill="both")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Type of Lamp")
tab_control.pack(expand=1, fill="both")

tab_i = ttk.Frame(tab_control)
tab_control.add(tab3, text="Effective Reflectance")
tab_control.pack(expand=1, fill="both")

tab3 = ttk.Frame(tab_control)
tab_control.add(tab4, text="Actual Reflectance")
tab_control.pack(expand=1, fill="both")

tab4 = ttk.Frame(tab_control)
tab_control.add(tab5, text="Light Output")
tab_control.pack(expand=1, fill="both")

tab5 = ttk.Frame(tab_control)
tab_control.add(tab6, text="Light Loss Factor")
tab_control.pack(expand=1, fill="both")

tab5 = ttk.Frame(tab_control)
tab_control.add(tab7, text="Required Number of Fixtures")
tab_control.pack(expand=1, fill="both")

tab5 = ttk.Frame(tab_control)
tab_control.add(tab8, text="Spacing Between Luminaries")
tab_control.pack(expand=1, fill="both")

tab5 = ttk.Frame(tab_control)
tab_control.add(tab9, text="Efficacy of Lighting Design")
tab_control.pack(expand=1, fill="both")

USERNAME = StringVar()
PASSWORD = StringVar()
PROJECT_NAME = StringVar()

SEARCH = StringVar()


def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `home` (home_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `designs` (designs_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, designs_name TEXT)")
    cursor.execute("SELECT * FROM `home` WHERE `username` = 'admin' AND `password` = 'designs'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()


def Exit():
    result = tkMessageBox.askquestion('Lighting Desgin: Zonal Cavity Method', 'Are you sure you want to exit?',
                                      icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Exit2():
    result = tkMessageBox.askquestion('Lighting Desgin: Zonal Cavity Method', 'Are you sure you want to exit?',
                                      icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()


def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Lighting Desgin: Zonal Cavity Method/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()


def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="User Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)


def Home():
    global Home
    Home = Tk()
    Home.title("Lighting Desgin: Zonal Cavity Method/Home")
    width = 1024
    height = 520
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Lighting Desgin: Zonal Cavity Method", font=('arial', 45))
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add new design", command=ShowAddNew)
    filemenu2.add_command(label="View previous designs", command=ShowView)
    Home.config(menu=menubar)
    Home.config(bg="#6666ff")


def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Lighting Desgin: Zonal Cavity Method/Add new designs")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()


def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Design", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_productname = Label(MidAddNew, text="Project Name:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=0, sticky=W)


def AddNew():
    Database()
    cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price) VALUES(?, ?, ?)",
                   (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), int(PRODUCT_PRICE.get())))
    conn.commit()
    PROJECT_NAME.set("")
    cursor.close()
    conn.close()


# still needs revision for canvas, entry and label churva
# requires numerous tables and other datas
# --------------
# tab1
canvas1 = tk.Canvas(tab1, width=470, height=480)
canvas1.pack()

label1 = tk.Label(tab1, text='Space Details')
label1.config(font=('Arial', 14))
canvas1.create_window(235, 40, window=label1)

entry1 = tk.Entry(tab1)
canvas1.create_window(330, 170, window=entry1)


def SpaceDetails():
    try:
    except ValueError:
        messagebox.showerror("Error")

else:

button1 = tk.Button(text='Space and Occupancy Details', command=SpaceDetails, bg='green', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(240, 330, window=button2)

# tab2
canvas2 = tk.Canvas(tab2, width=470, height=480)
canvas2.pack()

label2 = tk.Label(tab2, text='Lamp Details')
label2.config(font=('Arial', 14))
canvas2.create_window(235, 40, window=label1)

entry2 = tk.Entry(tab2)
canvas2.create_window(330, 170, window=entry1)


def LampDetails():
    try:
    except ValueError:
        messagebox.showerror("Error")

else:

button2 = tk.Button(text='Lamp Details and Specifications', command=LampDetails, bg='green', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas2.create_window(240, 330, window=button2)

# tab3
canvas3 = tk.Canvas(tab3, width=470, height=480)
canvas3.pack()

label3 = tk.Label(tab3, text='Reflectance Value')
label3.config(font=('Arial', 14))
canvas3.create_window(235, 40, window=label1)

entry3 = tk.Entry(tab3)
canvas3.create_window(330, 170, window=entry1)


def Reflectance():
    try:
    except ValueError:
        messagebox.showerror("Error")

else:

button3 = tk.Button(text='Reflectance Value', command=Reflectance, bg='green', fg='white',
                    font=('arial', 9, 'bold'))
canvas3.create_window(240, 330, window=button2)

# tab4
canvas4 = tk.Canvas(tab4, width=470, height=480)
canvas4.pack()

label4 = tk.Label(tab4, text='Coeffecient of Utilization')
label4.config(font=('Arial', 14))
canvas4.create_window(235, 40, window=label1)

entry4 = tk.Entry(tab4)
canvas4.create_window(330, 170, window=entry1)


def CoeUtil():
    try:
    except ValueError:
        messagebox.showerror("Error")

else:

button4 = tk.Button(text='Coeffecient of Utilization', command=CoeUtil, bg='green', fg='white',
                    font=('arial', 9, 'bold'))
canvas4.create_window(240, 330, window=button2)

# tab5
canvas5 = tk.Canvas(tab5, width=470, height=480)
canvas5.pack()

label5 = tk.Label(tab5, text='Lumen Output')
label5.config(font=('Arial', 14))
canvas5.create_window(235, 40, window=label1)

entry5 = tk.Entry(tab5)
canvas5.create_window(330, 170, window=entry1)


def LumenOutput():
    try:
    except ValueError:
        messagebox.showerror("Error")

else:

button5 = tk.Button(text='Lumen Output', command=LumenOutput, bg='green', fg='white',
                    font=('arial', 9, 'bold'))
canvas5.create_window(240, 330, window=button2)

# tab6
canvas6 = tk.Canvas(tab6, width=470, height=480)
canvas6.pack()

label6 = tk.Label(tab6, text='Light Loss Factor')
label6.config(font=('Arial', 14))
canvas6.create_window(235, 40, window=label1)

entry6 = tk.Entry(tab6)
canvas6.create_window(330, 170, window=entry1)


def LightLoss():
    try:
    except ValueError:
        messagebox.showerror("Error")

else:

button6 = tk.Button(text='Light Loss Factor', command=LightLoss, bg='green', fg='white',
                    font=('arial', 9, 'bold'))
canvas6.create_window(240, 330, window=button2)

# tab7
canvas7 = tk.Canvas(tab7, width=470, height=480)
canvas7.pack()

label7 = tk.Label(tab7, text='Fixtures')
label7.config(font=('Arial', 14))
canvas7.create_window(235, 40, window=label1)

entry7 = tk.Entry(tab7)
canvas7.create_window(330, 170, window=entry1)


def Fixtures():
    try:
    except ValueError:
        messagebox.showerror("Error")

else:

button7 = tk.Button(text='Fixtures', command=fixtures, bg='green', fg='white',
                    font=('arial', 9, 'bold'))
canvas7.create_window(240, 330, window=button2)

# tab8
canvas8 = tk.Canvas(tab8, width=470, height=480)
canvas8.pack()

label8 = tk.Label(tab8, text='Spacing Criteria')
label8.config(font=('Arial', 14))
canvas8.create_window(235, 40, window=label1)

entry8 = tk.Entry(tab8)
canvas8.create_window(330, 170, window=entry1)


def SpaceCriteria():
    try:
    except ValueError:
        messagebox.showerror("Error")

else:

button8 = tk.Button(text='Spacing Criteria', command=SpaceCriteria, bg='green', fg='white',
                    font=('arial', 9, 'bold'))
canvas8.create_window(240, 330, window=button2)

# tab9
canvas9 = tk.Canvas(tab9, width=470, height=480)
canvas9.pack()

label9 = tk.Label(tab9, text='Efficacy of Lighting Design')
label9.config(font=('Arial', 14))
canvas9.create_window(235, 40, window=label1)

entry9 = tk.Entry(tab9)
canvas9.create_window(330, 170, window=entry1)


def Efficacy():
    try:
    except ValueError:
        messagebox.showerror("Error")

else:

button9 = tk.Button(text='Efficacy of Lighting Design', command=Efficacy, bg='green', fg='white',
                    font=('Arial', 9, 'bold'))
canvas9.create_window(240, 330, window=button2)

# ==========================
# still needs polishing and finalizing the tables
# -------
# (initial formula and codes)
# Title of the Project:          Engineering Utilities Lighting Design by Zonal Cavity Method Virtual Assistant
# Author:                        Alyka M. Cruz, Miles B. Costillas, Dariel King S. Ramirez
# Date Created:                  2021/11/25

import math
import pandas as pd

root = tk.Tk()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root.title("Zonal Cavity")
root = Tk()
root.title("Simple Inventory System")

width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#6666ff")

df = pd.read_excel(r'C:\Users\alyka\Downloads\Computer Fundamentals and Programming\Zonal Cavity MethodAnnex.xlsx')
print(df)

print(f'Engineering Utilities Lighting Design' '\n ZONAL CAVITY METHOD')
print('\n')

print("OCCUPANCY DETAILS")
occupancy = float(input("Occupancy: "))
maintenance_cycle = float(input("Maintenance Cycle (years): "))

print('\n')
print("LAMP DETAILS")
type_of_lamp = input("Type of Lamp: ")
watts = int(input("Wattage: "))
type_of_luminaire = input("Type of Luminaire: ")
number_lamps = float(int(input("Maximum number of lamps: ")))
cs_perpendicular = float(int(input("CS Perpendicular: ")))
cs_parallel = float(int(input("CS Parallel: ")))

print('\n')
print("SPACE DETAILS")

width = float(int(input("Width(m): ")))
depth = float(int(input("Depth (m): ")))
height = float(int(input("Height(m): ")))

p_unit = "meters"
a_unit = "square meters"

perimeter = (2 * depth) + (2 * width)
print("Perimeter: ", perimeter, p_unit)

area = width * depth
print("Area: ", area, a_unit)

print('\n')
print("EFFECTIVE REFLECTANCE")

hcc = float(int(input("Ceiling Cavity: ")))
hrc = float(int(input("Room Cavity: ")))
hfc = float(int(input("Floor Cavity: ")))

rcc = (2.5 * hcc) * (perimeter / area)
rrc = (2.5 * hrc) * (perimeter / area)
rfc = (2.5 * hfc) * (perimeter / area)

print("Ceiling Cavity Ratio (Rcc): ", rcc)
print("Room Cavity Ratio (Rrc): ", rrc)
print("Floor Cavity Ratio (Rfc): ", rfc)

print('\n')
print("ACTUAL REFLECTANCE")
floor_finish = input("Floor Finish: ")
wall_finish = input("Wall Finish: ")
ceiling_finish = input("Ceiling Finish: ")
# insert table
df = pd.read_excel(r'C:\Users\alyka\Downloads\Computer Fundamentals and Programming\Zonal Cavity MethodAnnex.xlsx')
df = pd.DataFrame(data, columns=['10'])
print(df)

print('\n')
print("COEFFICIENT OF UTILIZATION")
pcc = int(input("PCC: "))
pw = int(input("PW: "))
# insert table
df = pd.read_excel(r'C:\Users\alyka\Downloads\Computer Fundamentals and Programming\Zonal Cavity MethodAnnex.xlsx')
print(df)
df = pd.DataFrame(data, columns=['20'])
cu = int(input("Coefficient of Utilization: "))

print('\n')
print("LUMEN OUTPUT")
lumen = "lm"
lumen_output = int(input("Lumen Output: "))
num_lamps = int(input("Number of lamps: "))
lld = int(input("Lamp Lumen Depreciation: "))
# insert table for LLD
df = pd.read_excel(r'C:\Users\alyka\Downloads\Computer Fundamentals and Programming\Zonal Cavity MethodAnnex.xlsx')
print(df)
df = pd.DataFrame(data, columns=['30'])

light_output = "lumens"
lo = (num_lamps * lumen_output * lld)
print("Light Ouput: ", lo)

print('\n')
print("LIGHT LOSS FACTOR")
fmf = int(input("Floor Multiplying Factor: "))
# insert table
df = pd.read_excel(r'C:\Users\alyka\Downloads\Computer Fundamentals and Programming\Zonal Cavity MethodAnnex.xlsx')
print(df)
df = pd.DataFrame(data, columns=['40'])
dl = int(input("Lumen Dirt Depreciation: "))
# insert table
df = pd.read_excel(r'C:\Users\alyka\Downloads\Computer Fundamentals and Programming\Zonal Cavity MethodAnnex.xlsx')
print(df)
df = pd.DataFrame(data, columns=['50'])
drs = int(input("Room Surface Dirt Depreciation: "))
# insert table
df = pd.read_excel(r'C:\Users\alyka\Downloads\Computer Fundamentals and Programming\Zonal Cavity MethodAnnex.xlsx')
print(df)
df = pd.DataFrame(data, columns=['60'])
lb = int(input("Light Burnout: "))
# insert table
df = pd.read_excel(r'C:\Users\alyka\Downloads\Computer Fundamentals and Programming\Zonal Cavity MethodAnnex.xlsx')
print(df)
df = pd.DataFrame(data, columns=['70'])
lff = (fmf * dl * drs * lb)
print("Light Loss Factor: ", lff)

print('\n')
print("NUMBER OF FIXTURES")
e = int(input("Illuminance on the Work Plane: "))
# insert table
df = pd.read_excel(r'C:\Users\alyka\Downloads\Computer Fundamentals and Programming\Zonal Cavity MethodAnnex.xlsx')
print(df)
df = pd.DataFrame(data, columns=['80'])
nl = ((e * area) / (cu * lo * lff))
luminaire = math.ceil(nl)
print("Number of Luminaires: ", luminaire)

print('\n')
print("SPACING CRITERIA")
perpendicular = (cs_perpendicular * hrc)
print("Perpendicular Spacing Criteria: ", perpendicular)
parallel = (cs_parallel * hrc)
print("Parallel Spacing Criteria: ", parallel)

print('\n')
print("EFFICACY OF LIGHTING DESIGN")
nt = (luminaire * number_lamps)
light_density = int(input("Allowable Light Density: "))
# insert table
df = pd.read_excel(r'C:\Users\alyka\Downloads\Computer Fundamentals and Programming\Zonal Cavity MethodAnnex.xlsx')
print(df)
df = pd.DataFrame(data, columns=['90'])
dlp = ((nt * watts) / area)
lp = round(dlp, 3)
lp_density = "watts per square meters"
print("Lighting Power Density: ", lp, lp_density)

if lp < light_density:
    print("Design is efficient. Lighting Design is approved.")
else:
    print("Design is not efficient. Use of different type of lamp with a different wattage is suggested.")