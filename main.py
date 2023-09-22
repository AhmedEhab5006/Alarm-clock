#importing recommended libraries
from playsound import playsound
from tkinter import *
import customtkinter
from customtkinter import *
import datetime , time
from tkinter import messagebox as msg
import threading
#creating the root window
root = CTk ()
#setting the theme in dark mode
customtkinter.set_appearance_mode("Dark")
#creating a variable for am and pm buttons
x = IntVar ()



#creating pm button's function
def pm () :
    global x
    x = 1



#creating variables which stores user's time
hr = StringVar()
min = StringVar()
sec = StringVar()
user_time = StringVar()


#creating flags for Threading , refresh and set functions to connect them together
y = 0
z = 0
r = 0


#creating threading function to avoid overload which is resulted from while loop which is in set function
def Threading ():
    thread = threading.Thread(target = set)
    thread.start()




#creating refresh function to make alarm reusable after canceling it
def refresh () :
    global y
    global z
    y = 0
    z = 0
    set3_btn = customtkinter.CTkButton(text="Set", master=root, command=Threading)
    set3_btn.place(x=184, y=550)
    blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", text_color="#242424")
    blank_label.place(x=125, y=500)
    new_alarm_label = customtkinter.CTkLabel(root , text = "Press set button to set a new alarm" , text_color = "white" )
    new_alarm_label.place(x=155, y=500)




