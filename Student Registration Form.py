from tkinter import *
from sqlite3 import *
from tkinter import messagebox
from tkinter import ttk

reg_form = Tk()
reg_form.title("STUDENT REGISTRATION FORM")
reg_form.geometry("700x700")
reg_form["bg"] = "slateblue3"

fname_label = Label(reg_form, text = "FIRST NAME", 
                    bg = "slateblue3", fg = "white")
fname_label.grid(row = 1, column = 0, sticky = W, pady = 4)

fname_entry = Entry(reg_form)
fname_entry.grid(row = 1, column = 1, pady = 4)

fname_range = Label(reg_form, text = "(max 30 characters a-z and A-Z)", 
                    bg = "slateblue3", fg = "white")
fname_range.grid(row = 1, column = 2, sticky = W)

lname_label = Label(reg_form, text = "LAST NAME", 
                    bg = "slateblue3", fg = "white")
lname_label.grid(row = 3, column = 0, sticky = W, pady = 4)

lname_entry = Entry(reg_form)
lname_entry.grid(row = 3, column = 1, pady = 4)

lname_range = Label(reg_form, text = "(max 30 characters a-z and A-Z)", 
                    bg = "slateblue3", fg = "white")
lname_range.grid(row = 3, column = 2, sticky = W)

dob_label = Label(reg_form, text = "DATE OF BIRTH",
                  bg = "slateblue3", fg = "white")
dob_label.grid(row = 6, column = 0, sticky = W, pady = 4)

day = StringVar(reg_form)

day_combo = ttk.Combobox(reg_form, textvariable = day, width = 5)
day_combo['values'] = ("Day:", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
                       '11', '12', '13', '14', '15', '16', '17', '18', 
                       '19', '20', '21', '22', '23', '24', '25', '26', 
                       '27', '28', '29', '30', '31')
day_combo.current(0)
day_combo.grid(row = 6, column = 1, pady = 4, sticky = EW)

month = StringVar(reg_form)

month_combo = ttk.Combobox(reg_form, text = "Month:", 
                           textvariable = month, width = 5)
month_combo['values'] = ("Month:", 'January', 'February', 
                         'March', 'April', 
                         'May', 'June', 
                         'July', 'August', 
                         'September', 'October', 
                         'November', 'December')
month_combo.current(0)
month_combo.grid(row = 6, column = 2, pady = 4, sticky = EW)

year = StringVar(reg_form)

year_combo = ttk.Combobox(reg_form, text = "Year:", 
                          textvariable = year, width =5)
years = ["Year:"]
years.extend([str(x) for x in range(1980,2019)])
year_combo['values'] = years[:]
year_combo.current(0)
year_combo.grid(row = 6, column = 3, pady = 4, sticky = EW)

mail_label = Label(reg_form, text = "EMAIL ID", bg = "slateblue3", fg = "white")
mail_label.grid(row = 9, column = 0, sticky = W, pady = 4)

mail_entry = Entry(reg_form)
mail_entry.grid(row = 9, column = 1, pady = 4)

mob_label = Label(reg_form, text = "MOBILE NUMBER", 
                  bg = "slateblue3", fg = "white")
mob_label.grid(row = 12, column = 0, sticky = W, pady = 4)

mob_entry = Entry(reg_form)
mob_entry.grid(row = 12, column = 1, pady = 4)

mob_range = Label(reg_form, text = "(10 digit number)", 
                  bg = "slateblue3", fg = "white")
mob_range.grid(row = 12, column = 2, sticky = W)

gender_label = Label(reg_form, text = "GENDER", bg = "slateblue3", fg = "white")
gender_label.grid(row = 15, column = 0, sticky = W, pady = 4)

v = IntVar(reg_form, 0)

values = {"Male" : 1,
         "Female" : 2}

for text, value in values.items():
    button = Radiobutton(reg_form, text = text, variable = v, value = value, 
                         bg = "slateblue3")
    button.grid(row = 15, column = value, sticky = W)

add_label = Label(reg_form, text = "ADDRESS", bg = "slateblue3", fg = "white")
add_label.grid(row = 18, rowspan = 4, column = 0, sticky = NW, pady = 4)

add_entry = Text(reg_form, height = 3, width = 30)
add_entry.grid(row = 18, column = 1, columnspan = 2, pady = 4, sticky = W)

city_label = Label(reg_form, text = "CITY", bg = "slateblue3", fg = "white")
city_label.grid(row = 21, column = 0, sticky = W, pady = 4)

city_entry = Entry(reg_form)
city_entry.grid(row = 21, column = 1, pady = 4)

city_range = Label(reg_form, text = "(max 30 characters a-z and A-Z)", 
                    bg = "slateblue3", fg = "white")
