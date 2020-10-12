#FrontEnd

from tkinter import *
from tkinter import messagebox
import xlwt
from xlwt import Workbook
import stdDatabase_BackEnd

class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("Login Page")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="royal blue")
        self.frame = Frame(self.master,bg="white",relief="groove",bd=10)
        self.frame.place(x=300,y=40)

        self.Username=StringVar()
        self.Password=StringVar()

        self.LabelTitle = Label(self.frame,text="Student Information System \nLogin Page",font=('arial',30,'bold'),
                                bg="white",bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=30)

        self.Loginframe1=Frame(self.frame,width=1010,height=100,bd=10,relief='ridge',bg="white")
        self.Loginframe1.grid(row=1,column=0,pady=30)

        self.Loginframe2=Frame(self.frame,width=1000,height=50,bd=10,relief='ridge')
        self.Loginframe2.grid(row=2,column=0,pady=30)

        self.Loginframe3=Frame(self.frame,width=1000,height=100,bd=10,relief='ridge')
        self.Loginframe3.grid(row=3,column=0)

        #=========================================================================================
        self.LabelUsername = Label(self.Loginframe1,text="UserName",font=('arial',20,'bold'),bd=10,bg="white")
        self.LabelUsername.grid(row=0,column=0)
        self.txtUsername = Entry(self.Loginframe1,font=('arial',20,'bold'),bd=10,textvariable=self.Username,bg="light gray")
        self.txtUsername.grid(row=0,column=1)
        
        self.LabelPassword= Label(self.Loginframe1,text="Password",font=('arial',20,'bold'), bd=10,bg="white")
        self.LabelPassword.grid(row=1,column=0) 
        self.txtPassword = Entry(self.Loginframe1,font=('arial',20,'bold'),bd=10,show="*",textvariable=self.Password,bg="light gray")
        self.txtPassword.grid(row=1,column=1,padx=85)

        

        #=========================================================================================

        self.btnLogin = Button(self.Loginframe2,text='Login',width=15,font=('arial',18,'bold'),bg="dodger blue",command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)

        self.btnReset = Button(self.Loginframe2,text='Reset',width=15,font=('arial',18,'bold'),bg="dodger blue",command=self.Reset)
        self.btnReset.grid(row=0,column=1)

        self.btnExit = Button(self.Loginframe2,text='Exit',width=15,font=('arial',18,'bold'),bg="dodger blue",command=self.Exit)
        self.btnExit.grid(row=0,column=2)


        #=========================================================================================
        self.btnDatabase = Button(self.Loginframe3,text='Student Database',state=DISABLED,bg="dodger blue",fg="white",
                                  font=('arial',20,'bold'),command=self.student_window)
        self.btnDatabase.grid(row=0,column=0)

        #=========================================================================================
    def Login_System(self):
        user=self.Username.get()
        pas=self.Password.get()

        if(user==str("admin")) and (pas == str("1234")):
            self.btnDatabase.config(state=NORMAL)
        else:
            messagebox.showinfo("Student Information System","You have Entered Invalid Login Details")
            self.btnDatabase.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
            self.btnDatabase.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Exit(self):
        self.Exit = messagebox.askyesno("Student Information System","Confirm if You want to exit")
        if(self.Exit>0):
            self.master.destroy()
            return


        #=========================================================================================


    def student_window(self):
        self.newWindow=Toplevel(self.master)
        self.obj=Window2(self.newWindow)