#creating stop function which cancels alarm
def stop () :
    global y
    global z
    y = 1
    z = 1
    set2_btn = customtkinter.CTkButton(text = "Set new one" , master = root , command = refresh )
    set2_btn.place(x=184, y=550)
    blank_label = customtkinter.CTkLabel(root , text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" , text_color = "#242424")
    blank_label.place(x=125, y=500)
    stop_label = customtkinter.CTkLabel(root, text_color="yellow", text="Alarm is canceled by user")
    stop_label.place(x=180, y=500)




#displaying current time on entry boxes when alarm is opened
hr.set(datetime.datetime.now().strftime("%H"))
if int(datetime.datetime.now().strftime("%H")) > 12 :
    hr.set(str(int(datetime.datetime.now().strftime("%H")) - 12))
    x.set(1)
min.set(datetime.datetime.now().strftime("%M"))
sec.set(datetime.datetime.now().strftime("%S"))




#creating set function which set the alarm
def set () :
    stop_btn = customtkinter.CTkButton(root, text="Cancel", fg_color="red", text_color="Black", command=stop)
    stop_btn.place(x=184, y=550)
    while True :
        global hr , min , sec , x , y , user_time , z , r , set_btn
        hr = hr_entry.get()
        min = min_entry.get()
        sec = sec_entry.get()
        if y == 1 :
            break
        if hr == "" and min == "" and sec == "" :
            blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",text_color="#242424")
            blank_label.place(x=125, y=500)
            error_label = customtkinter.CTkLabel(root, text_color="red", text="You must enter a time !")
            error_label.place(x = 184 , y = 500)
            break
        if int(min) > 60 and int(sec) > 60 and int(hr) > 12:
                blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",text_color="#242424")
                blank_label.place(x=125, y=500)
                error_label = customtkinter.CTkLabel(root, text_color="red",text="Wrong input !")
                error_label.place(x=217, y=500)
                break
        if int(min) > 60 and int(sec) > 60 :
                blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",text_color="#242424")
                blank_label.place(x=125, y=500)
                error_label = customtkinter.CTkLabel(root, text_color="red",text="Wrong input !")
                error_label.place(x=217, y=500)
                break
        if  int(sec) > 60 and int(hr) > 12:
                blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",text_color="#242424")
                blank_label.place(x=125, y=500)
                error_label = customtkinter.CTkLabel(root, text_color="red",text="Wrong input !")
                error_label.place(x=217, y=500)
                break
        if int(min) > 60 and int(hr) > 12:
            if int(min) > 60:
                blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",text_color="#242424")
                blank_label.place(x=125, y=500)
                error_label = customtkinter.CTkLabel(root, text_color="red",text="Wrong input !")
                error_label.place(x=217, y=500)
                break
        if int(hr) > 12 :
            blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",text_color="#242424")
            blank_label.place(x=125, y=500)
            error_label = customtkinter.CTkLabel(root, text_color="red", text="Wrong input (Hrs cannot be greater than 12)")
            error_label.place(x=133, y=500)
            break
        if int(min) > 60 :
            blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",text_color="#242424")
            blank_label.place(x=125, y=500)
            error_label = customtkinter.CTkLabel(root, text_color="red",text="Wrong input (Mins cannot be greater than 60)")
            error_label.place(x=133, y=500)
            break
        if int(sec) > 60 :
            blank_label = customtkinter.CTkLabel(root, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",text_color="#242424")
            blank_label.place(x=125, y=500)
            error_label = customtkinter.CTkLabel(root, text_color="red",text="Wrong input (Secs cannot be greater than 60)")
            error_label.place(x=133, y=500)
            break
        if min == "" and sec == "" :
            min = "00"
            sec = "00"
        if hr == "" :
            hr = "00"
        if sec == "" :
            sec = "00"
        if min == "" :
            min = "00"
        else:
            if len(hr) < 2 :
                hr = f"0{hr}"
            if len(min) < 2 :
                min = f"0{min}"
            if len(sec) < 2 :
                sec = f"0{sec}"
            if hr == "12"  :
                hr = "00"
                if x == 1 :
                    hr = "12"
                user_time = f"{hr}:{min}:{sec}"
            if x == 1 or int(datetime.datetime.now().strftime("%H")) > 12:
                user_time = f"{str((int (hr) + 12))}:{min}:{sec}"
            else :
                user_time = f"{hr}:{min}:{sec}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        hrs = int(hr)
        mins = int(min)
        secs = int(sec)
        current_hrs = int(datetime.datetime.now().strftime("%H"))
        current_mins = int(datetime.datetime.now().strftime("%M"))
        current_secs = int(datetime.datetime.now().strftime("%S"))
        if int(datetime.datetime.now().strftime("%H")) > 12 or x == 1 :
            current_hrs -= 12
        hrs_sub = hrs - current_hrs
        mins_sub = mins - current_mins
        secs_sub = secs - current_secs
        if hrs == current_hrs :
            if x == 1 :
                hrs += 12
                hrs_sub = hrs - current_hrs
        if hrs < current_hrs or hrs == current_hrs and mins < current_mins :
            hrs_sub = (hrs+23) - current_hrs
        if mins < current_mins :
                mins += 59
                mins_sub = mins - current_mins
        if secs < current_secs :
                secs += 59
                secs_sub = secs - current_secs

        count_label = customtkinter.CTkLabel(root, text_color="green", text=f"Alarm will ring after {hrs_sub} Hrs : {mins_sub} Mins : {secs_sub} Secs" )
        count_label.place(x=125, y=500)
        if z == 1 :
            count_label.destroy()
        print(user_time,current_time)
        if user_time == current_time:
            stop_btn.destroy()
            playsound("Elements\\Sound\\Alarm.mp3")
            msg.showwarning(title="Alarm clock", message="Wake up!")
            break







#configuring our root by choosing window size , icon , title , buttons , labels and entries
root.geometry("500x600")
root.resizable(False , False)
root.title("Alarm clock")
root.iconbitmap("Elements\\Images\\Clock.ico")
clock_img = PhotoImage(file = "Elements\\Images\\Clock.png")
clock_label = Label (image = clock_img , borderwidth = 0 , bg = "#242424")
clock_label.place(x = 160 , y = 25)
set_label = Label(text = "Set the alarm" , fg = "White" , bg = "#242424" , font = "Arial 40" )
set_label.place(x = 100 , y = 250)
sec_label = Label(text = "Sec" , font = "Arial 20" , bg = "#242424" , fg = "white")
sec_label.place(x = 383 , y = 330)
min_label = Label(text = "Min" , font = "Arial 20" , bg = "#242424" , fg = "white")
min_label.place(x = 230 , y = 330)
hr_label = Label(text = "Hr" , font = "Arial 20" , bg = "#242424" , fg = "white")
hr_label.place(x = 77 , y = 330)
sec_entry = customtkinter.CTkEntry (textvariable = sec , width = 60 , height = 100 , master = root ,font = customtkinter.CTkFont(size=40) )
sec_entry.place(x = 380 , y = 370)
min_entry = customtkinter.CTkEntry (textvariable = min , width = 60 , height = 100 , master = root ,font = customtkinter.CTkFont(size=40) )
min_entry.place(x = 225 , y = 370)
hr_entry = customtkinter.CTkEntry (textvariable = hr,width = 60 , height = 100 , master = root ,font = customtkinter.CTkFont(size=40) )
hr_entry.place(x = 65 , y = 370)
am_check = customtkinter.CTkRadioButton(root , text = "AM" ,width = 5 , value = 0 , variable = x)
am_check.place(x = 141 , y = 388)
pm_check = customtkinter.CTkRadioButton(root , text = "PM" ,width = 5 , value = 1 , variable = x , command = pm)
pm_check.place(x = 141 , y = 430)
set_btn = customtkinter.CTkButton(text = "Set" , master = root , command = Threading )
set_btn.place(x = 184 , y = 550)
root.mainloop()