city_range.grid(row = 21, column = 2, sticky = W)

pin_label = Label(reg_form, text = "PIN CODE", bg = "slateblue3", fg = "white")
pin_label.grid(row = 24, column = 0, sticky = W, pady = 4)

pin_entry = Entry(reg_form)
pin_entry.grid(row = 24, column = 1, pady = 4)

pin_range = Label(reg_form, text = "(6 digit number)", 
                    bg = "slateblue3", fg = "white")
pin_range.grid(row = 24, column = 2, sticky = W)

state_label = Label(reg_form, text = "STATE", bg = "slateblue3", fg = "white")
state_label.grid(row = 27, column = 0, sticky = W, pady = 4)

state_entry = Entry(reg_form)
state_entry.grid(row = 27, column = 1)

state_range = Label(reg_form, text = "(max 30 characters a-z and A-Z)", 
                    bg = "slateblue3", fg = "white")
state_range.grid(row = 27, column = 2, sticky = W)

country_label = Label(reg_form, text = "COUNTRY", bg = "slateblue3", fg = "white")
country_label.grid(row = 30, column = 0, sticky = W, pady = 4)

def_country = StringVar(reg_form, "India")
country_entry = Entry(reg_form, text = def_country)
country_entry.grid(row = 30, column = 1, pady = 4)

hobbies_label = Label(reg_form, text = "HOBBIES", bg = "slateblue3", fg = "white")
hobbies_label.grid(row = 33, column = 0, sticky = W, pady = 3)

h1 = IntVar(reg_form, 0)
h2 = IntVar(reg_form, 0)
h3 = IntVar(reg_form, 0)
h4 = IntVar(reg_form, 0)
h5 = IntVar(reg_form, 0)

hobby1 = Checkbutton(reg_form, text = "Drawing", variable = h1, 
                     onvalue = 1, offvalue = 0, bg = "slateblue3")
hobby2 = Checkbutton(reg_form, text = "Singing", variable = h2, 
                     onvalue = 1, offvalue = 0, bg = "slateblue3")
hobby3 = Checkbutton(reg_form, text = "Dancing", variable = h3, 
                     onvalue = 1, offvalue = 0, bg = "slateblue3")
hobby4 = Checkbutton(reg_form, text = "Sketching", variable = h4, 
                     onvalue = 1, offvalue = 0, bg = "slateblue3")
hobby5 = Checkbutton(reg_form, text = "Other", variable = h5, 
                     onvalue = 1, offvalue = 0, bg = "slateblue3")

hobby1.grid(row = 33, column = 1, padx = 2, sticky = W)
hobby2.grid(row = 33, column = 2, padx = 2, sticky = W)
hobby3.grid(row = 33, column = 3, padx = 2, sticky = W)
hobby4.grid(row = 33, column = 4, padx = 2, sticky = W)
hobby5.grid(row = 34, column = 1, padx = 2, sticky = W)

otherhob_entry = Entry(reg_form)
otherhob_entry.grid(row = 34, column = 2, sticky = W) 

qlf_label = Label(reg_form, text = "QUALIFICATION", 
                  bg = "slateblue3", fg = "white")
qlf_label.grid(row = 35, column = 0, sticky = W, pady = 4)

ex_label = Label(reg_form, text = "Sl. No. Examination", 
                 bg = "slateblue3", fg = "white")
ex_label.grid(row = 35, column = 1, sticky = W, pady = 2)

board_label = Label(reg_form, text = "  Board", 
                    bg = "slateblue3", fg = "white")
board_label.grid(row = 35, column = 2, pady = 2)

b1_entry = Entry(reg_form)
b1_entry.grid(row = 36, column = 2, padx = 1, pady = 1, sticky = E)
b2_entry = Entry(reg_form)
b2_entry.grid(row = 37, column = 2, pady = 2, padx = 1, sticky = E)
b3_entry = Entry(reg_form)
b3_entry.grid(row = 38, column = 2, pady = 2, padx = 1, sticky = E)
b4_entry = Entry(reg_form)
b4_entry.grid(row = 39, column = 2, pady = 2, padx = 1, sticky = E)

b_range = Label(reg_form, text = "(10 chars max)", 
                    bg = "slateblue3", fg = "white")
b_range.grid(row = 40, column = 2, sticky = EW)

per_label = Label(reg_form, text = "Percentage", 
                  bg = "slateblue3", fg = "white")
per_label.grid(row = 35, column = 3, pady = 2, padx = 2)

