#PROJECT - 7

import customtkinter
import tkinter as tk
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

#////////////////////////////////////////////////////////////////////////////////////////////#

r7 = customtkinter.CTk()
r7.title(" ")

r6 = customtkinter.CTk()
r6.title(" ")

r5 = customtkinter.CTk()
r5.title(" ")

r4 = customtkinter.CTk()
r4.title(" ")

r3 = customtkinter.CTk()
r3.title("RECIPE APP")

r2 = customtkinter.CTk()
r2.title("LOGIN")

r1 = customtkinter.CTk()
r1.title("REGISTER")

#////////////////////////////////////////////////////////////////////////////////////////////#

conn = sqlite3.connect("data7.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')




#////////////////////////////////////////////////////////////////////////////////////////////#

def signup():
    username = username_entry_register.get()
    password = password_entry_register.get()
    if ((username != "") and (password != "")):
        cursor.execute("SELECT username FROM users WHERE username=?", [username])
        if(cursor.fetchone() is not None):
            messagebox.showerror("Error","Username already exists!")
        else:
            encodedpassword = password.encode("utf-8")
            hashedpassword = bcrypt.hashpw(encodedpassword, bcrypt.gensalt())
            print(hashedpassword)
            cursor.execute("INSERT into users VALUES(?, ?)", [username, hashedpassword])
            conn.commit()
            messagebox.showinfo("Sucsess!","Account has been created")
            register_to_login_page_button = customtkinter.CTkButton(master=r1,
                                                                    text="Go to Login Page",
                                                                    command=login,)
            register_to_login_page_button.place(relx=0.5, rely=0.6, anchor = tk.CENTER)
    else:
        messagebox.showerror("Error","Enter all data.")

def register_to_login_page():
    r1.destroy()
    frame2 = customtkinter.CTkFrame(master=r2,
                                    width=350,
                                    height=350)
    frame2.pack(padx=20,pady=20)

    global username_entry_login
    global password_entry_login

    username_entry_login = customtkinter.CTkEntry(master=frame2,
                                                placeholder_text="Username",
                                                width=150,
                                                height=40)
    username_entry_login.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

    password_entry_login = customtkinter.CTkEntry(master=frame2,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
    password_entry_login.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

    verification_button = customtkinter.CTkButton(master=frame2,
                                          text="Verify and Continue!",
                                          command=loginaccount)
    verification_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
    r2.mainloop()

def login():


    r1.destroy()
    frame2 = customtkinter.CTkFrame(master=r2,
                                    width=350,
                                    height=350)
    frame2.pack(padx=20,pady=20)

    global username_entry_login
    global password_entry_login

    username_entry_login = customtkinter.CTkEntry(master=frame2,
                                                placeholder_text="Username",
                                                width=150,
                                                height=40)
    username_entry_login.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

    password_entry_login = customtkinter.CTkEntry(master=frame2,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
    password_entry_login.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

    verification_button = customtkinter.CTkButton(master=frame2,
                                          text="Verify and Continue!",
                                          command=loginaccount)
    verification_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
    r2.mainloop()

def loginaccount():

    
    username = username_entry_login.get()
    password = password_entry_login.get()
    if ((username != "") and (password != "")):
        cursor.execute("SELECT password FROM users WHERE username=?", [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode("utf-8"), result[0]):
                messagebox.showinfo("Success", f"Logged in successfully, Welcome {username}")
                #////////////////////////////////////////////////////////////////////////////////////////////#

                r2.destroy()

                #////////////////////////////////////////////////////////////////////////////////////////////#

                def user_info_saver_button_func():
                    user_kg = user_kg_entry.get().strip()
                    user_waist = user_waist_circumfrence_entry.get().strip()
                    user_height = user_height_entry.get().strip()
                    user_neck = user_neck_circumfrence_entry.get().strip()

                    if not all([user_kg, user_waist, user_height, user_neck]):
                        messagebox.showerror("Error", "Please fill all the entries")

                    else:
                        messagebox.showinfo("Sucsess","Wellcome")
                        r3.destroy()

                    #////////////////////////////////////////////////////////////////////////////////////////////#

                        def lose_weight_button_func():
                            r4.destroy()

                            big_frame = customtkinter.CTkFrame(master=r5, width=800, height=500)
                            big_frame.pack(padx=20, pady=20)

                            lose_weight_frame = customtkinter.CTkFrame(master=big_frame, width=800, height=400)
                            lose_weight_frame.pack(padx=20, pady=20)
                            
                            tabview = customtkinter.CTkTabview(lose_weight_frame, width=400, height=400)
                            tabview.pack(padx=20, pady=20)

                            tabview.add("Beginer")
                            tabview.add("Intermediate")
                            tabview.add("Upper-Intermediate")

                            l_tabview_label = customtkinter.CTkLabel(master=lose_weight_frame,text="LOSE WEIGHT TRAINING",font=("Arial", 18))
                            l_tabview_label.place(relx=0.257,rely=0)


                            beginer_tabview_label = customtkinter.CTkLabel(tabview.tab("Beginer"), text='''
                                                                        -Crunch 3 sets 12 reps
                                                                        -Plank 3 sets 12 reps
                                                                        -Squats 3 set 12 reps
                                                                        -1 hr cardio
                                                                        ''')

                            beginer_tabview_label.place(relx=-0.23, rely=0.1)

                            intermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Intermediate"), text='''
                                                                        -Crunch 4 sets 12 reps
                                                                        -Plank 4 sets 12 reps
                                                                        -Squats 4 set 12 reps
                                                                        -1 hr cardio''')

                            intermediate_tabview_label.place(relx=-0.23, rely=0.1)

                            upperintermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Upper-Intermediate"), text='''
                                                                        -Crunch 3 sets 15 reps
                                                                        -Plank 3 sets 15 reps
                                                                        -Squats 3 set 15 reps
                                                                        -1 hr cardio''')

                            upperintermediate_tabview_label.place(relx=-0.23, rely=0.1)

                            #////////////////////////////////////////////////////////////////////////////////////////////#

                            r5.mainloop()

                            #////////////////////////////////////////////////////////////////////////////////////////////#
                        
                        def stay_fit_button_func():
                            r4.destroy()

                            big_frame = customtkinter.CTkFrame(master=r6, width=800, height=500)
                            big_frame.pack(padx=20, pady=20, )

                            stay_fit_frame = customtkinter.CTkFrame(master=big_frame, width=800, height=400)
                            stay_fit_frame.pack(padx=20, pady=20, side="right")

                            tabview = customtkinter.CTkTabview(stay_fit_frame, width=400, height=400)
                            tabview.pack(padx=20, pady=20)

                            tabview.add("Beginer")
                            tabview.add("Intermediate")
                            tabview.add("Upper-Intermediate")

                            l_tabview_label = customtkinter.CTkLabel(master=stay_fit_frame,text="STAY FIT TRAINING",font=("Arial", 18))
                            l_tabview_label.place(relx=0.313,rely=0)

                            beginer_tabview_label = customtkinter.CTkLabel(tabview.tab("Beginer"), text='''
                                                                        -Crunch 4 sets 15 reps
                                                                        -Push-Up 4 Sets 15 reps
                                                                        -Plank 2 min
                                                                        -Barfix 3 sets 6 reps
                                                                        -30 min cardio''')

                            beginer_tabview_label.place(relx=-0.23, rely=0.1)

                            intermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Intermediate"), text='''
                                                                        -Crunch 5 sets 15 reps
                                                                        -Push-Up 5 Sets 15 reps
                                                                        -Plank 2 min
                                                                        -Barfix 4 sets 6 reps
                                                                        -30 min cardio''')

                            intermediate_tabview_label.place(relx=-0.23, rely=0.1)

                            upperintermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Upper-Intermediate"), text='''
                                                                        -Crunch 4 sets 18 reps
                                                                        -Push-Up 4 Sets 18 reps
                                                                        -Plank 2.30 min
                                                                        -Barfix 3 sets 10 reps
                                                                        -30 min cardio''')

                            upperintermediate_tabview_label.place(relx=-0.23, rely=0.1)

                            #////////////////////////////////////////////////////////////////////////////////////////////#

                            r6.mainloop()
                            #////////////////////////////////////////////////////////////////////////////////////////////#

                        def build_muscles_button_func():
                            r4.destroy()

                            big_frame = customtkinter.CTkFrame(master=r7, width=800, height=500)
                            big_frame.pack(padx=20, pady=20, )

                            stay_fit_frame = customtkinter.CTkFrame(master=big_frame, width=800, height=400)
                            stay_fit_frame.pack(padx=20, pady=20, side="right")

                            tabview = customtkinter.CTkTabview(stay_fit_frame, width=400, height=400)
                            tabview.pack(padx=20, pady=20)

                            tabview.add("Beginer")
                            tabview.add("Intermediate")
                            tabview.add("Upper-Intermediate")

                            l_tabview_label = customtkinter.CTkLabel(master=stay_fit_frame,text="BUILT MUSCLES TRAINING",font=("Arial", 18))
                            l_tabview_label.place(relx=0.236,rely=0)

                            beginer_tabview_label = customtkinter.CTkLabel(tabview.tab("Beginer"), text='''
                                                                        -Bench Press 4 sets 12 reps
                                                                        -Push-Up 4 Sets 18 reps
                                                                        -T Bar Push-down 4 sets 12 reps
                                                                        -Barbell Row 4 sets 12 reps
                                                                        -30 min cardio''')

                            beginer_tabview_label.place(relx=-0.23, rely=0.1)

                            intermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Intermediate"), text='''
                                                                        -Bench Press 4 sets 15 reps
                                                                        -Push-Up 4 Sets 18 reps
                                                                        -T Bar Push-down 4 sets 15 reps
                                                                        -Barbell Row 4 sets 12 reps
                                                                        -30 min cardio''')

                            intermediate_tabview_label.place(relx=-0.23, rely=0.1)

                            upperintermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Upper-Intermediate"), text='''
                                                                        -Bench Press 4 sets 12 reps
                                                                        -Push-Up 4 Sets 20 reps
                                                                        -T Bar Push-down 4 sets 15 reps
                                                                        -Barbell Row 4 sets 15 reps
                                                                        -30 min cardio''')

                            upperintermediate_tabview_label.place(relx=-0.23, rely=0.1)
                            #////////////////////////////////////////////////////////////////////////////////////////////#

                            r7.mainloop()

                    #////////////////////////////////////////////////////////////////////////////////////////////#

                           

                        user_choice_frame = customtkinter.CTkFrame(master=r4,                                      
                                                            width=1000,
                                                            height=1000)
                        user_choice_frame.pack(padx=20,pady=20)

                        user_choice_label =customtkinter.CTkLabel(master=user_choice_frame, 
                                                                    text=" Are You Ready for Your New Life? Make Your Choice!",
                                                                    font=("Arial", 28))
                        user_choice_label.place(relx=0.5, rely=0.4, anchor = tk.CENTER)

                        lose_weight_button = customtkinter.CTkButton(master=user_choice_frame,
                                                                    text="LOSE WEIGHT",
                                                                    command=lose_weight_button_func)
                        lose_weight_button.place(relx=0.3, rely=0.5, anchor = tk.CENTER)

                        stay_fit_button = customtkinter.CTkButton(master=user_choice_frame,
                                                                    text="STAY FIT",
                                                                    command=stay_fit_button_func)
                        stay_fit_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

                        build_muscles_button = customtkinter.CTkButton(master=user_choice_frame,
                                                                    text="BUILD MUSCLES",
                                                                    command=build_muscles_button_func)
                        build_muscles_button.place(relx=0.7, rely=0.5, anchor = tk.CENTER)

                        #////////////////////////////////////////////////////////////////////////////////////////////#

                        r4.mainloop()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#   
                 
                def user_info_dont_save_button_func():
                    messagebox.showinfo("Sucsess","Wellcome")
                    r3.destroy()
                    #////////////////////////////////////////////////////////////////////////////////////////////#

                    def lose_weight_button_func():
                        
                        r4.destroy()

                        big_frame = customtkinter.CTkFrame(master=r5, width=800, height=500)
                        big_frame.pack(padx=20, pady=20)

                        lose_weight_frame = customtkinter.CTkFrame(master=big_frame, width=800, height=400)
                        lose_weight_frame.pack(padx=20, pady=20)
                        
                        tabview = customtkinter.CTkTabview(lose_weight_frame, width=400, height=400)
                        tabview.pack(padx=20, pady=20)

                        tabview.add("Beginer")
                        tabview.add("Intermediate")
                        tabview.add("Upper-Intermediate")

                        l_tabview_label = customtkinter.CTkLabel(master=lose_weight_frame,text="LOSE WEIGHT TRAINING",font=("Arial", 18))
                        l_tabview_label.place(relx=0.257,rely=0)


                        beginer_tabview_label = customtkinter.CTkLabel(tabview.tab("Beginer"), text='''
                                                                    -Crunch 3 sets 12 reps
                                                                    -Plank 3 sets 12 reps
                                                                    -Squats 3 set 12 reps
                                                                    -1 hr cardio
                                                                       ''')

                        beginer_tabview_label.place(relx=-0.23, rely=0.1)

                        intermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Intermediate"), text='''
                                                                    -Crunch 4 sets 12 reps
                                                                    -Plank 4 sets 12 reps
                                                                    -Squats 4 set 12 reps
                                                                    -1 hr cardio''')

                        intermediate_tabview_label.place(relx=-0.23, rely=0.1)

                        upperintermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Upper-Intermediate"), text='''
                                                                    -Crunch 3 sets 15 reps
                                                                    -Plank 3 sets 15 reps
                                                                    -Squats 3 set 15 reps
                                                                    -1 hr cardio''')

                        upperintermediate_tabview_label.place(relx=-0.23, rely=0.1)

                        #////////////////////////////////////////////////////////////////////////////////////////////#

                        r5.mainloop()

                        #////////////////////////////////////////////////////////////////////////////////////////////#

                    def stay_fit_button_func():

                        r4.destroy()

                        big_frame = customtkinter.CTkFrame(master=r6, width=800, height=500)
                        big_frame.pack(padx=20, pady=20, )

                        stay_fit_frame = customtkinter.CTkFrame(master=big_frame, width=800, height=400)
                        stay_fit_frame.pack(padx=20, pady=20, side="right")

                        tabview = customtkinter.CTkTabview(stay_fit_frame, width=400, height=400)
                        tabview.pack(padx=20, pady=20)

                        tabview.add("Beginer")
                        tabview.add("Intermediate")
                        tabview.add("Upper-Intermediate")

                        l_tabview_label = customtkinter.CTkLabel(master=stay_fit_frame,text="STAY FIT TRAINING",font=("Arial", 18))
                        l_tabview_label.place(relx=0.313,rely=0)

                        beginer_tabview_label = customtkinter.CTkLabel(tabview.tab("Beginer"), text='''
                                                                    -Crunch 4 sets 15 reps
                                                                    -Push-Up 4 Sets 15 reps
                                                                    -Plank 2 min
                                                                    -Barfix 3 sets 6 reps
                                                                    -30 min cardio''')

                        beginer_tabview_label.place(relx=-0.23, rely=0.1)

                        intermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Intermediate"), text='''
                                                                    -Crunch 5 sets 15 reps
                                                                    -Push-Up 5 Sets 15 reps
                                                                    -Plank 2 min
                                                                    -Barfix 4 sets 6 reps
                                                                    -30 min cardio''')

                        intermediate_tabview_label.place(relx=-0.23, rely=0.1)

                        upperintermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Upper-Intermediate"), text='''
                                                                    -Crunch 4 sets 18 reps
                                                                    -Push-Up 4 Sets 18 reps
                                                                    -Plank 2.30 min
                                                                    -Barfix 3 sets 10 reps
                                                                    -30 min cardio''')

                        upperintermediate_tabview_label.place(relx=-0.23, rely=0.1)

                        #////////////////////////////////////////////////////////////////////////////////////////////#

                        r6.mainloop()

                    def build_muscles_button_func():
                        r4.destroy()
                        #////////////////////////////////////////////////////////////////////////////////////////////#

                        big_frame = customtkinter.CTkFrame(master=r7, width=800, height=500)
                        big_frame.pack(padx=20, pady=20, )

                        stay_fit_frame = customtkinter.CTkFrame(master=big_frame, width=800, height=400)
                        stay_fit_frame.pack(padx=20, pady=20, side="right")

                        tabview = customtkinter.CTkTabview(stay_fit_frame, width=400, height=400)
                        tabview.pack(padx=20, pady=20)

                        tabview.add("Beginer")
                        tabview.add("Intermediate")
                        tabview.add("Upper-Intermediate")

                        l_tabview_label = customtkinter.CTkLabel(master=stay_fit_frame,text="BUILT MUSCLES TRAINING",font=("Arial", 18))
                        l_tabview_label.place(relx=0.236,rely=0)

                        beginer_tabview_label = customtkinter.CTkLabel(tabview.tab("Beginer"), text='''
                                                                    -Bench Press 4 sets 12 reps
                                                                    -Push-Up 4 Sets 18 reps
                                                                    -T Bar Push-down 4 sets 12 reps
                                                                    -Barbell Row 4 sets 12 reps
                                                                    -30 min cardio''')

                        beginer_tabview_label.place(relx=-0.23, rely=0.1)

                        intermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Intermediate"), text='''
                                                                    -Bench Press 4 sets 15 reps
                                                                    -Push-Up 4 Sets 18 reps
                                                                    -T Bar Push-down 4 sets 15 reps
                                                                    -Barbell Row 4 sets 12 reps
                                                                    -30 min cardio''')

                        intermediate_tabview_label.place(relx=-0.23, rely=0.1)

                        upperintermediate_tabview_label = customtkinter.CTkLabel(tabview.tab("Upper-Intermediate"), text='''
                                                                    -Bench Press 4 sets 12 reps
                                                                    -Push-Up 4 Sets 20 reps
                                                                    -T Bar Push-down 4 sets 15 reps
                                                                    -Barbell Row 4 sets 15 reps
                                                                    -30 min cardio''')

                        upperintermediate_tabview_label.place(relx=-0.23, rely=0.1)
                        #////////////////////////////////////////////////////////////////////////////////////////////#

                        r7.mainloop()

                    #////////////////////////////////////////////////////////////////////////////////////////////#

                    user_choice_frame = customtkinter.CTkFrame(master=r4,                                      
                                                        width=1000,
                                                        height=1000)
                    user_choice_frame.pack(padx=20,pady=20)

                    user_choice_label =customtkinter.CTkLabel(master=user_choice_frame, 
                                                                text=" Are You Ready for Your New Life? Make Your Choice!",
                                                                font=("Arial", 28))
                    user_choice_label.place(relx=0.5, rely=0.4, anchor = tk.CENTER)

                    lose_weight_button = customtkinter.CTkButton(master=user_choice_frame,
                                                                text="LOSE WEIGHT",
                                                                command=lose_weight_button_func)
                    lose_weight_button.place(relx=0.3, rely=0.5, anchor = tk.CENTER)

                    stay_fit_button = customtkinter.CTkButton(master=user_choice_frame,
                                                                text="STAY FIT",
                                                                command=stay_fit_button_func)
                    stay_fit_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

                    build_muscles_button = customtkinter.CTkButton(master=user_choice_frame,
                                                                text="BUILD MUSCLES",
                                                                command=build_muscles_button_func)
                    build_muscles_button.place(relx=0.7, rely=0.5, anchor = tk.CENTER)

                    #////////////////////////////////////////////////////////////////////////////////////////////#

                    r4.mainloop()

                    #////////////////////////////////////////////////////////////////////////////////////////////#

                    user_choice_frame = customtkinter.CTkFrame(master=r4,                                      
                                                        width=1000,
                                                        height=1000)
                    user_choice_frame.pack(padx=20,pady=20)

                    user_choice_label =customtkinter.CTkLabel(master=user_choice_frame, 
                                                                text=" Are You Ready for Your New Life? Make Your Choice!",
                                                                font=("Arial", 28))
                    user_choice_label.place(relx=0.5, rely=0.4, anchor = tk.CENTER)

                    lose_weight_button = customtkinter.CTkButton(master=user_choice_frame,
                                                                text="LOSE WEIGHT",
                                                                command=lose_weight_button_func)
                    lose_weight_button.place(relx=0.3, rely=0.5, anchor = tk.CENTER)

                    stay_fit_button = customtkinter.CTkButton(master=user_choice_frame,
                                                                text="STAY FIT",
                                                                command=stay_fit_button_func)
                    stay_fit_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

                    build_muscles_button = customtkinter.CTkButton(master=user_choice_frame,
                                                                text="BUILD MUSCLES",
                                                                command=build_muscles_button_func)
                    build_muscles_button.place(relx=0.7, rely=0.5, anchor = tk.CENTER)

                    #////////////////////////////////////////////////////////////////////////////////////////////#
                    r4.mainloop()
                    

                #////////////////////////////////////////////////////////////////////////////////////////////#

                

                user_info_frame = customtkinter.CTkFrame(master=r3,                                      
                                                    width=1000,
                                                    height=1000)
                user_info_frame.pack(padx=20,pady=20)

                user_kg_entry = customtkinter.CTkEntry(master=user_info_frame)
                user_kg_entry.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

                global kg
                kg = user_kg_entry.get()
                
                user_waist_circumfrence_entry = customtkinter.CTkEntry(master=user_info_frame)
                user_waist_circumfrence_entry.place(relx=0.5, rely=0.25, anchor = tk.CENTER)

                global waist
                waist = user_waist_circumfrence_entry.get()

                user_height_entry = customtkinter.CTkEntry(master=user_info_frame)
                user_height_entry.place(relx=0.5, rely=0.3, anchor = tk.CENTER)

                global height
                height = user_height_entry.get()

                user_neck_circumfrence_entry = customtkinter.CTkEntry(master=user_info_frame )
                user_neck_circumfrence_entry.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

                global neck
                neck = user_neck_circumfrence_entry.get()

                user_kg_entry_label = customtkinter.CTkLabel(master=user_info_frame, 
                                                            text="Enter Your Kilo:")
                user_kg_entry_label.place(relx=0.3, rely=0.2, anchor = tk.CENTER)

                user_waist_circumfrence_entry_label = customtkinter.CTkLabel(master=user_info_frame, 
                                                                text="Enter Your Waist Circumfrence:")
                user_waist_circumfrence_entry_label.place(relx=0.3, rely=0.25, anchor = tk.CENTER)

                user_height_entry_label = customtkinter.CTkLabel(master=user_info_frame,
                                                    text="Enter Your Height:")
                user_height_entry_label.place(relx=0.3, rely=0.3, anchor = tk.CENTER)

                user_neck_circumfrence_entry_label = customtkinter.CTkLabel(master=user_info_frame, 
                                                                text="Enter Your Neck Circumfrence:")
                user_neck_circumfrence_entry_label.place(relx=0.3, rely=0.35, anchor = tk.CENTER)

                user_info_saver_button1 = customtkinter.CTkButton(master=user_info_frame,
                                                            text="Save and Continue!",
                                                            command=user_info_saver_button_func)
                user_info_saver_button1.place(relx=0.5, rely=0.4, anchor = tk.CENTER)   

                user_info_saver_button2 = customtkinter.CTkButton(master=user_info_frame,
                                                            text="Dont Save and Continue!",
                                                            command=user_info_dont_save_button_func)
                user_info_saver_button2.place(relx=0.3, rely=0.4, anchor = tk.CENTER)
                

                #////////////////////////////////////////////////////////////////////////////////////////////#

                r3.mainloop()

                #////////////////////////////////////////////////////////////////////////////////////////////#

            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            messagebox.showerror("Error", "Invalid Username")
    else:
        messagebox.showerror("Error", "Enter all data")

#////////////////////////////////////////////////////////////////////////////////////////////#

frame1 = customtkinter.CTkFrame(master=r1,
                                width=350,
                                height=350)
frame1.pack(padx=20,pady=20)

username_entry_register = customtkinter.CTkEntry(master=frame1,
                                     placeholder_text="Username",
                                     width=150,
                                     height=40)
username_entry_register.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

password_entry_register = customtkinter.CTkEntry(master=frame1,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
password_entry_register.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

register_button = customtkinter.CTkButton(master=frame1,
                                          text="Create Your account!",
                                          command=signup)
register_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

register_to_login_label = customtkinter.CTkLabel(master=frame1, 
                                                 text="Already have an account?")
register_to_login_label.place(relx=0.5, rely=0.7, anchor = tk.CENTER)

register_to_login_button = customtkinter.CTkButton(master=frame1,
                                          text="Login!",
                                          command=register_to_login_page)
register_to_login_button.place(relx=0.5, rely=0.8, anchor = tk.CENTER)

#////////////////////////////////////////////////////////////////////////////////////////////#

r1.mainloop()