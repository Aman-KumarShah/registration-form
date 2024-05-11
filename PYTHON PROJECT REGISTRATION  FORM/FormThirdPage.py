from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import openpyxl


def third_page(root):
      root = Toplevel(root)
      root.title("BrainHacks Filled Application Form")
      root.configure(bg="white")
      root.wm_iconbitmap("stceticon.ico")
      Width = root.winfo_screenwidth()
      Height = root.winfo_screenheight()
      root.geometry(f"{Width}x{Height}+-6+0")
      root.minsize(Width, Height)

      # HEADING - CAPTIONS
      f0 = Frame(root, width=Width, heigh=75, bg="#92c8d6",relief=GROOVE, borderwidth=2)
      f0.pack(fill=X)
      Label(f0, text="BRAINHACKS", font="widelatin 40 bold",
            bg="#92c8d6").place(x=85, y=3)

      def update():
            l0.config(text="|", fg='white')
            e0.config(text="Let's Code", fg='white')
            e0.after(2000, myfunc)
      def myfunc():
            l0.config(text="|", fg='white')
            e0.config(text="Let's Compete", fg='white')
            e0.after(2000, update)

      l0 = Label(f0, text="", font="widelatin 35 bold", bg="#92c8d6", fg="white")
      l0.place(x=455, y=1)
      e0 = Label(f0, text='', font="arialblack 25 bold", bg="#92c8d6", fg="white")
      e0.place(x=485, y=18)
      e0.after(2000, myfunc)


      # HEADING - IMAGES(ICONS)
      image2 = Image.open("icon1.png").resize((60, 60))
      photo2 = ImageTk.PhotoImage(image2)
      Label(f0,image=photo2, bg="#92c8d6").place(x=15, y=5)

      image3 = Image.open("icon2.png").resize((78, 66))
      photo3 = ImageTk.PhotoImage(image3)
      Label(f0,image=photo3, bg="#92c8d6").place(x=Width-195, y=1)

      image1 = Image.open("icon3.png").resize((70, 66))
      photo1 = ImageTk.PhotoImage(image1)
      Label(f0,image=photo1, bg="#92c8d6").place(x=Width-93, y=1)



      # CREATING ANOTHER WINDOW
      main_frame = Frame(root, bg="white")
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
      my_canvas.create_window((25, 105), window=second_frame, anchor="nw")

      my_canvas.create_rectangle(15, 20, Width-35, 40, fill='white', outline='white')
      my_canvas.create_rectangle(15, 40, Width-35, 100,
                              fill='lightcyan4')  # thistle4
      my_canvas.create_text(Width/2, 70, text='YOUR FILLED APPLICATION FORM',
                        font='alegreya 25 bold', fill='white')
      my_canvas.create_rectangle(15, 100, Width-35, 1450, fill='white')
      my_canvas.create_rectangle(15, 1452, Width-35, 1700,
                              fill='white', outline='white')


      # LABELFRAMES
      LabelFrame(second_frame, text=" PERSONAL DETAILS", font="alegreya 17 bold underline", bg="white",
            width=Width-100, height=400, bd=2, fg="black", relief=GROOVE).pack(padx=15, pady=20)
      LabelFrame(second_frame, text="ADDRESS", font="alegreya 17 bold underline",
            bg="white", width=Width-100, height=300, relief=GROOVE).pack(pady=20, padx=15)
      LabelFrame(second_frame, text="EDUCATIONAL DETAILS", font="alegreya 17 bold underline",
            bg="white", width=Width-100, height=290, relief=GROOVE).pack(pady=20, padx=15)


      # PERSONAL DETAILS
      # NAME
      Label(second_frame, text="Name           :",
            font="cambria 14 ", bg="white").place(x=35, y=70)
      firstname = StringVar()
      firstname_entry = Entry(second_frame, textvariable=firstname, font="cambria 13", width=16, relief=FLAT,
                              fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      firstname_entry.place(x=145, y=70)

      middlename = StringVar()
      middlename_entry = Entry(second_frame, textvariable=middlename, font="cambria 13", width=16, relief=FLAT,
                              fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      middlename_entry.place(x=313, y=70)

      lastname = StringVar()
      lastname.set('')
      lastname_entry = Entry(second_frame, textvariable=lastname, font="cambria 13", width=16, relief=FLAT,
                        fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      lastname_entry.place(x=479, y=70)

      # BIRTH DATE
      Label(second_frame, text="Birth Date  : ",
            font="cambria 14 ", bg="white").place(x=35, y=135)
      date = StringVar()
      date_entry = ttk.Combobox(second_frame, textvariable=date,
                              font="cambria 13", width=14, state="normal")
      date_entry.place(x=145, y=140)
      month = StringVar()
      month_entry = ttk.Combobox(
      second_frame, textvariable=month, font="cambria 13", width=14, state="normal")
      month_entry.place(x=313, y=140)
      year = StringVar()
      year_entry = ttk.Combobox(second_frame, textvariable=year,
                              font="cambria 13", width=14, state="normal")
      year_entry.place(x=478, y=140)

      # GENDER
      Label(second_frame, text="Gender       :",
            font="cambria 14 ", bg="white").place(x=35, y=215)
      gender = StringVar()
      gender_entry = ttk.Combobox(
      second_frame, textvariable=gender, font="cambria 13", width=14, state='readonly')
      gender_entry.place(x=145, y=215)

      # CATEGORY
      Label(second_frame, text="Category                      :",
            font="cambria 14 ", bg="white").place(x=780, y=215)
      category = StringVar()
      category_entry = ttk.Combobox(
      second_frame, textvariable=category, font="cambria 13", width=12)
      category_entry.place(x=960, y=215)

      # NATIONALITY
      Label(second_frame, text="Nationality                  :",
            font="cambria 14 ", bg="white").place(x=780, y=140)
      nationality = StringVar()
      nationality_entry = ttk.Combobox(
      second_frame, textvariable=nationality, font="cambria 13", width=12)
      nationality_entry.place(x=960, y=140)

      #GUARDIAN NAME
      Label(second_frame, text="Guardian's Name      :",
            font="cambria 14 ", bg="white").place(x=780, y=70)
      guardian = StringVar()
      guardian_entry = Entry(second_frame, textvariable=guardian, font="cambria 13", width=32, relief=FLAT,
                        fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      guardian_entry.place(x=960, y=70)

      # IDENTIFICATION PROOF
      Label(second_frame, text="Identification Proof :",
            font="cambria 14 ", bg="white").place(x=780, y=280)
      identity_type = StringVar()
      identity_combo = ttk.Combobox(
      second_frame, textvariable=identity_type, font="cambria 13", width=12, state="readonly")
      identity_combo.place(x=960, y=280)
      identity_num = StringVar()
      identity_entry = Entry(second_frame, textvariable=identity_num, font="cambria 13", width=16, relief=FLAT,
                        fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      identity_entry.place(x=1102, y=280)

      # PHONE NUMBER
      Label(second_frame, text="Phone No. : ",
            font="cambria 14 ", bg="white").place(x=35, y=280)
      phone_area = StringVar()
      phone_area_entry = Entry(second_frame, textvariable=phone_area, font="cambria 13", width=9, relief=FLAT,
                              fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      phone_area_entry.place(x=145, y=280)
      phone_num = StringVar()
      phone_num_entry = Entry(second_frame, textvariable=phone_num, font="cambria 13", width=18, relief=FLAT,
                              fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1,)
      phone_num_entry.place(x=240, y=280)

      # EMAIL ID
      Label(second_frame, text='Email Address           :',
            font="cambria 14 ", bg="white").place(x=780, y=350)
      email = StringVar()
      email_entry = Entry(second_frame, textvariable=email, font="cambria 13", width=32, relief=FLAT,
                        fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      email_entry.place(x=960, y=350)

      # PWD
      Label(second_frame, text='Are you Physically Disabled? :',
            font="cambria 14 ", bg="white").place(x=35, y=350)
      pwd = StringVar()
      pwd_entry = ttk.Combobox(second_frame, textvariable=pwd,
                              font="cambria 13", width=7)
      pwd_entry.place(x=290, y=350)


      # ADDRESS
      # HOUSE NO
      Label(second_frame, text="House No. :",
            font="cambria 14", bg="white").place(x=35, y=530)
      house = StringVar()
      house_entry = Entry(second_frame, textvariable=house, font="cambria 13", bg="white", width=32,
                        fg="black", relief=FLAT, highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      house_entry.place(x=145, y=530)

      # STREET 
      Label(second_frame, text="Street      :",
            font="cambria 14", bg="white").place(x=780, y=530)
      street = StringVar()
      street_entry = Entry(second_frame, textvariable=street, font="cambria 14", bg="white", fg="black",
                        width=35, relief=FLAT, highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      street_entry.place(x=870, y=530)

      # CITY
      Label(second_frame, text="City             :",
            font="cambria 14", bg="white").place(x=35, y=600)
      city = StringVar()
      city_entry = Entry(second_frame, textvariable=city, font="cambria 13", width=32, relief=FLAT,
                        fg="black", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      city_entry.place(x=145, y=600)

      # STATE
      Label(second_frame, text="State        :",
            font="cambria 14", bg="white").place(x=780, y=600)
      state = StringVar()
      state_entry = Entry(second_frame, textvariable=state, font="cambria 13", relief=FLAT, fg="black",
                        highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1, width=32)
      state_entry.place(x=870, y=600)

      # COUNTRY
      Label(second_frame, text="Country    :",
            font="cambria 14", bg="white").place(x=35, y=680)
      country = StringVar()
      country_entry = Entry(second_frame, textvariable=country, font="cambria 13", width=32, relief=FLAT,
                        fg="black", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      country_entry.place(x=145, y=680)

      # PIN CODE
      Label(second_frame, text="Pin Code :",
            font="cambria 14", bg="white").place(x=780, y=680)
      pin = StringVar()
      pin_entry = Entry(second_frame, textvariable=pin, font="cambria 13", width=32, relief=FLAT,
                        fg="black", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      pin_entry.place(x=870, y=680)


      # EDUCATION DETAILS
      # UNIVERSITY NAME
      Label(second_frame, text="University Name :",
            font="cambria 14 ", bg="white").place(x=35, y=870)
      uni_name = StringVar()
      uni_name_entry = Entry(second_frame, textvariable=uni_name, font="cambria 13", width=40, relief=FLAT,
                        fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      uni_name_entry.place(x=195, y=870)

      # COLLEGE NAME
      Label(second_frame, text="College Name         :",
            font="cambria 14 ", bg="white").place(x=780, y=870)
      college_name = StringVar()
      college_name_entry = Entry(second_frame, textvariable=college_name, font="cambria 13", width=35, relief=FLAT,
                              fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      college_name_entry.place(x=940, y=870)

      # STREAM
      Label(second_frame, text="Stream                    :",
            font="cambria 14 ", bg="white").place(x=35, y=940)
      stream = StringVar()
      stream_entry = ttk.Combobox(
      second_frame, textvariable=stream, font="cambria 13", width=38, state="readonly")
      stream_entry.place(x=195, y=940)

      # CURRENT SEMESTER
      Label(second_frame, text="Current Semester :",
            font="cambria 14 ", bg="white").place(x=780, y=940)
      sem_year = StringVar()
      sem_entry = ttk.Combobox(second_frame, textvariable=sem_year,
                              font="cambria 13", width=19, state="readonly")
      sem_entry.place(x=940, y=940)

      # COLLEGE ID
      Label(second_frame, text="College Id              :",
            font="cambria 14 ", bg="white").place(x=35, y=1010)
      college_id = StringVar()
      college_id_entry = Entry(second_frame, textvariable=college_id, font="cambria 13", width=40, relief=FLAT,
                              fg="black", bg="white", highlightbackground="grey", highlightcolor="#0a75bf", highlightthickness=1)
      college_id_entry.place(x=195, y=1010)

      # TOPIC TO COMPETE 
      radiobutton_frame = LabelFrame(
      second_frame, bg="#fafa7d", width=650, height=150, relief=GROOVE)
      radiobutton_frame.pack(padx=30, pady=20)
      Label(radiobutton_frame, text="THE TOPIC CHOSEN FOR THE COMPETITION:",
            font="alegreya 15 bold underline", bg="#fafa7d").place(x=100, y=20)
      var = IntVar()


      # SHOW DATA FROM EXCEL FILE
      workbook = openpyxl.load_workbook('FormData.xlsx')
      worksheet = workbook.active
      row = worksheet[f'{worksheet.max_row}']

      firstname_entry.insert(0, row[0].value)
      firstname_entry.config(state='readonly')

      middlename_entry.insert(0, row[1].value)
      middlename_entry.config(state='readonly')

      lastname_entry.insert(0, row[2].value)
      lastname_entry.config(state='readonly')

      date_entry.set(row[3].value)
      date_entry.config(state='readonly')

      month_entry.set(row[4].value)
      month_entry.config(state='readonly')

      year_entry.set(row[5].value)
      year_entry.config(state='readonly')

      gender_entry.set(row[6].value)
      # gender_entry.config(state='readonly')

      guardian_entry.insert(0, row[7].value)
      guardian_entry.config(state='readonly')

      nationality_entry.insert(0, row[8].value)
      nationality_entry.config(state='readonly')

      category_entry.set(row[9].value)
      category_entry.config(state='readonly')

      pwd_entry.set(row[10].value)
      pwd_entry.config(state='readonly')

      identity_combo.set(row[11].value)
      identity_combo.config(state='readonly')

      identity_entry.insert(0, row[12].value)
      identity_entry.config(state='readonly')

      phone_area_entry.insert(0, row[13].value)
      phone_area_entry.config(state='readonly')

      phone_num_entry.insert(0, row[14].value)
      phone_num_entry.config(state='readonly')

      email_entry.insert(0, row[15].value)
      email_entry.config(state='readonly')

      house_entry.insert(0, row[16].value)
      house_entry.config(state='readonly')

      street_entry.insert(0, row[17].value)
      street_entry.config(state='readonly')

      city_entry.insert(0, row[18].value)
      city_entry.config(state='readonly')

      state_entry.insert(0, row[19].value)
      state_entry.config(state='readonly')

      country_entry.insert(0, row[20].value)
      country_entry.config(state='readonly')

      pin_entry.insert(0, row[21].value)
      pin_entry.config(state='readonly')

      uni_name_entry.insert(0, row[22].value)
      uni_name_entry.config(state='readonly')

      college_name_entry.insert(0, row[23].value)
      college_name_entry.config(state='readonly')

      stream_entry.set(row[24].value)
      # stream_entry.config(state='readonly')

      sem_entry.set(row[25].value)
      # sem_entry.config(state='readonly')

      college_id_entry.insert(0, row[26].value)
      college_id_entry.config(state='readonly')

      Radiobutton(radiobutton_frame, text=row[27].value, activebackground='#fafa7d',
                  font="Cambria 15 bold", bg="#fafa7d", cursor="target", bd=10).place(x=90, y=60)

      Frame(second_frame,width=Width-70,height=1,bg='black').place(x=0,y=1345)
      # back_button = Button(second_frame,text=' BACK ',bg='gray30',fg='white',font="timesnewroman 14 bold",relief=GROOVE).pack(anchor='sw',pady=80)
      back_button = ttk.Button(second_frame,text='Back',width=8,cursor='hand2')
      back_button.pack(anchor='sw',pady=80)
      def close(event):
            root.destroy()
      back_button.bind('<Button-1>',close)
      root.mainloop()
