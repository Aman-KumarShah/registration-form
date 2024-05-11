from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter.messagebox as tmsg
from tkinter import messagebox
import pyttsx3
import webbrowser
import openpyxl


def second_page(root):
    secondroot = Toplevel(root)
    secondroot.title("BrainHacks Application Form")
    secondroot.configure(bg="white")
    secondroot.wm_iconbitmap("stceticon.ico")
    Width = secondroot.winfo_screenwidth()
    Height = secondroot.winfo_screenheight()

    secondroot.geometry(f"{Width}x{Height}+-6+0")
    secondroot.minsize(Width, Height)


    # HEADING - CAPTIONS
    f01 = Frame(secondroot, width=Width, heigh=75, bg="#92c8d6",
            relief=GROOVE, borderwidth=2)
    f01.pack(fill=X)
    Label(f01, text="BRAINHACKS", font="widelatin 40 bold",
        bg="#92c8d6").place(x=85, y=3)

    def update():
        l0.config(text="|", fg='white')
        e0.config(text="Let's Code", fg='white') 
        e0.after(2000, myfunc)
    def myfunc():
        l0.config(text="|", fg='white')
        e0.config(text="Let's Compete", fg='white')
        e0.after(2000, update)
    l0 = Label(f01, text="", font="widelatin 35 bold", bg="#92c8d6", fg="white")
    l0.place(x=455, y=1)
    e0 = Label(f01, text='', font="arialblack 25 bold", bg="#92c8d6", fg="white")
    e0.place(x=485, y=18)
    e0.after(2000, myfunc)


    # HEADING - IMAGES(ICONS)
    image2 = Image.open("icon1.png").resize((60, 60))
    photo2 = ImageTk.PhotoImage(image2)
    Label(f01,image=photo2, bg="#92c8d6").place(x=15, y=5)

    image3 = Image.open("icon2.png").resize((78, 66))
    photo3 = ImageTk.PhotoImage(image3)
    Label(f01,image=photo3, bg="#92c8d6").place(x=Width-195, y=1) 


    image1 = Image.open("icon3.png").resize((70, 66))
    photo1 = ImageTk.PhotoImage(image1)
    Label(f01,image=photo1, bg="#92c8d6").place(x=Width-93, y=1)


    # CREATING ANOTHER WINDOW
    main_frame = Frame(secondroot, bg="white")
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame, bg="white")
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(
        main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox(ALL)))
    second_frame = Frame(my_canvas, bg="white")

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


    # LABELFRAMES
    LabelFrame(second_frame, text="PERSONAL DETAILS", font="alegreya 17 bold underline",
            bg="white", width=Width-70, height=410, relief=SOLID).pack(pady=20, padx=30)
    LabelFrame(second_frame, text="ADDRESS", font="alegreya 17 bold underline",
            bg="white", width=Width-70, height=300, relief=SOLID).pack(pady=20, padx=30)
    LabelFrame(second_frame, text="EDUCATIONAL DETAILS", font="alegreya 17 bold underline",
            bg="white", width=Width-70, height=290, relief=SOLID).pack(pady=20, padx=30)


    # NAME
    Label(second_frame, text="Name           :",
        font="cambria 14 ", bg="white").place(x=60, y=70)
    # FIRST NAME
    def firstname_delete(event):
        if firstname_entry.get() == "First Name":
            firstname_entry.configure(fg="black")
            firstname_entry.delete(0, "end")
    def firstname_insert(event):
        if len(firstname.get()) == 0:
            firstname_entry.delete(0, "end")
            firstname_entry.configure(fg="grey")
            firstname_entry.insert(0, "First Name")
        elif not firstname.get().isalpha() and firstname.get() != "First Name":
            firstname_entry.delete(0, "end")
            firstname_entry.configure(fg="grey")
            firstname_entry.insert(0, "First Name")
            # tmsg.showinfo("Name Error","Error.\nPlease Enter Valid Name Input.")
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 4.5)
            text_speech.say("Please enter valid first name")
            text_speech.runAndWait()
        else:
            str = firstname.get().title()
            firstname_entry.delete(0, "end")
            firstname_entry.insert(0, str)
    firstname = StringVar()
    firstname_entry = Entry(second_frame, textvariable=firstname, font="cambria 13", width=16, relief=FLAT,
                            fg="grey", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
    firstname_insert(1)
    firstname_entry.place(x=165, y=70)
    firstname_entry.bind("<FocusIn>", firstname_delete)
    firstname_entry.bind("<FocusOut>", firstname_insert)
    # firstname_entry.bind("<Return>",firstname_insert)


    # MIDDLE NAME
    def middlename_insert(event):
        if len(middlename.get()) == 0:
            middlename_entry.configure(fg="grey")
            middlename_entry.insert(0, "Middle Name")
        else:
            string = middlename.get().split(' ')
            for substr in string:
                if substr != '' and not substr.isalpha():
                    middlename_entry.delete(0, "end")
                    middlename_entry.configure(fg="grey")
                    middlename_entry.insert(0, "Middle Name")
                    # tmsg.showinfo("Guardian's Name Error","Error.\nPlease Enter Valid Name Input.")
                    text_speech = pyttsx3.init()
                    text_speech.setProperty("volume", 4.5)
                    text_speech.say("Please enter valid middle name")
                    text_speech.runAndWait()
            else:
                    middlename_caps(1)
    def middlename_caps(event):
        str = middlename.get().title()
        middlename_entry.delete(0, "end")
        middlename_entry.insert(0, str)
    def middlename_delete(o):
        if middlename_entry.get() == "Middle Name":
            middlename_entry.configure(fg="black")
            middlename_entry.delete(0, "end")
    middlename = StringVar()
    middlename_entry = Entry(second_frame, textvariable=middlename, font="cambria 13", width=16, relief=FLAT,
                            fg="grey", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
    middlename_insert(1)
    middlename_entry.place(x=333, y=70)
    middlename_entry.bind("<FocusIn>", middlename_delete)
    middlename_entry.bind("<FocusOut>", middlename_insert)
    middlename_entry.bind("<space>",middlename_caps)


    # LAST NAME
    def lastname_delete(o):
        if lastname_entry.get() == "Last Name":
            lastname_entry.configure(fg="black")
            lastname_entry.delete(0, "end")
    def lastname_insert(e):
        if len(lastname.get()) == 0:
            lastname_entry.configure(fg="grey")
            lastname_entry.insert(0, "Last Name")
        elif not lastname.get().isalpha() and lastname.get() != "Last Name":
            lastname_entry.delete(0, "end")
            lastname_entry.configure(fg="grey")
            lastname_entry.insert(0, "Last Name")
            # tmsg.showinfo("Name Error","Error.\nPlease Enter Valid Name Input.")
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 4.5)
            text_speech.say("Please enter valid last name")
            text_speech.runAndWait()
        else:
            str = lastname.get().title()
            lastname_entry.delete(0, "end")
            lastname_entry.insert(0, str)
    lastname = StringVar()
    lastname.set('')
    lastname_entry = Entry(second_frame, textvariable=lastname, font="cambria 13", width=16, relief=FLAT,
                        fg="grey", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
    lastname_insert(1)
    lastname_entry.place(x=503, y=70)
    lastname_entry.bind("<FocusIn>", lastname_delete)
    lastname_entry.bind("<FocusOut>", lastname_insert)
    # lastname_entry.bind("<Return>",lastname_insert)


    # BIRTH DATE
    Label(second_frame, text="Birth Date  : ", font="cambria 14 ",
        bg="white").place(x=60, y=135)  # x=860, y=65
    # DATE
    def date_insert(e):
        if len(date.get()) == 0:
            date_entry.insert(0, "Date")
        elif not date.get().isdigit() or int(date.get()) not in date_list:
            date_entry.delete(0, "end")
            date_entry.insert(0, "Date")
            # tmsg.showinfo("Birth Date Error","Error.\nPlease Enter Valid Date Input.")
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 4.5)
            text_speech.say("Please enter valid date of birth")
            text_speech.runAndWait()
    def date_delete(e):
        if date.get() == "Date":
            date_entry.delete(0, "end")
    date_list = list(range(1, 32))
    date = StringVar()
    date.set("Date")
    date_entry = ttk.Combobox(second_frame, textvariable=date,
                            font="cambria 13", width=14, state="normal", value=date_list)
    date_entry.place(x=165, y=140)  # x=980, y=65
    date_entry.bind("<FocusIn>", date_delete)
    date_entry.bind("<FocusOut>", date_insert)


    # MONTH
    def month_insert(e):
        if len(month.get()) != 0 and month.get()[0].islower():
            str = month.get()
            str = str.capitalize()
            month_entry.delete(0, "end")
            month_entry.insert(0, str)
        if len(month.get()) == 0:
            month_entry.insert(0, "Month")
        elif month.get() not in month_list:
            month_entry.delete(0, "end")
            month_entry.insert(0, "Month")
            # tmsg.showinfo("Birth Date Error","Error.\nPlease Enter Valid Month Input.")
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 4.5)
            text_speech.say("Please enter valid month of birth")
            text_speech.runAndWait()
    def month_delete(e):
        if month.get() == "Month":
            month_entry.delete(0, "end")
    month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
                'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month = StringVar()
    month.set("Month")
    month_entry = ttk.Combobox(second_frame, textvariable=month,
                            font="cambria 13", width=14, state="normal", value=month_list)
    month_entry.place(x=333, y=140)  # x=1180, y=65
    month_entry.bind("<FocusIn>", month_delete)
    month_entry.bind("<FocusOut>", month_insert)


    # YEAR
    def year_insert(e):
        if len(year.get()) == 0:
            year_entry.insert(0, "Year")
        elif not year.get().isdigit() or int(year.get()) not in year_list:
            year_entry.delete(0, "end")
            year_entry.insert(0, "Year")
            # tmsg.showinfo("Birth Date Error","Error.\nPlease Enter Valid Year Input.")
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 4.5)
            text_speech.say("Please enter valid year of birth")
            text_speech.runAndWait()
    def year_delete(e):
        if year.get() == "Year":
            year_entry.delete(0, "end")
    year_list = list(range(2022, 1979, -1))
    year = StringVar()
    year.set("Year")
    year_entry = ttk.Combobox(second_frame, textvariable=year,
                            font="cambria 13", width=14, state="normal", value=year_list)
    year_entry.place(x=503, y=140)  # x=1380, y=65
    year_entry.bind("<FocusIn>", year_delete)
    year_entry.bind("<FocusOut>", year_insert)


    # GENDER
    Label(second_frame, text="Gender       :",
        font="cambria 14 ", bg="white").place(x=60, y=210)
    gender_list = ['Female', 'Male', 'Others']
    gender = StringVar()
    gender.set("Select")
    gender_entry = ttk.Combobox(second_frame, textvariable=gender,
                                font="cambria 13", width=14, value=gender_list, state='readonly')
    gender_entry.place(x=165, y=210)


    # CATEGORY
    Label(second_frame, text="Category                      :",
        font="cambria 14 ", bg="white").place(x=800, y=210)
    category_list = ['General','Gen-EWS', 'OBC-A', 'OBC-B', 'SC', 'ST']
    category = StringVar()
    category.set('Select')
    category_entry = ttk.Combobox(second_frame, textvariable=category,
                                font="cambria 13", width=12, value=category_list, state=DISABLED)
    category_entry.place(x=980, y=210)


    # NATIONALITY
    Label(second_frame, text="Nationality                  :",
        font="cambria 14 ", bg="white").place(x=800, y=140)
    nationality_list = []
    nationality = StringVar()
    f = open("Nationality list.txt", 'r')
    text = f.read()
    final_text = ''
    for i in range(len(text)):
        final_text += text[i]
        if text[i] == '\n':
            nationality_list.append(final_text)
            final_text = ''
    nationality_entry = ttk.Combobox(
        second_frame, font="cambria 13", width=12, state='normal', textvariable=nationality)
    nationality_entry.place(x=980, y=140)
    # def focusout(event):
    #     if nationality_entry.get() not in nationality_list:
    #         nationality_entry.delete(0,'end')
    #         text_speech = pyttsx3.init()
    #         text_speech.setProperty("volume", 4.5)
    #         text_speech.say("Please enter valid nationality")
    #         text_speech.runAndWait()    
    def check(event):
        value = event.widget.get()
        if value == '':
            nationality_entry['values'] = nationality_list
        else:
            data = []
            for item in nationality_list:
                # if value.lower() in item.lower():
                if value.lower() == item[:len(value)].lower():
                    data.append(item)
            nationality_entry['values'] = data
    nationality_entry.bind('<Motion>', check)
    # nationality_entry.bind('<FocusOut>', focusout)


    # GUARDIAN NAME
    def guardian_insert(event):
        string = guardian.get().split(' ')
        for substr in string:
            if substr != '' and not substr.isalpha():
                guardian_entry.delete(0, "end")
                # tmsg.showinfo("Guardian's Name Error","Error.\nPlease Enter Valid Name Input.")
                text_speech = pyttsx3.init()
                text_speech.setProperty("volume", 4.5)
                text_speech.say("Please enter valid guardian's name")
                text_speech.runAndWait()
        else:
            guardian_caps(1)
    def guardian_caps(event):
        str = guardian.get().title()
        guardian_entry.delete(0, "end")
        guardian_entry.insert(0, str)
    Label(second_frame, text="Guardian's Name      :",
        font="cambria 14 ", bg="white").place(x=800, y=70)  # x=70,y=170
    guardian = StringVar()
    guardian_entry = Entry(second_frame, textvariable=guardian, font="cambria 13", width=32, relief=FLAT,
                        fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
    guardian_entry.place(x=980, y=70)  # x=245,y=170
    guardian_entry.bind("<FocusOut>", guardian_insert)
    guardian_entry.bind("<Return>", guardian_insert)
    guardian_entry.bind("<space>", guardian_caps)


    # IDENTIFICATION PROOF
    Label(second_frame, text="Identification Proof :",
        font="cambria 14 ", bg="white").place(x=800, y=280)
    identity_type = StringVar()
    identity_type.set('Select Type')
    identity_list = ['Aadhaar Card', 'Driving License',
                    'Election Commission Card', 'Pan Card', 'Passport']
    identity_combo = ttk.Combobox(second_frame, textvariable=identity_type,
                                font="cambria 13", width=12, value=identity_list, state="readonly")
    identity_combo.place(x=980, y=280)
    def identity_func1(event):
        if identity_type.get() != 'Select Type':
            identity_entry.configure(fg="black", state=NORMAL)
    def identity_func2(event):
        if len(identity_num.get()) == 0:
            identity_type.set('Select Type')
            identity_entry.configure(state=DISABLED)
        else:
            str = identity_num.get().upper()
            identity_entry.delete(0, 'end')
            identity_entry.insert(0, str)
    identity_num = StringVar()
    identity_entry = Entry(second_frame, textvariable=identity_num, font="cambria 13", width=16, relief=FLAT, fg="grey",
                        bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1, state='readonly')
    identity_entry.place(x=1122, y=280)
    identity_combo.bind("<FocusIn>", identity_func1)
    # identity_combo.bind("<Return>",identity_func1)
    identity_entry.bind("<FocusIn>", identity_func1)
    identity_entry.bind("<FocusOut>", identity_func2)
    # identity_entry.bind("<Return>",identity_func2)


    # PHONE NUMBER
    def phone_area_delete(event):
        if phone_area.get() == "Area Code":
            phone_area_entry.configure(fg="black")
            phone_area_entry.delete(0, "end")
            phone_num_entry.configure(state=NORMAL)
    def phone_area_insert(event):
        if len(phone_area.get()) == 0:
            phone_area_entry.delete(0, "end")
            phone_area_entry.configure(fg="grey")
            phone_area_entry.insert(0, "Area Code")
            phone_num_entry.delete(0, 'end')
            phone_num_entry.configure(fg='grey')
            phone_num_entry.insert(0, 'Number')
            phone_num_entry.configure(state=DISABLED)
        elif nationality.get() == 'Indian\n':
            category_entry.configure(state='readonly')
            if phone_area.get() == 'Area Code':
                phone_area_entry.configure(fg="black")
                phone_area_entry.delete(0, "end")
                phone_area_entry.insert(0, '+91')
                phone_num_entry.configure(state=NORMAL)
        elif nationality.get() != 'Indian\n' and nationality.get() != 'Select':
            category.set('Select')
            category_entry.configure(state=DISABLED)
        if len(phone_area.get()) != 0 and phone_area.get() != 'Area Code':
            str = phone_area.get()
            if (not str[0].isdigit() and str[0] != '+') or (len(str) > 1 and not str[1:].isdigit()):
                phone_area_entry.delete(0, "end")
                phone_area_entry.configure(fg="grey")
                phone_area_entry.insert(0, "Area Code")
                #tmsg.showinfo("Phone Number Error",
                text_speech = pyttsx3.init()
                text_speech.setProperty("volume", 4.5)
                text_speech.say("Please enter valid Area code")
                text_speech.runAndWait()            
            phone_num_entry.configure(state=NORMAL)
    Label(second_frame, text="Phone No. : ",
        font="cambria 14 ", bg="white").place(x=60, y=280)
    phone_area = StringVar()
    phone_area.set('Area Code')
    phone_area_entry = Entry(second_frame, textvariable=phone_area, font="cambria 13", width=9, relief=FLAT,
                            fg="grey", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
    phone_area_entry.place(x=165, y=280)
    phone_area_entry.bind("<FocusIn>", phone_area_delete)
    phone_area_entry.bind("<FocusOut>", phone_area_insert)
    # phone_area_entry.bind("<Return>",phone_area_insert)
    nationality_entry.bind("<FocusIn>", phone_area_insert)

    def phone_num_delete(event):
        if phone_num.get() == "Number":
            phone_num_entry.delete(0, "end")
        if len(phone_num.get()) == 0:
            phone_num_entry.configure(fg="black")
    def phone_num_insert(event):
        if len(phone_num.get()) == 0:
            phone_num_entry.configure(fg="grey")
            phone_num_entry.insert(0, "Number")
        elif phone_num.get() != 'Number' and not phone_num.get().isdigit():
            phone_num_entry.delete(0, "end")
            phone_num_entry.configure(fg="grey")
            phone_num_entry.insert(0, "Number")
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 4.5)
            text_speech.say("Please enter valid Phone Number")
            text_speech.runAndWait()           
        elif phone_area.get() == '+91' and len(phone_num.get()) != 10:
            phone_num_entry.delete(0, "end")
            phone_num_entry.configure(fg="grey")
            phone_num_entry.insert(0, "Number")
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 4.5)
            text_speech.say("Please enter 10 digit Phone Number")
            text_speech.runAndWait()
    phone_num = StringVar()
    phone_num.set('Number')
    phone_num_entry = Entry(second_frame, textvariable=phone_num, font="cambria 13", width=18, relief=FLAT, fg="grey",
                            bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1, state="readonly")
    phone_num_entry.place(x=260, y=280)
    phone_num_entry.bind("<FocusIn>", phone_num_delete)
    phone_num_entry.bind("<FocusOut>", phone_num_insert)
    # phone_num_entry.bind("<Return>",phone_num_insert)


    #  EMAIL
    def email_func(e):
        if not email_entry.get().islower():
            str = email.get().lower()
            email_entry.delete(0, 'end')
            email_entry.insert(0, str)
    def email_delete(event):
        if email.get() == 'nameexample@gmail.com':
            email_entry.delete(0, 'end')
            email_entry.configure(fg='black')
    def email_insert(event):
        if len(email.get()) == 0:
            email_entry.configure(fg='grey')
            email_entry.insert(0, 'nameexample@gmail.com')
        elif email.get()[-10:] != '@gmail.com':
            email_entry.delete(0, 'end')
            email_entry.configure(fg='grey')
            email_entry.insert(0, 'nameexample@gmail.com')
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 4.5)
            text_speech.say("Please enter valid email id")
            text_speech.runAndWait()
        else:
            str = email.get()[-11::-1]
            email_list = str.split('.')
            for x in email_list:
                if not x.isalnum():
                    email_entry.delete(0, 'end')
                    email_entry.configure(fg='grey')
                    email_entry.insert(0, 'nameexample@gmail.com')
                    text_speech = pyttsx3.init()
                    text_speech.setProperty("volume", 4.5)
                    text_speech.say("Please enter valid email id")
                    text_speech.runAndWait()
    Label(second_frame, text='Email Address           :',
        font="cambria 14 ", bg="white").place(x=800, y=350)
    email = StringVar()
    email.set('nameexample@gmail.com')
    email_entry = Entry(second_frame, textvariable=email, font="cambria 13", width=32, relief=FLAT,
                        fg="grey", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
    email_entry.place(x=980, y=350)
    email_entry.bind('<FocusIn>', email_delete)
    email_entry.bind('<FocusOut>', email_insert)
    # email_entry.bind('<Return>',email_insert)
    email_entry.bind('<KeyRelease>', email_func)

    # PWD
    Label(second_frame, text='Are you Physically Disabled?  :',
        font="cambria 14 ", bg="white").place(x=60, y=350)
    pwd = StringVar()
    pwd.set('Select')
    pwd_entry = ttk.Combobox(second_frame, textvariable=pwd,
                            font="cambria 13", width=7, value=['Yes', 'No'], state="readonly")
    pwd_entry.place(x=310, y=350)


    # ADDRESS
    Label(second_frame, text="House No. :",
        font="cambria 14", bg="white").place(x=60, y=530)
    house = StringVar()
    Entry(second_frame, textvariable=house, font="cambria 13", bg="white", width=32, fg="black", relief=FLAT,
        highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1).place(x=165, y=530)

    Label(second_frame, text="Street      :",
        font="cambria 14", bg="white").place(x=800, y=530)
    street = StringVar()
    Entry(second_frame, textvariable=street, font="cambria 14", bg="white", fg="black", width=35, relief=FLAT,
        highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1).place(x=890, y=530)

    Label(second_frame, text="City             :",
        font="cambria 14", bg="white").place(x=60, y=600)
    city = StringVar()
    Entry(second_frame, textvariable=city, font="cambria 13", width=32, relief=FLAT, fg="black",
        highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1).place(x=165, y=600)

    Label(second_frame, text="State        :",
        font="cambria 14", bg="white").place(x=800, y=600)
    state = StringVar()
    Entry(second_frame, textvariable=state, font="cambria 13", relief=FLAT, fg="black",
        highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1, width=32).place(x=890, y=600)

    Label(second_frame, text="Country    :",
        font="cambria 14", bg="white").place(x=60, y=680)
    country = StringVar()
    Entry(second_frame, textvariable=country, font="cambria 13", width=32, relief=FLAT, fg="black",
        highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1).place(x=165, y=680)

    Label(second_frame, text="Pin Code :",
        font="cambria 14", bg="white").place(x=800, y=680)
    pin = StringVar()
    Entry(second_frame, textvariable=pin, font="cambria 13", width=32, relief=FLAT, fg="black",
        highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1).place(x=890, y=680)



    # EDUCATION DETAILS
    Label(second_frame, text="University Name :",
        font="cambria 14 ", bg="white").place(x=60, y=870)
    uni_name = StringVar()
    Entry(second_frame, textvariable=uni_name, font="cambria 13", width=40, relief=FLAT, fg="black", bg="white",
        highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1).place(x=215, y=870)

    Label(second_frame, text="College Name         :",
        font="cambria 14 ", bg="white").place(x=800, y=870)
    college_name = StringVar()
    Entry(second_frame, textvariable=college_name, font="cambria 13", width=36, relief=FLAT, fg="black",
        bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1).place(x=960, y=870)

    Label(second_frame, text="Stream                    :",
        font="cambria 14 ", bg="white").place(x=60, y=940)
    stream = StringVar()
    stream_list = ["Civil Engineering", "Computer Science and Engineering", "Electrical Engineering",
                "Electrical and Electronics Engineering", "Electronics and Communication Engineering", "Mechanical Engineering"]
    stream.set('Select')
    stream_entry = ttk.Combobox(second_frame, textvariable=stream,
                                font="cambria 13", width=38, value=stream_list, state="readonly")
    stream_entry.place(x=215, y=940)

    Label(second_frame, text="Current Semester :",
        font="cambria 14 ", bg="white").place(x=800, y=940)
    sem_year = StringVar()
    sem_year_list = ["First", "Second", "Third",
                    "Fourth", "Fifth", "Sixth", "Seventh", "Eighth"]
    sem_year.set('Select')
    sem_entry = ttk.Combobox(second_frame, textvariable=sem_year,
                            font="cambria 13", width=19, value=sem_year_list, state="readonly")
    sem_entry.place(x=960, y=940)

    Label(second_frame, text="College Id              :",
        font="cambria 14 ", bg="white").place(x=60, y=1010)
    name = StringVar()
    Entry(second_frame, textvariable=name, font="cambria 13", width=40, relief=FLAT, fg="black", bg="white",
        highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1).place(x=215, y=1010)



    # RADIO BUTTON
    radiobutton_frame = LabelFrame(
        second_frame, bg="#fafa7d", width=650, height=280, relief=SOLID)
    radiobutton_frame.pack(padx=30, pady=20)
    Label(radiobutton_frame, text="CHOOSE THE TOPIC FOR WHICH YOU WANT TO COMPETE:",
        font="alegreya 16 bold underline", bg="#fafa7d").place(x=20, y=20)
    var = IntVar()
    Radiobutton(radiobutton_frame, text="  Internet of Things(IOT)", activebackground='white',
                            font="Cambria 15 bold", bg="#fafa7d", cursor="target", variable=var, value=1, bd=10).place(x=10, y=60)
    Radiobutton(radiobutton_frame, text="  Machine Learning", activebackground="white",
                            font="Cambria 15 bold", bg="#fafa7d", cursor="target", variable=var, value=2, bd=10).place(x=10, y=110)
    Radiobutton(radiobutton_frame, text="  Artificial Intelligence(AI) and Robotics", activebackground="white",
                            font="Cambria 15 bold", bg="#fafa7d", cursor="target", variable=var, value=3, bd=10).place(x=10, y=160)
    Radiobutton(radiobutton_frame, text="  Big Data", activebackground="white",
                            font="Cambria 15 bold", bg="#fafa7d", cursor="target", variable=var, value=4, bd=10).place(x=10, y=210)


    # TERMS & CONDITION AND SUBMIT BUTTON
    submit_frame = Frame(second_frame, bg="white",
                        width=Width-70, height=150, relief=SOLID)
    submit_frame.pack(pady=40, padx=0)

    canvas = Canvas(submit_frame, width=Width-70, height=150,
                    bg='white', highlightbackground='white')
    canvas.pack()
    canvas.create_rectangle(0, 0, Width-50, 6, fill='black', outline='gray60')

    check_var = IntVar()
    b = Checkbutton(submit_frame, variable=check_var, text="I agree to the",
                    font="calibri 16 bold", bg="white", activebackground='white', selectcolor='gray85')
    b.place(x=20, y=37)
    b.deselect()

    my_link = Label(submit_frame, text="terms & conditions ",
                    font="calibri 16 bold underline", cursor='hand2', fg='blue', bg="white")
    my_link.place(x=165, y=40)
    my_link.bind('<Button-1>', lambda x: webbrowser.open_new(
        "https://extra.codemotion.com/the-code-factor-coding-challenge-terms-conditions/"))


    # CHECKING FOR ALL FILLED AREA
    def validate():
        global submit_flag
        if firstname.get() == 'First Name':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter first name")
            text_speech.runAndWait()
        elif guardian.get() == '':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter guardian's name")
            text_speech.runAndWait()
        elif date.get() == 'Date':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter date of birth")
            text_speech.runAndWait()
        elif month.get() == 'Month':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter month of birth")
            text_speech.runAndWait()
        elif year.get() == 'Year':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter year of birth")
            text_speech.runAndWait()
        elif nationality.get() == '' or nationality.get() not in nationality_list:
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter your nationality")
            text_speech.runAndWait()
        elif nationality.get() == 'Indian\n' and category.get() == 'Select':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please select your category")
            text_speech.runAndWait()
        elif gender.get() == '' or gender.get() == 'Select':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter your gender")
            text_speech.runAndWait()
        elif identity_type.get() == 'Select Type':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please select identity proof")
            text_speech.runAndWait()
        elif identity_num.get() == '':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter your identity proof details")
            text_speech.runAndWait()
        elif phone_area.get() == 'Area Code':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter area code")
            text_speech.runAndWait()
        elif phone_num.get() == 'Number':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter phone no.")
            text_speech.runAndWait()
        elif email.get() == '' or email.get() == 'nameexample@gmail.com':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter email id")
            text_speech.runAndWait()
        elif pwd.get() == 'Select':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter if you are physically disabled or not")
            text_speech.runAndWait()
        elif house.get() == '':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please complete your address details")
            text_speech.runAndWait()
        elif street.get() == '':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please complete your address details")
            text_speech.runAndWait()
        elif state.get() == '':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter your state")
            text_speech.runAndWait()
        elif city.get() == '':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter your city")
            text_speech.runAndWait()
        elif country.get() == '':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter your country")
            text_speech.runAndWait()
        elif pin.get() == '':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter your pin code")
            text_speech.runAndWait()
        elif uni_name.get() == '':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter university name")
            text_speech.runAndWait()
        elif college_name.get() == '':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter college name")
            text_speech.runAndWait()
        elif stream.get() == 'Select':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter your stream")
            text_speech.runAndWait()
        elif sem_year.get() == 'Select':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter your current semester")
            text_speech.runAndWait()
        elif name.get() == '':
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please enter college id")
            text_speech.runAndWait()
        elif var.get() == 0:
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please choose the one for which you want to compete")
            text_speech.runAndWait()
        elif check_var.get() == 0:
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Please agree to the terms and conditions")
            text_speech.runAndWait()
        else:
            text_speech = pyttsx3.init()
            text_speech.setProperty("volume", 7)
            text_speech.say("Your form has been successfully submitted")
            text_speech.runAndWait()
            messagebox.showinfo(
                "Submitted Successfully", f"Your form has been successfully submitted {firstname.get()}.\nIf you have any further questions please visit support option in the home page menu.")
            save(1)
            secondroot.destroy()

    submit_button = Button(submit_frame, text="SUBMIT", command=validate, font="timesnewroman 14 bold",
                        fg='white', width=8, bg="seagreen", relief=GROOVE, activeforeground='seagreen')
    submit_button.place(x=Width-200, y=35)

    # CLEAR
    def clear():
        firstname_entry['fg'] = 'grey'
        firstname.set("First Name")
        middlename_entry['fg'] = 'grey'
        middlename.set("Middle Name")
        lastname_entry['fg'] = 'grey'
        lastname.set("Last Name")
        guardian.set("")
        date.set("Date")
        month.set("Month")
        year.set("Year")
        nationality.set("")
        gender.set("Select")
        identity_type.set("Select Type")
        identity_num.set("")
        phone_area_entry['fg'] = 'grey'
        phone_area.set("Area Code")
        phone_num_entry['fg'] = 'grey'
        phone_num.set("Number")
        email_entry['fg'] = 'grey'
        email.set("nameexample@gmail.com")
        pwd.set("Select")
        house.set("")
        street.set("")
        city.set("")
        state.set("")
        country.set("")
        pin.set("")
        uni_name.set("")
        college_name.set("")
        stream.set("Select")
        sem_year.set("Select")
        name.set("")
        var.set(0)

    Button(submit_frame, text='CLEAR', font='timesnewroman 14 bold', fg='white',
        bg='gray30', command=clear, width=8, height=1, relief=GROOVE).place(x=Width-330, y=36)


    # SAVING DATA IN EXCEL FILE
    workbook = openpyxl.load_workbook('FormData.xlsx')
    worksheet = workbook.active

    def save(e):
        if middlename.get() == 'Middle Name':
            middlenamestr = ' '
        else:
            middlenamestr = middlename.get()
        if lastname.get() == 'Last Name':
            lastnamestr = ' '
        else:
            lastnamestr = lastname.get()
        if category.get() == 'Select':
            categorystr = ' '
        else:
            categorystr = category.get()
        if var.get() == 1:
            radiobutton_value = "Internet of Things(IOT)"
        elif var.get() == 2:
            radiobutton_value = "Machine Learning"
        elif var.get() == 3:
            radiobutton_value = "Artificial Intelligence(AI)and Robotics"
        elif var.get() == 4:
            radiobutton_value = "Big Data"

        userdata_list = [firstname.get(), middlenamestr, lastnamestr, date.get(), month.get(), year.get(), gender.get(), guardian.get(), nationality.get(), categorystr, pwd.get(), identity_type.get(), identity_num.get(), phone_area.get(), phone_num.get(), email.get(), house.get(), street.get(), city.get(), state.get(), country.get(), pin.get(), uni_name.get(), college_name.get(), stream.get(), sem_year.get(), name.get(), radiobutton_value]

        worksheet.append(userdata_list)
        workbook.save('FormData.xlsx')

    secondroot.mainloop()