p1_entry = Entry(reg_form)
p1_entry.grid(row = 36, column = 3, pady = 2, padx = 1)
p2_entry = Entry(reg_form)
p2_entry.grid(row = 37, column = 3, pady = 2, padx = 1)
p3_entry = Entry(reg_form)
p3_entry.grid(row = 38, column = 3, pady = 2, padx = 1)
p4_entry = Entry(reg_form)
p4_entry.grid(row = 39, column = 3, pady = 2, padx = 1)

p_range = Label(reg_form, text = "(upto 2 decimals)", 
                    bg = "slateblue3", fg = "white")
p_range.grid(row = 40, column = 3)

yr_label = Label(reg_form, text = "Year of Passing", 
                 bg = "slateblue3", fg = "white")
yr_label.grid(row = 35, column = 4, pady = 2, padx = 1)

y1_entry = Entry(reg_form)
y1_entry.grid(row = 36, column = 4, pady = 2, padx = 1)
y2_entry = Entry(reg_form)
y2_entry.grid(row = 37, column = 4, pady = 2, padx = 1)
y3_entry = Entry(reg_form)
y3_entry.grid(row = 38, column = 4, pady = 2, padx = 1)
y4_entry = Entry(reg_form)
y4_entry.grid(row = 39, column = 4, pady = 2, padx = 1)

sl1_label = Label(reg_form, text = "1      Class X", 
                  bg = "slateblue3", fg = "white")
sl1_label.grid(row = 36, column = 1,sticky = W, pady = 2)

sl2_label = Label(reg_form, text = "2      Class XII", 
                  bg = "slateblue3", fg = "white")
sl2_label.grid(row = 37, column = 1,sticky = W, pady = 2)

sl3_label = Label(reg_form, text = "3      Graduation", 
                  bg = "slateblue3", fg = "white")
sl3_label.grid(row = 38, column = 1,sticky = W, pady = 2)

sl4_label = Label(reg_form, text = "4      Masters", 
                  bg = "slateblue3", fg = "white")
sl4_label.grid(row = 39, column = 1,sticky = W, pady = 2)

courses_label = Label(reg_form, text = "COURSES\nAPPLIED FOR", 
                      bg = "slateblue3", fg = "white")
courses_label.grid(row = 41, column = 0, sticky = W, pady = 3)

c = IntVar(reg_form, 0)
courses = {"BCA" : 1,
          "B.com" : 2,
          "B.Sc" : 3, 
          "B.A" : 4}

for course,value in courses.items():
    button = Radiobutton(reg_form, text = course, value = value,
                        variable = c, bg = "slateblue3")
    button.grid(row = 41, column = value)
    