class Window2:
    def __init__(self,master):
        self.master=master
        self.master.title("Student Information System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="royal blue")

        StdId = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

#===========================================Functions===============================================

        def Exit():
            self.Exit = messagebox.askyesno("Student Information System","Do you want to exit?",parent=master)
            if (self.Exit>0):
                master.destroy()
                return
    
        def clearData():
            self.txtStdId.delete(0,END)
            self.txtfname.delete(0,END)
            self.txtsname.delete(0,END)
            self.txtDob.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtGender.delete(0,END)
            self.txtAddress.delete(0,END)
            self.txtMobile.delete(0,END)

        def addData():
            if(len(StdId.get())!=0):
               stdDatabase_BackEnd.addStdRec(StdId.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(),
                           Gender.get(), Address.get(), Mobile.get())
               studentlist.delete(0,END)
               studentlist.insert(END,(StdId.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(),
                           Gender.get(), Address.get(), Mobile.get()))

        def DisplayData():
            studentlist.delete(0,END)
            for row in stdDatabase_BackEnd.viewData():
                studentlist.insert(END,row)

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()
            sd = studentlist.get(searchStd)

            self.txtStdId.delete(0,END)
            self.txtStdId.insert(END,sd[1])
            self.txtfname.delete(0,END)
            self.txtfname.insert(END,sd[2])
            self.txtsname.delete(0,END)
            self.txtsname.insert(END,sd[3])
            self.txtDob.delete(0,END)
            self.txtDob.insert(END,sd[4])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END,sd[5])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,sd[6])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,sd[7])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,sd[8])
    
        def DeleteData():
            global sd
            if(len(StdId.get())!=0):
                stdDatabase_BackEnd.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0,END)
            for row in stdDatabase_BackEnd.searchData(StdId.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(),
                           Gender.get(), Address.get(), Mobile.get()):
               studentlist.insert(END,row,str(""))

        def update():
            if(len(StdId.get())!=0):
                stdDatabase_BackEnd.deleteRec(sd[0])
            if(len(StdId.get())!=0):
                stdDatabase_BackEnd.addStdRec(StdId.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(),
                           Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdId.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(),
                           Gender.get(), Address.get(), Mobile.get()))


        def Print():
            wb=Workbook()
            sheet1 = wb.add_sheet("Sheet 1")

            sheet1.write(0,0,"S.No.")
            sheet1.write(0,1,"Student Roll No.")
            sheet1.write(0,2,"First Name")
            sheet1.write(0,3,"Last Name")
            sheet1.write(0,4,"DOB")
            sheet1.write(0,5,"Age")
            sheet1.write(0,6,"Gender")
            sheet1.write(0,7,"Address")
            sheet1.write(0,8,"Mobile No.")

            for (row,i) in zip((stdDatabase_BackEnd.viewData()),range(1,9)):
                sheet1.write(i,0,row[0])
                sheet1.write(i,1,row[1])
                sheet1.write(i,2,row[2])
                sheet1.write(i,3,row[3])
                sheet1.write(i,4,row[4])
                sheet1.write(i,5,row[5])
                sheet1.write(i,6,row[6])
                sheet1.write(i,7,row[7])
                sheet1.write(i,8,row[8])
            wb.save("Student Details.xls")
            messagebox.showinfo("Student Information System","your details are saved!!",parent=master)
            
    
        
       
#===========================================Frames===============================================
        self.MainFrame = Frame(self.master,bg="royal blue")
        self.MainFrame.grid()

        self.TitleFrame = Frame(self.MainFrame,padx=70,pady=8,bg="white",relief=RIDGE)        
        self.TitleFrame.pack(side=TOP)

        self.lblTitle = Label(self.TitleFrame, font=('arial',45,'bold'), text="   Student Information System  ",
                                  bg="white")
        self.lblTitle.grid(sticky=W)

        self.ButtonFrame = Frame(self.MainFrame,width=1350,height=70,padx=1,pady=1,relief=RIDGE,bg="Ghost White")        
        self.ButtonFrame.pack(side=BOTTOM)

        self.DataFrame = Frame(self.MainFrame,bd=1, width=1300,height=700,padx=20,pady=50,relief=RIDGE,bg="royal blue")        
        self.DataFrame.pack(side=BOTTOM)

        self.DataFrameLEFT = LabelFrame(self.DataFrame,bd=1, width=1000,height=600,padx=20,relief=RIDGE,bg="Ghost White",
                           font=('arial',20,'bold','underline'),text="Student Information\n")        
        self.DataFrameLEFT.pack(side=LEFT)

        self.DataFrameRIGHT = LabelFrame(self.DataFrame,bd=1, width=450,height=300,padx=31,pady=3,relief=RIDGE,bg="Ghost White",
                            font=('arial',18,'bold','underline'),text="Student Details\n")        
        self.DataFrameRIGHT.pack(side=RIGHT)


