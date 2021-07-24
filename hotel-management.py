from tkinter import *
import os
from tkinter import messagebox
import tkinter as tk
import mysql.connector
import datetime
import string
from tkinter import filedialog
from PIL import ImageTk,Image
# special characters
special_chars = string.punctuation

slbd=[]
dbbd=[]
qbd=[]
msbd=[]
mibd=[]

mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="hotel")

mysql = mydb.cursor()

data="Select room_no from singlebed where status='vacant'"
mysql.execute(data)
for i in mysql:
    slbd.append(*i)
    
data="Select room_no from doublebed where status='vacant'"
mysql.execute(data)
for i in mysql:
    dbbd.append(*i)
    
data="Select room_no from queenbed where status='vacant'"
mysql.execute(data)
for i in mysql:
    qbd.append(*i)
    
data="Select room_no from mastersuite where status='vacant'"
mysql.execute(data)
for i in mysql:
    msbd.append(*i)
    
data="Select room_no from minisuite where status='vacant'"
mysql.execute(data)
for i in mysql:
    mibd.append(*i)

window = tk.Tk()
window.state('zoomed')
window.title("Hotel Management System")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


#=====================Checkin window==============================#


def check():
    checkin=tk.Toplevel(window)
    checkin.state('zoomed')
    checkin.title("Checkin Window")
    
    checkin.rowconfigure(0, weight=1)
    checkin.columnconfigure(0, weight=1)
    aa = (  "Gabriola",  15,  "bold")
    
    def show_frame(frame):
        frame.tkraise()

    frame2 = tk.Frame(checkin)
    frame3 = tk.Frame(checkin)
    frame4 = tk.Frame(checkin)

    for frame in ( frame2, frame3,frame4):
        frame.grid(row=0,column=0,sticky='nsew')

    #==================Frame 2 code
    Desired_font = (  "Gabriola",  25,  "bold")
    
    def sel():
        global selection
        selection = "You have selected " + str(var.get())
        text1.config(text = selection)
        
    label2 = Label(frame2, image = det)

    label2.pack()
    room=tk.Label(frame2,text="Room Types :-",font=Desired_font,bg="#8b6b51",fg="white")
    room.place(x=100,y=70)
    var = tk.StringVar()
    R1 = tk.Radiobutton(frame2,text="RS: 1500 | Rooms Available = "+str(len(slbd)), image=rb,compound=TOP,variable=var, value="singlebed",command=sel,tristatevalue="x")

    R1.place( x=350,y=70 )

    R2 = tk.Radiobutton(frame2,text="RS: 2000 | Rooms Available = "+str(len(dbbd)), image=doub,compound=TOP, variable=var,value="doublebed",command=sel,tristatevalue="x")
    R2.place( x=650,y=70 )

    R3 = tk.Radiobutton(frame2,text="RS: 3000 | Rooms Available = "+str(len(qbd)), image=que,compound=TOP, variable=var, value="queenbed",command=sel,tristatevalue="x")
    R3.place( x=950,y=70)

    R4 = tk.Radiobutton(frame2,text="RS: 5000 | Rooms Available = "+str(len(msbd)), image=mas,compound=TOP, variable=var, value="mastersuite",command=sel,tristatevalue="x")
    R4.place( x=350,y=360)

    R5 = tk.Radiobutton(frame2,text="RS: 4000 | Rooms Available = "+str(len(mibd)), image=mini,compound=TOP, variable=var, value="minisuite",command=sel,tristatevalue="x")
    R5.place( x=650,y=360)

    suites=tk.Label(frame2,text="Suites :-",font=Desired_font,bg="#6e5338",fg="white")
    suites.place(x=100,y=360)

    text1 = tk.Label(frame2,font=aa,bg="white",fg="green")
    text1.place(x=350,y=660)    


    nextp4 = tk.Button(frame2, text='Confirm',command=lambda:show_frame(frame3),height=1,width=20,font=aa,fg="white",bg="#ac1b12")
    nextp4.place(x=780,y=660)


    #==================Frame 3 code
    
    
    
    Desired_font = (  "Gabriola",  25,  "bold")
    aa = (  "Helvetica",  15,  "bold")
    label3 = Label(frame3, image = ro)
    filename=["empty"]
    def checking():
        ipname = name1.get(1.0, "end-1c")
        ipmobno =mobno1.get(1.0, "end-1c")
        ipnoofd =noofd1.get(1.0, "end-1c")
        ipaddress =address1.get(1.0, "end-1c")
        ipage =age1.get(1.0, "end-1c")
        a=0
        def isnumber(s):
            for i in range(len(s)):
                if s[i].isdigit() != True:
                    return False
            return True
        try :    
            bools = list(map(lambda char: char in special_chars, ipname))
            boolp = list(map(lambda char: char in special_chars, ipmobno))
            boold = list(map(lambda char: char in special_chars, ipnoofd))
            boola = list(map(lambda char: char in special_chars, ipage))
            age=isnumber(ipage)
            phn=isnumber(ipmobno)
            dayss=isnumber(ipnoofd)

            if ipname=="" or ipaddress=="" or ipage=="" or ipmobno=="" or ipnoofd=="":
                raise exception
            elif any(bools) or any(boolp) or any(boold) or any(boola):
                raise exception
            elif len(ipmobno)!=10:
                raise exception
            elif age!=True:
                raise exception
            elif phn!=True:
                raise exception
            elif dayss!=True:
                raise exception("days")
            elif filename[0]=="empty":
                print("checked")
                raise exception
            else:
                for i in ipname:
                    x = i.isdigit()
                    if (x==True):
                        raise exception
            
        except:

            if ipname=="" or ipaddress=="" or ipage=="" or ipmobno=="" or ipnoofd=="":
                messagebox.showerror("Error","Please enter all details")
                window.after(1, lambda: checkin.focus_force())
                a+=1
            elif any(bools) or any(boolp) or any(boold) or any(boola):
                messagebox.showerror("Error","Special characters are not allowed")
                window.after(1, lambda: checkin.focus_force())
                a+=1
            elif age!=True:
                messagebox.showerror("Error","Only integers are allowed in age")
                window.after(1, lambda: checkin.focus_force())
                a+=1
            elif len(ipmobno)!=10:
                messagebox.showerror("Error","Enter valid 10 digit phone number")
                window.after(1, lambda: checkin.focus_force())
                a+=1
            elif phn!=True:
                messagebox.showerror("Error","Only integers are allowed in phone number")
                window.after(1, lambda: checkin.focus_force())
                a+=1
            elif dayss!=True:
                messagebox.showerror("Error","Only integers are allowed in days")
                window.after(1, lambda: checkin.focus_force())
                a+=1
            elif filename[0]=="empty":
                messagebox.showerror("Error","Kindly add proof for completing booking process")
                window.after(1, lambda: checkin.focus_force())
                a+=1
            else:
                for i in ipname:
                    x = i.isdigit()
                    if (x==True):
                        messagebox.showerror("Error","Only alphabets are allowed in name")
                        window.after(1, lambda: checkin.focus_force())
                        a+=1
            
            
        if a==0:
            show_frame(frame4)
    def browseFiles():
        filename[0]=(filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Png files","*.png*"),("all files","*.*"))))
        # Change label contents
        
        window.after(1, lambda: checkin.focus_force())
        if filename[-1]=="":
            messagebox.showerror("Error","Please select proof to complete booking")
            window.after(1, lambda: checkin.focus_force())
        else:
            upl.configure(text="File Selected: "+filename[-1])
            upl.place(x=550,y=350)
        

    label3.pack()
    details=tk.Label(frame3,text="Personal Detail",font=Desired_font,bg="#ac1b12",fg="white")
    details.place(x=620,y=30)

    name=tk.Label(frame3,text="Name:-",font=aa,bg="#867263",fg="white")
    name.place(x=350,y=100)
    
    name1=tk.Text(frame3,font=aa,height=1.4,width=50)
    name1.place(x=450,y=100)
    
    address=tk.Label(frame3,text="Address:-",font=aa,bg="#867263",fg="white")
    address.place(x=328,y=150)

    address1=tk.Text(frame3,font=aa,height=1.4,width=50)
    address1.place(x=450,y=150)

    age=tk.Label(frame3,text="Age:-",font=aa,bg="#867263",fg="white")
    age.place(x=370,y=200)

    age1=tk.Text(frame3,font=aa,height=1.4,width=50)
    age1.place(x=450,y=200)

    mobno=tk.Label(frame3,text="Mobile No:-",font=aa,bg="#867263",fg="white")
    mobno.place(x=315,y=250)

    mobno1=tk.Text(frame3,font=aa,height=1.4,width=50)
    mobno1.place(x=450,y=250)

    noofd=tk.Label(frame3,text="Number Of Days:-",font=aa,bg="#867263",fg="white")
    noofd.place(x=250,y=300)

    noofd1=tk.Text(frame3,font=aa,height=1.4,width=50)
    noofd1.place(x=450,y=300)

    upl = tk.Label(frame3,text="Select a proof:",fg="white",bg="#4c392e",font=aa)
    upl.place(x=650,y=350)

    button_explore = Button(frame3,text = "Browse Files",height=1,width=15,font=aa,fg="white",bg="#ac1b12",command = browseFiles)
    button_explore.place(x=620,y=400)						
    						

    aaa = (  "Helvetica",  15,  "bold")
    b1 = tk.IntVar()  
    b2 = tk.IntVar()  
    b3 = tk.IntVar()

    foodl=tk.Label(frame3,text="Food Type:- ",font=Desired_font,bg="#867263",fg="white")
    foodl.place(x=280,y=450)

    def sel():
        if (b1.get() == 1) & (b2.get() == 0) & (b3.get() == 0):
            text.config(text='You Have Selected Lunch')
        elif (b1.get() == 0) & (b2.get() == 1) & (b3.get() == 0):
            text.config(text='You Have Selected Dinner')
        elif (b1.get() == 0) & (b2.get() == 0) & (b3.get() == 1):
            text.config(text='You Have Selected BreakFast')
        elif (b1.get() == 1) & (b2.get() == 1) & (b3.get() == 0):
            text.config(text='You Have Selected Lunch + Dinner')
        elif (b1.get() == 1) & (b2.get() == 0) & (b3.get() == 1):
            text.config(text='You Have Selected Lunch + BreakFast')
        elif (b1.get() == 0) & (b2.get() == 1) & (b3.get() == 1):
            text.config(text='You Have Selected Dinner + BreakFast')
        elif (b1.get() == 1) & (b2.get() == 1) & (b3.get() == 1):
            text.config(text='You Have Selected Lunch + Dinner + BreakFast')
        elif (b1.get() == 0) & (b2.get() == 0) & (b3.get() == 0):
            text.config(text='You Have Selected None')

  
    Button1 = Checkbutton(frame3, text = "  Lunch      ", font=aaa,variable = b1,onvalue =1,offvalue = 0,height = 2,width = 10,tristatevalue="x",command=sel,bg="#ac1b12",fg="white", activebackground='#ac1b12', activeforeground='white',selectcolor="black")
    Button1.place(x=450,y=450)
  
    Button2 = Checkbutton(frame3, text = "  Dinner     ",font=aaa,variable = b2,onvalue = 1,offvalue = 0,height = 2,width = 10,tristatevalue="x",command=sel,bg="#ac1b12",fg="white", activebackground='#ac1b12', activeforeground='white',selectcolor="black")
    Button2.place(x=450,y=500) 

    Button3 = Checkbutton(frame3, text = "  BreakFast",font=aaa,variable = b3,onvalue =1,offvalue = 0,height = 2,width = 10,tristatevalue="x",command=sel,bg="#ac1b12",fg="white", activebackground='#ac1b12', activeforeground='white',selectcolor="black")  
    Button3.place(x=450,y=550)

    text = tk.Label(frame3,fg="white",bg="#4c392e",font=aa)
    text.place(x=450,y=650)

    nextp = tk.Button(frame3, text='Enter',command=lambda:checking(),height=2,width=20,font=aa,fg="white",bg="#ac1b12")
    nextp.place(x=1100,y=640)

    previous = tk.Button(frame3, text='Back',command=lambda:[show_frame(frame2)],height=2,width=20,font=aa,fg="white",bg="#ac1b12")
    previous.place(x=100,y=640)
    
    #============================Frame4
    receipt1 = (  "Gabriola", 20,  "bold")
    receipt2 = (  "Courier New", 12,  "bold")
    def printre(ipname):
        os.startfile("C://python/"+ipname+".txt","print")
    def printInput():
        
        ipname = name1.get(1.0, "end-1c")
        ipmobno =mobno1.get(1.0, "end-1c")
        ipnoofd =noofd1.get(1.0, "end-1c")
        ipaddress =address1.get(1.0, "end-1c")
        ipage =age1.get(1.0, "end-1c")
        ipage=int(ipage)
        ipnoofd=int(ipnoofd)
        iproom =str(var.get())
        ipname1.config(text="Name- \t\t"+ipname,font=receipt2)
        ipnoofd1.config(text="No Of Days- \t"+str(ipnoofd),font=receipt2)
        ipmobno1.config(text="Mobile No- \t"+ipmobno,font=receipt2)
        iproom1.config(text="room type- \t"+iproom,font=receipt2)
        slbed=1500*ipnoofd
        dbed=2000*ipnoofd
        qbed=3000*ipnoofd
        masbed=5000*ipnoofd
        minbed=4000*ipnoofd
        lch=200*ipnoofd
        din=250*ipnoofd
        brk=100*ipnoofd
        
        if (iproom=="singlebed"):
            roomr1.config(text="RS-"+str(slbed),font=receipt2)
            total=slbed
            roomid=slbd[0]
            slbd.remove(roomid)
            roomid=str(roomid)
            info=("Update singlebed set status = 'occupied' where room_no ="+roomid)
            mysql.execute(info)
            mydb.commit()
        elif (iproom=="doublebed"):
            roomr1.config(text="RS-"+str(dbed),font=receipt2)
            total=dbed
            roomid=dbbd[0]
            dbbd.remove(roomid)
            roomid=str(roomid)
            info=("Update doublebed set status = 'occupied' where room_no ="+roomid)
            mysql.execute(info)
            mydb.commit()
        elif (iproom=="queenroom"):
            roomr1.config(text="RS-"+str(qbed),font=receipt2)
            total=qbed
            roomid=qbd[0]
            qbd.remove(roomid)
            roomid=str(roomid)
            info=("Update queenbed set status = 'occupied' where room_no ="+roomid)
            mysql.execute(info)
            mydb.commit()
        elif (iproom=="mastersuite"):
            roomr1.config(text="RS-"+str(masbed),font=receipt2)
            total=masbed
            roomid=msbd[0]
            msbd.remove(roomid)
            roomid=str(roomid)
            info=("Update mastersuite set status = 'occupied' where room_no ="+roomid)
            mysql.execute(info)
            mydb.commit()
        elif (iproom=="minisuite"):
            roomr1.config(text="RS-"+str(minbed),font=receipt2)
            total=minbed
            roomid=mibd[0]
            mibd.remove(roomid)
            roomid=str(roomid)
            info=("Update minisuite set status = 'occupied' where room_no ="+roomid)
            mysql.execute(info)
            mydb.commit()
        
        tag1.config(text="ORDER \t\t\t\t\t Rs",font=receipt2)
        if (b1.get() == 1) & (b2.get() == 0) & (b3.get() == 0):
            iptext1.config(text='Food Type-',font=receipt2)
            iplunch1.config(text=' Lunch',font=receipt2)
            ipdinner1.config(text=' Dinner',font=receipt2)
            ipbreak1.config(text=' BreakFast',font=receipt2)
            lunchr1.config(text="RS-"+str(lch),font=receipt2)
            dinnerr1.config(text="RS-0",font=receipt2)
            breakr1.config(text="RS-0",font=receipt2)
            total=total+lch
            ipfood="Lunch"
        elif (b1.get() == 0) & (b2.get() == 1) & (b3.get() == 0):
            iptext1.config(text='Food Type-',font=receipt2)
            iplunch1.config(text=' Lunch',font=receipt2)
            ipdinner1.config(text=' Dinner',font=receipt2)
            ipbreak1.config(text=' BreakFast',font=receipt2)
            lunchr1.config(text="RS-0",font=receipt2)
            dinnerr1.config(text="RS-0"+str(din),font=receipt2)
            breakr1.config(text="RS-0",font=receipt2)
            total=total+din
            ipfood="Dinner"
        elif (b1.get() == 0) & (b2.get() == 0) & (b3.get() == 1):
            iptext1.config(text='Food Type-',font=receipt2)
            iplunch1.config(text=' Lunch',font=receipt2)
            ipdinner1.config(text=' Dinner',font=receipt2)
            ipbreak1.config(text=' BreakFast',font=receipt2)
            lunchr1.config(text="RS-0",font=receipt2)
            dinnerr1.config(text="RS-0",font=receipt2)
            breakr1.config(text="RS-"+str(brk),font=receipt2)
            total=total+brk
            ipfood="BreakFast"
        elif (b1.get() == 1) & (b2.get() == 1) & (b3.get() == 0):
            iptext1.config(text='Food Type-',font=receipt2)
            iplunch1.config(text=' Lunch',font=receipt2)
            ipdinner1.config(text=' Dinner',font=receipt2)
            ipbreak1.config(text=' BreakFast',font=receipt2)
            lunchr1.config(text="RS-"+str(lch),font=receipt2)
            dinnerr1.config(text="RS-"+str(din),font=receipt2)
            breakr1.config(text="RS-0",font=receipt2)
            total=total+lch+din
            ipfood="Lunch+Dinner"
        elif (b1.get() == 1) & (b2.get() == 0) & (b3.get() == 1):
            iptext1.config(text='Food Type-',font=receipt2)
            iplunch1.config(text=' Lunch',font=receipt2)
            ipdinner1.config(text=' Dinner',font=receipt2)
            ipbreak1.config(text=' BreakFast',font=receipt2)
            lunchr1.config(text="RS-"+str(lch),font=receipt2)
            dinnerr1.config(text="RS-0",font=receipt2)
            breakr1.config(text="RS-"+str(brk),font=receipt2)
            total=total+lch+brk
            ipfood="Lunch+Breakfast"
        elif (b1.get() == 0) & (b2.get() == 1) & (b3.get() == 1):
            iptext1.config(text='Food Type-',font=receipt2)
            iplunch1.config(text=' Lunch',font=receipt2)
            ipdinner1.config(text=' Dinner',font=receipt2)
            ipbreak1.config(text=' BreakFast',font=receipt2)
            lunchr1.config(text="RS-0",font=receipt2)
            dinnerr1.config(text="RS-"+str(din),font=receipt2)
            breakr1.config(text="RS-"+str(brk),font=receipt2)
            total=total+din+brk
            ipfood="dinner+Breakfast"
        elif (b1.get() == 1) & (b2.get() == 1) & (b3.get() == 1):
            iptext1.config(text='Food Type-',font=receipt2)
            iplunch1.config(text=' Lunch',font=receipt2)
            ipdinner1.config(text=' Dinner',font=receipt2)
            ipbreak1.config(text=' BreakFast',font=receipt2)
            lunchr1.config(text="RS-"+str(lch),font=receipt2)
            dinnerr1.config(text="RS-"+str(din),font=receipt2)
            breakr1.config(text="RS-"+str(brk),font=receipt2)
            total=total+lch+din+brk
            ipfood="Lunch+Dinner+Breakfast"
        foodprice=lch+din+brk
            #=============Database entry===============#
        now = datetime.datetime.today()
        date = str(now.strftime("%d/%m/%Y"))
        time = str(now.strftime("%H:%M:%S"))
        nextd = datetime.datetime.today() + datetime.timedelta(days=ipnoofd)
        period = str(nextd.strftime("%d/%m/%Y"))
        roomid=int(roomid)
        info = ("INSERT into cust_info (room_no,Name,Address,phone,age,days,food,room_type,amount,date,time,period,proof)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        val = (roomid,ipname,ipaddress,ipmobno,ipage,ipnoofd,ipfood,iproom,total,date,time,period,filename[0])
        mysql.execute(info,val)
        mydb.commit()

        totall1.config(text="TOTAL-",font=receipt2)
        totalr1.config(text="RS-"+str(total),font=receipt2)
        roomno1.config(text="Your Room No Is  --"+str(roomid),font=receipt2)
        exit1.config(text="=========Have A Nice Day=========",font=receipt2)

        f = open(ipname+".txt", "w")
        f.write("\n=======Thankyou For Booking========\n\n\tName:- {}\n\tAddress:- {}\n\tMobile No:- {}\n\tAge:- {}\n\tDays:- {}\n\tFood Type:- {}\n\tFood price:- {}\n\tRoom Type:- {}\n\tRoom No:- {}\n\tTotal:- {}\n\tCheckin Date:- {}\n\tCheckin Time:- {}\n\tCheckout Date:- {}\n\n=======Have A Nice Day=======".format(ipname,ipaddress,ipmobno,ipage,ipnoofd,ipfood,foodprice,iproom,roomid,total,date,time,period))
        f.close()
        date1.config(text='Date = '+date,font=receipt2)
        time1.config(text='Checkin Time = '+time,font=receipt2)

        printButton1 = tk.Button(frame4,text = "Print Receipt",command = lambda:printre(ipname))
        printButton1.place(x=630,y=700)

        printButton.destroy()

        
        
        
        
  

    printButton = tk.Button(frame4,text = "Get receipt",command = printInput)
    printButton.place(x=630,y=100)
    ipname1 = tk.Label(frame4,text="======Thankyou For Booking======",font=receipt1)
    ipname1.place(x=500,y=30)

    date1 = tk.Label(frame4)
    date1.place(x=400,y=200)

    time1 = tk.Label(frame4)
    time1.place(x=660,y=200)
    
    ipname1 = tk.Label(frame4)
    ipname1.place(x=400,y=240)
    
    ipnoofd1 = tk.Label(frame4)
    ipnoofd1.place(x=400,y=280)
    
    ipmobno1 = tk.Label(frame4)
    ipmobno1.place(x=400,y=320)
    
    iproom1 = tk.Label(frame4)
    iproom1.place(x=400,y=400)
    
    iptext1 = tk.Label(frame4)
    iptext1.place(x=400,y=440)
    
    iplunch1 = tk.Label(frame4)
    iplunch1.place(x=560,y=440)
    
    ipdinner1 = tk.Label(frame4)
    ipdinner1.place(x=560,y=480)
    
    ipbreak1 = tk.Label(frame4)
    ipbreak1.place(x=560,y=520)
    
    tag1 = tk.Label(frame4)
    tag1.place(x=400,y=340)

    roomr1 = tk.Label(frame4)
    roomr1.place(x=800,y=400)
    
    foodr1 = tk.Label(frame4)
    foodr1.place(x=560,y=480)
    lunchr1 = tk.Label(frame4)
    lunchr1.place(x=800,y=440)
    dinnerr1 = tk.Label(frame4)
    dinnerr1.place(x=800,y=480)
    breakr1 = tk.Label(frame4)
    breakr1.place(x=800,y=520)

    totall1 = tk.Label(frame4)
    totall1.place(x=400,y=560)
    totalr1 = tk.Label(frame4)
    totalr1.place(x=800,y=560)

    exit1 = tk.Label(frame4)
    exit1.place(x=500,y=660)
    roomno1 = tk.Label(frame4)
    roomno1.place(x=400,y=620)
    
    

    

    
    show_frame(frame2)
    checkin.mainloop()





#========================checkout window==============================#
def checkout():
    checko=tk.Toplevel(window,bg="#3C1A5B")
    checko.geometry('400x350')
    checko.title("Checkout")
    Desired_font = (  "Helvetica",  25,  "bold")
    aa = (  "Helvetica",  15,  "bold")
    details=tk.Label(checko,text="Check Out",font=Desired_font,bg="#3C1A5B", fg="#CCF381")
    details.place(x=100,y=30)

    name=tk.Label(checko,text="Enter Room No: ",font=aa,bg="#3C1A5B", fg="#CCF381")
    name.place(x=50,y=100)

    name1=tk.Text(checko,font=aa,height=1.4,width=10)
    name1.place(x=250,y=100)

    def check_out():
        inp=name1.get(1.0,"end-1c")
        try:
            rest = ("SELECT room_no,room_type FROM `cust_info` WHERE `room_no`="+inp)            
            mysql.execute(rest)
            for i in mysql:
                roomno=i[0]
                roomtype=i[1]
            info = ("Delete from `cust_info` where `room_no`="+inp)        
            mysql.execute(info)
            mydb.commit()
            info = ("Update {} set status='vacant' where room_no={}".format(roomtype,roomno))
            mysql.execute(info)
            mydb.commit()

            if(roomtype=="singlebed"):
                slbd.append(roomno)
            elif(roomtype=="doublebed"):
                dbbd.append(roomno)
            elif(roomtype=="queenbed"):
                qbd.append(roomno)
            elif(roomtype=="mastersuite"):
                msbd.append(roomno)
            elif(roomtype=="minisuite"):
                mibd.append(roomno)
            lbl.config(text="The room number {} is checked out".format(inp))

        except:
            messagebox.showerror("Error","Enter occupied Room no")
            window.after(1, lambda: checko.focus_force())
            

            
        

    lbl = tk.Label(checko, text = "",bg="#3C1A5B", fg="#CCF381",font=aa)
    lbl.place(x=10,y=200)

    chec = tk.Button(checko, text='Checkout',command=check_out,height=1,width=20,fg="#3C1A5B", bg="#CCF381",font=aa)
    chec.place(x=50,y=150)
    checko.mainloop()
#========================checklist window==============================#
def listt():
    listo=tk.Toplevel(window,bg="#3C1A5B")
    listo.geometry("650x600")
    Desired_font = (  "Gabriola",  35, "bold")
    listo.title("Guest List")
    
    
    a=1
    aa = (  "Gabriola",  25,  "bold")
    listbox = Listbox(listo, height = 5, width = 35, bg = "#3C1A5B",activestyle = 'dotbox', font = aa,fg = "#FFF748")
    info = "Select Name,room_no from cust_info"
    mysql.execute(info)
    name=[]
    roomno=[]
    for i in mysql:
        ft=i[0]
        sd=i[1]
        name.append(ft)
        roomno.append(sd)   
    for i in name:
        listbox.insert(a, " Name:- "+name[a-1]+"  Room No:- "+str(roomno[a-1]))
        a=a+1
    #label.place(x=250,y=40)
    listbox.place(x=68,y=90)
    canvas=tk.Canvas(listo,width=170,height=40,bg="#3C1A5B", highlightbackground="#3C1A5B")
    canvas.place(x=228,y=65)
    canvas.create_text(8,21,text="\tGuest List",fill="#FFF748",font=Desired_font)

    listo.mainloop()

def show_proof(prf):
    proofi=tk.Toplevel(window)
    proofi.title("Proof")
    proofi.rowconfigure(0, weight=1)
    proofi.columnconfigure(0, weight=1)
    
    img = Image.open(prf)
    width = img.width
    height = img.height
    img = ImageTk.PhotoImage(img)
    proofi.geometry(f"{width}x{height}")
    label2 = Label(proofi, image = img)
    label2.image = img
    label2.pack()
#========================checkinfo window==============================#
def info():
    inf=tk.Toplevel(window,bg="#5f0eed",relief=RIDGE)
    inf.state("zoomed")
    inf.title("Guest Info")
    Desired_font = (  "Gabriola",  35,  "bold")
    aa = (  "Gabriola",  15,  "bold")
    rr = (  "Gabriola",  18,  "bold")
    details=tk.Label(inf,text="Guest Info",font=Desired_font,bg="#5f0eed",fg="#CCF381")
    details.place(x=100,y=30)

    name=tk.Label(inf,text="Enter Room No: ",font=Desired_font,bg="#5f0eed",fg="#CCF381")
    name.place(x=50,y=100)

    name1=tk.Text(inf,font=20,height=1.4,width=10)
    name1.place(x=320,y=135)

    
    
    def check_info():
        inp=name1.get(1.0,"end-1c")
        try:
            info=("Select * from cust_info where room_no="+inp)
            mysql.execute(info)
            for i in mysql:
                room = tk.Label(inf,text="Room No:- "+str(i[0]),bg="#5f0eed",font=rr,fg="#CCF381")
                ipname1 = tk.Label(inf,text="Name:- "+i[1],bg="#5f0eed",font=rr,fg="#CCF381")
                address = tk.Label(inf,text="Address:- "+i[2],bg="#5f0eed",font=rr,fg="#CCF381")
                ipmobno1 = tk.Label(inf,text="Mobile No:- "+i[3],bg="#5f0eed",font=rr,fg="#CCF381")
                ipage = tk.Label(inf,text="Age:- "+str(i[4]),bg="#5f0eed",font=rr,fg="#CCF381")
                ipnoofd1 = tk.Label(inf,text="Days:- "+str(i[5]),bg="#5f0eed",font=rr,fg="#CCF381")        
                iptext1 = tk.Label(inf,text="Food Type:- "+i[6],bg="#5f0eed",font=rr,fg="#CCF381")        
                iproom1 = tk.Label(inf,text="Room Type:- "+i[7],bg="#5f0eed",font=rr,fg="#CCF381")
                totall1 = tk.Label(inf,text="Total Amount:- "+str(i[8]),bg="#5f0eed",font=rr,fg="#CCF381")
                date1 = tk.Label(inf,text="Date:- "+str(i[9]),bg="#5f0eed",font=rr,fg="#CCF381")
                time1 = tk.Label(inf,text="Checkin Time:- "+str(i[10]),bg="#5f0eed",font=rr,fg="#CCF381")
                chck1 = tk.Label(inf,text="Checkout Date:- "+str(i[11]),bg="#5f0eed",font=rr,fg="#CCF381")
            
        
                room.place(x=450,y=160)
                ipname1.place(x=450,y=200)
                address.place(x=450,y=240)
                ipmobno1.place(x=450,y=280)
                ipage.place(x=450,y=320)
                ipnoofd1.place(x=450,y=360)
                iptext1.place(x=450,y=400)
                iproom1.place(x=450,y=440)
                totall1.place(x=450,y=480)
                date1.place(x=450,y=520)
                time1.place(x=450,y=560)
                chck1.place(x=450,y=600)

                sh = tk.Button(inf, text='Proof',command=lambda:show_proof(i[12]),width=10,bg="#CCF381", fg="#5f0eed", relief=GROOVE, font=aa)
                sh.place(x=500,y=640)
        except:
            messagebox.showerror("Error","Enter occupied Room no")
            window.after(1, lambda: inf.focus_force())


    chec = tk.Button(inf, text='Show Info',command=check_info,height=1,width=20,bg="#CCF381", fg="#5f0eed", relief=GROOVE, font=aa)
    chec.place(x=50,y=200)
    inf.mainloop()


#==================Window1
bg = PhotoImage(file = "C:/python/bg-img.png")

rb = PhotoImage(file = "C:/python/trial.png")
ro = PhotoImage(file = "C:/python/bg.png")
det = PhotoImage(file = "C:/python/detai.png")
doub = PhotoImage(file = "C:/python/double.png")
que = PhotoImage(file = "C:/python/queen.png")
mini = PhotoImage(file = "C:/python/mini.png")
mas = PhotoImage(file = "C:/python/master.png")
label1 = Label(window, image = bg)

label1.place(x=-210,y=0)

Desired_font = (  "Gabriola", 60,  "bold")
Desired_button = (  "Gabriola", 15,  "bold")

T = Label(window,text="Welcome to",font=Desired_font, fg="#eea22f",bg="#5f0eed")
T.place(x=520,y=20)

nextp1 = tk.Button(window, text='Check In',height=0,width=30, font=Desired_button, fg="#5f0eed", relief=GROOVE, bg="#eea22f",command=check)
nextp1.place(x=270,y=500)

nextp2 = tk.Button(window, text='Check Out',height=0,width=30, font=Desired_button, fg="#5f0eed", relief=GROOVE, bg="#eea22f",command=checkout)
nextp2.place(x=790,y=500)

nextp3 = tk.Button(window, text='Guest List',height=0,width=30, font=Desired_button, fg="#5f0eed", relief=GROOVE, bg="#eea22f",command=listt)
nextp3.place(x=270,y=600)

nextp4 = tk.Button(window, text='Search Guest Info',height=0,width=30, font=Desired_button, fg="#5f0eed", relief=GROOVE, bg="#eea22f",command=info)
nextp4.place(x=790,y=600)


window.mainloop()
mydb.close()