def sub_clicked():
    f_n = fname_entry.get()
    l_n = lname_entry.get()
    dob = str(day.get()) + " " + str(month.get()) + " " + str(year.get())
    mail = mail_entry.get()
    mob = mob_entry.get()
    gender = ""
    if v.get() == 1:
        gender = "M"
    elif v.get() == 2:
        gender = "F"
    ads = add_entry.get("1.0", END)
    city = city_entry.get()
    pin = pin_entry.get()
    state = state_entry.get()
    ctry = country_entry.get()
    hobbies = ""
    if h1.get() == 1:
        hobbies += "Drawing, " 
    if h2.get() == 1:
        hobbies += "Singing, " 
    if h3.get() == 1:
        hobbies += "Dancing, " 
    if h4.get() == 1:
        hobbies += "Sketching, " 
    if h5.get() == 1:
        hobbies += str(otherhob_entry.get())
    X_board = b1_entry.get()
    XII_board = b2_entry.get()
    graduation_board = b3_entry.get()
    masters_board = b4_entry.get()
    X_yr = y1_entry.get()
    XII_yr = y2_entry.get()
    graduation_yr = y3_entry.get()
    masters_yr = y4_entry.get()
    X_per = p1_entry.get()
    XII_per = p2_entry.get()
    graduation_per = p3_entry.get()
    masters_per = p4_entry.get() 
    course = ""
    if c.get() == 1:
        course = "BCA"
    elif c.get() == 2:
        course = "B.com"
    elif c.get() == 3:
        course = "B.Sc"
    elif c.get() == 4:
        course = "B.A"    
        
    conn = connect("reg_form.db")
    
    crsr = conn.cursor()
    with conn:
        crsr.execute("""CREATE TABLE IF NOT EXISTS std (
        fname VARCHAR(30), 
        lname VARCHAR(30), 
        dob VARCHAR(20), 
        mail VARCHAR(30), 
        mob VARCHAR(30), 
        gen VARCHAR(20), 
        address VARCHAR(100), 
        cty VARCHAR(20), 
        pin VARCHAR(10), 
        ste VARCHAR(20), 
        cntry VARCHAR(20), 
        hobbies TEXT,
        X_board VARCHAR(20), 
        X_year VARCHAR(5), 
        X_per VARCHAR(5),
        XII_board VARCHAR(20), 
        XII_year VARCHAR(5), 
        XII_per VARCHAR(5), 
        grad_board VARCHAR(50), 
        grad_year VARCHAR(5), 
        grad_per VARCHAR(5), 
        masters_board VARCHAR(50), 
        masters_year VARCHAR(5), 
        masters_per VARCHAR(5), 
        course VARCHAR(20)
        )""")
        
        crsr.execute("""INSERT INTO std (
        fname, lname, 
        dob, mail, 
        mob, gen, 
        address, cty, 
        pin, ste, 
        cntry, hobbies,
        X_board, X_year, 
        X_per, XII_board, 
        XII_year, XII_per, 
        grad_board, grad_year, 
        grad_per, masters_board, 
        masters_year, masters_per, 
        course) 
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", 
                     (f_n, l_n, dob, mail, mob, gender, ads, city, pin, state, ctry, hobbies, X_board, X_yr, X_per, XII_board, XII_yr, XII_per, graduation_board, graduation_yr, graduation_per, masters_board, masters_yr, masters_per, course, ))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Submission", "Submitted Successfully")
    
sub_bt = Button(reg_form, text = "Submit", command = sub_clicked)
sub_bt.grid(row = 42, column = 1)

def delete():
    fname_entry.delete(0,'end')
    lname_entry.delete(0,'end')
    v.set(0) 
    day_combo.current(0)
    month_combo.current(0)
    year_combo.current(0)
    mail_entry.delete(0,'end')
    mob_entry.delete(0,'end')
    add_entry.delete('1.0','end')
    city_entry.delete(0,'end')
    pin_entry.delete(0,'end')
    state_entry.delete(0,'end')
    cty = StringVar(reg_form,"India")
    country_entry.configure(text = cty)
    h1.set(0)
    h2.set(0)
    h3.set(0)
    h4.set(0)
    h5.set(0)
    otherhob_entry.delete(0,'end')
    b1_entry.delete(0,'end')
    p1_entry.delete(0,'end')
    y1_entry.delete(0,'end')
    b2_entry.delete(0,'end')
    p2_entry.delete(0,'end')
    y2_entry.delete(0,'end')
    b3_entry.delete(0,'end')
    p3_entry.delete(0,'end')
    y3_entry.delete(0,'end')
    b4_entry.delete(0,'end')
    p4_entry.delete(0,'end')
    y4_entry.delete(0,'end')
    c.set(0)

reset_bt = Button(reg_form, text = "Reset", command = delete)
reset_bt.grid(row = 42, column = 2)

def display():
    lst = [
           "First Name : ", "Last Name : ", 
           "DOB : " , "EMAIL Id : ",
           "MOBILE : ", "GENDER : ",
           "ADDRESS : ", "CITY : ",
           "PIN : ", "STATE : ",
           "COUNTRY : ", "HOBBIES : ",
           "X BOARD : ", "X PERCENTAGE :", 
           "X YEAR OF PASSING : ", "XII BOARD : ", 
           "XII PERCENTAGE :", "XII YEAR OF PASSING : ",
           "GRADUATION BOARD : ", "GRADUATION PERCENTAGE :", 
           "GRADUATION YEAR OF PASSING : ", 
           "MASTERS BOARD : ", "MASTERS PERCENTAGE :", 
           "MASTERS YEAR OF PASSING : ", "COURSES APPLIED : "
          ]
    
    reg = Tk()
    reg.geometry("500x500")
    
    conn = connect("reg_form.db")
    crsr = conn.cursor()
    crsr.execute("SELECT * FROM std ")
    records = crsr.fetchall()
    
    for i in range(len(lst)):
        A = Label(reg, text = lst[i])
        A.grid(row = i, column = 0, sticky = W, padx = 20, pady = 5)
        
    i = 1
    for record in records:
        j =0
        for item in record:
            L = Label(reg, text = item)
            L.grid(row = j, column = i, sticky = W, padx = 20, pady = 5)
            j += 1
        i += 1
    
    conn.commit()
    conn.close()
    
    reg.mainloop()       
            
dis_bt = Button(reg_form, text = "DISPLAY", command = display)
dis_bt.grid(row = 42, column = 3, pady = 5)

def dropTable():
    conn = connect("reg_form.db")
    crsr = conn.execute("DROP TABLE std")
    conn.commit()
    
drop_bt = Button(reg_form, text = "DROP TABLE", command = dropTable)
drop_bt.grid(row = 42, column = 4, pady = 5)


reg_form.mainloop()