#===========================================Labels and Entry Widget===============================================
        self.lblStdId = Label(self.DataFrameLEFT, font=('arial',20,'bold'), text="Student ID:",padx=2,pady=2,bg="GhostWhite")
        self.lblStdId.grid(row=0,column=0,sticky=W)
        self.txtStdId = Entry(self.DataFrameLEFT, font=('arial',20,'bold'), textvariable=StdId,width=39)
        self.txtStdId.grid(row=0,column=1)

        self.lblfname = Label(self.DataFrameLEFT, font=('arial',20,'bold'), text="First Name:",padx=2,pady=2,bg="GhostWhite")
        self.lblfname.grid(row=1,column=0,sticky=W)
        self.txtfname = Entry(self.DataFrameLEFT, font=('arial',20,'bold'), textvariable=Firstname,width=39)
        self.txtfname.grid(row=1,column=1)

        self.lblsname = Label(self.DataFrameLEFT, font=('arial',20,'bold'), text="Sur Name:",padx=2,pady=2,bg="GhostWhite")
        self.lblsname.grid(row=2,column=0,sticky=W)
        self.txtsname = Entry(self.DataFrameLEFT, font=('arial',20,'bold'), textvariable=Surname,width=39)
        self.txtsname.grid(row=2,column=1)

        self.lblDob = Label(self.DataFrameLEFT, font=('arial',20,'bold'), text="DOB:",padx=2,pady=2,bg="GhostWhite")
        self.lblDob.grid(row=3,column=0,sticky=W)
        self.txtDob = Entry(self.DataFrameLEFT, font=('arial',20,'bold'), textvariable=DoB,width=39)
        self.txtDob.grid(row=3,column=1)

        self.lblAge = Label(self.DataFrameLEFT, font=('arial',20,'bold'), text="Age:",padx=2,pady=2,bg="GhostWhite")
        self.lblAge.grid(row=4,column=0,sticky=W)
        self.txtAge = Entry(self.DataFrameLEFT, font=('arial',20,'bold'), textvariable=Age,width=39)
        self.txtAge.grid(row=4,column=1)

        self.lblGender = Label(self.DataFrameLEFT, font=('arial',20,'bold'), text="Gender:",padx=2,pady=2,bg="GhostWhite")
        self.lblGender.grid(row=5,column=0,sticky=W)
        self.txtGender = Entry(self.DataFrameLEFT, font=('arial',20,'bold'), textvariable=Gender,width=39)
        self.txtGender.grid(row=5,column=1)

        self.lblAddress = Label(self.DataFrameLEFT, font=('arial',20,'bold'), text="Address:",padx=2,pady=2,bg="GhostWhite")
        self.lblAddress.grid(row=6,column=0,sticky=W)
        self.txtAddress = Entry(self.DataFrameLEFT, font=('arial',20,'bold'), textvariable=Address,width=39)
        self.txtAddress.grid(row=6,column=1)

        self.lblMobile = Label(self.DataFrameLEFT, font=('arial',20,'bold'), text="Mobile:",padx=2,pady=2,bg="GhostWhite")
        self.lblMobile.grid(row=7,column=0,sticky=W)
        self.txtMobile = Entry(self.DataFrameLEFT, font=('arial',20,'bold'), textvariable=Mobile,width=39)
        self.txtMobile.grid(row=7,column=1)

#===========================================ListBox & ScrollBar Widget===============================================

        yscrollbar = Scrollbar(self.DataFrameRIGHT)
        yscrollbar.grid(row=0,column=1,sticky=N+S)

        xscrollbar = Scrollbar(self.DataFrameRIGHT,orient=HORIZONTAL)
        xscrollbar.grid(row=1,column=0,sticky=E+W)

        studentlist = Listbox(self.DataFrameRIGHT, width=47,height=15,font=('arial',12,'bold'),
                      yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set)
        studentlist.bind('<<ListboxSelect>>',StudentRec)
        studentlist.grid(row=0,column=0)
        yscrollbar.config(command = studentlist.yview)
        xscrollbar.config(command = studentlist.xview)

#===========================================Button Widget===============================================

        self.btnAdd = Button(self.ButtonFrame, text="Add New",font=('arial',18,'bold'),height=1,width=10,bd=4,
                activeforeground="white",activebackground="black",command=addData)
        self.btnAdd.grid(row=0,column=0)

        self.btnDisplay = Button(self.ButtonFrame, text="Display",font=('arial',18,'bold'),height=1,width=10,bd=4,
                    activeforeground="white",activebackground="black",command=DisplayData)
        self.btnDisplay.grid(row=0,column=1)

        self.btnClear = Button(self.ButtonFrame, text="Clear",font=('arial',18,'bold'),height=1,width=10,bd=4,
                  activeforeground="white",activebackground="black",command=clearData)
        self.btnClear.grid(row=0,column=2)

        self.btnDelete = Button(self.ButtonFrame, text="Delete",font=('arial',18,'bold'),height=1,width=10,bd=4,
                   activeforeground="white",activebackground="black",command=DeleteData)
        self.btnDelete.grid(row=0,column=3)

        self.btnSearch = Button(self.ButtonFrame, text="Search",font=('arial',18,'bold'),height=1,width=10,bd=4,
                   activeforeground="white",activebackground="black",command=searchDatabase)
        self.btnSearch.grid(row=0,column=4)

        self.btnUpdate = Button(self.ButtonFrame, text="Update",font=('arial',18,'bold'),height=1,width=10,bd=4,
                   activeforeground="white",activebackground="black",command=update)
        self.btnUpdate.grid(row=0,column=5)

        self.btnPrint = Button(self.ButtonFrame, text="Print",font=('arial',18,'bold'),height=1,width=10,bd=4,
                 activeforeground="white",activebackground="black",command=Print)
        self.btnPrint.grid(row=0,column=6)

        self.btnExit = Button(self.ButtonFrame, text="Exit",font=('arial',18,'bold'),height=1,width=10,bd=4,
                 activeforeground="white",activebackground="black",command=Exit)
        self.btnExit.grid(row=0,column=7)


        
    #=========================================================================================



if __name__ == '__main__':
    root=Tk()
    obj = Window1(root)
    root.mainloop()
