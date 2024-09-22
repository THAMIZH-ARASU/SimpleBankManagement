import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime
from PIL import ImageTk, Image

def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num):
	try:
		fpin=open(num+".txt",'r')
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
	fpin.close()
	return 

def home_return(master):
	master.destroy()
	Main_Menu()

def write(master,name,oc,pin):
	
	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	f1=open("Accnt_Record.txt",'r')
	accnt_no=int(f1.readline())
	accnt_no+=1
	f1.close()

	f1=open("Accnt_Record.txt",'w')
	f1.write(str(accnt_no))
	f1.close()

	fdet=open(str(accnt_no)+".txt","w")
	fdet.write(pin+"\n")
	fdet.write(oc+"\n")
	fdet.write(str(accnt_no)+"\n")
	fdet.write(name+"\n")
	fdet.close()

	frec=open(str(accnt_no)+"-rec.txt",'w')
	frec.write("Date                             Credit      Debit     Balance\n")
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
	frec.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return

def crdt_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=amti+camt
	fdet=open(accnt+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(accnt+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(accnt)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return

def debit_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 
			
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if(int(amt)>camt):
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
		amti=int(amt)
		cb=camt-amti
		fdet=open(accnt+".txt",'w')
		fdet.write(pin)
		fdet.write(str(cb)+"\n")
		fdet.write(accnt+"\n")
		fdet.write(name+"\n")
		fdet.close()
		frec=open(str(accnt)+"-rec.txt",'a+')
		frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
		frec.close()
		messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
		master.destroy()
		return

def Cr_Amt(accnt,name):
	creditwn=tk.Tk()
	creditwn.geometry("600x300")
	creditwn.title("Credit Amount")
	creditwn.configure(bg="orange")
	fr1=tk.Frame(creditwn,bg="blue")
	l_title=tk.Message(creditwn,text="BANKING SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Times New Roman","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(creditwn,relief="flat",text="Enter Amount to be credited: ",font=("Times New Roman","30","bold"),bg="orange")
	e1=tk.Entry(creditwn,relief="raised",width=30,font=("Times New Roman","28","bold"))
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(creditwn,text="Credit",relief="raised",font=("Times New Roman","30","bold"),bg="red",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
	b.pack(side="top")
	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))


def De_Amt(accnt,name):
	debitwn=tk.Tk()
	debitwn.geometry("600x300")
	debitwn.title("Debit Amount")	
	debitwn.configure(bg="orange")
	fr1=tk.Frame(debitwn,bg="blue")
	l_title=tk.Message(debitwn,text="BANKING SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Times New Roman","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(debitwn,relief="flat",text="Enter Amount to be debited: ",font=("Times New Roman","30","bold"),bg="orange")
	e1=tk.Entry(debitwn,relief="raised",width=30,font=("Times New Roman","28","bold"))
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(debitwn,text="Debit",relief="raised",font=("Times New Roman","30","bold"),bg="red",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
	b.pack(side="top")
	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))




def disp_bal(accnt):
	fdet=open(accnt+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",bal)




def disp_tr_hist(accnt):
	disp_wn=tk.Tk()
	disp_wn.geometry("900x600")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg="orange")
	fr1=tk.Frame(disp_wn,bg="blue")
	l_title=tk.Message(disp_wn,text="BANKING SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Your Transaction History",font=("Times New Roman",38,"bold"),padx=100,pady=20,width=1000,bg="orange",fg="blue",relief="flat")
	l1.pack(side="top")
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	frec=open(accnt+"-rec.txt",'r')
	for line in frec:
		l=tk.Message(disp_wn,anchor="w",text=line,font=("Times New Roman",10,"bold"),relief="flat",width=2000)
		l.pack(side="top")
	b=tk.Button(disp_wn,text="Quit",relief="raised",bg="red",font=("Times New Roman",30,"bold"),command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()

def logged_in_menu(accnt,name):
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("BANKING SYSTEM-"+name)
	rootwn.configure(background='orange')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(rootwn,text="SIMPLE BANKING\n SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
	label=tk.Label(text="Logged in as: "+name,relief="raised",bg="black",fg="white",anchor="center",justify="center")
	label.pack(side="top")
	img2=tk.PhotoImage(file="img/credit.png")
	myimg2=img2.subsample(2,2)
	img3=tk.PhotoImage(file="img/debit.png")
	myimg3=img3.subsample(2,2)
	img4=tk.PhotoImage(file="img/balance1.png")
	myimg4=img4.subsample(2,2)
	img5=tk.PhotoImage(file="img/transaction.png")
	myimg5=img5.subsample(2,2)
	b2=tk.Button(image=myimg2,command=lambda: Cr_Amt(accnt,name))
	b2.image=myimg2
	b3=tk.Button(image=myimg3,command=lambda: De_Amt(accnt,name))
	b3.image=myimg3
	b4=tk.Button(image=myimg4,command=lambda: disp_bal(accnt))
	b4.image=myimg4
	b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
	b5.image=myimg5
	
	img6=tk.PhotoImage(file="img/logout.png")
	myimg6=img6.subsample(2,2)
	b6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(rootwn))
	b6.image=myimg6

	
	b2.place(x=100,y=150)
	b3.place(x=100,y=220)
	b4.place(x=750,y=150)
	b5.place(x=750,y=220)
	b6.place(x=450,y=400)

	
def logout(master):
	
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()
	Main_Menu()

def check_log_in(master,name,acc_num,pin):
	if(check_acc_nmb(acc_num)==0):
		master.destroy()
		Main_Menu()
		return

	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		Main_Menu()
	else:
		master.destroy()
		logged_in_menu(acc_num,name)


def log_in(master):
	master.destroy()
	loginwn=tk.Tk()
	loginwn.geometry("1500x635")
	loginwn.title("Log in")
	loginwn.configure(bg="orange")
	fr1=tk.Frame(loginwn,bg="blue")
	l_title=tk.Message(loginwn,text="ACCOUNT LOGIN",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Times New Roman","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(loginwn,text="Enter Name:",font=("Times New Roman","30","bold"),bg="orange",relief="flat")
	l1.pack(side="top")
	e1=tk.Entry(loginwn,width=30,font=("Times New Roman","28","bold"))
	e1.pack(side="top")
	l2=tk.Label(loginwn,text="Enter account number:",font=("Times New Roman","30","bold"),bg="orange",relief="flat")
	l2.pack(side="top")
	e2=tk.Entry(loginwn,width=30,font=("Times New Roman","28","bold"))
	e2.pack(side="top")
	l3=tk.Label(loginwn,text="Enter your PIN:",font=("Times New Roman","30","bold"),bg="orange",relief="flat")
	l3.pack(side="top")
	e3=tk.Entry(loginwn,width=30,font=("Times New Roman","28","bold"),show="*")
	e3.pack(side="top")
	b=tk.Button(loginwn,text="Submit",font=("Times New Roman","30","bold"),bg="red",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	b1=tk.Button(text="HOME",relief="raised",font=("Times New Roman","30","bold"),bg="black",fg="white",command=lambda: home_return(loginwn))
	b1.pack(side="bottom")
	loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	

def Create():
	
	crwn=tk.Tk()
	crwn.geometry("1500x1000")
	crwn.title("Create Account")
	crwn.configure(bg="orange")
	l_title=tk.Message(crwn,text="Create New Account",relief="flat",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Times New Roman","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(crwn,text="Enter Name:",font=("Times New Roman","30","bold"),bg="orange",relief="flat")
	l1.pack(side="top")
	e1=tk.Entry(crwn,width=30,font=("Times New Roman","28","bold"))
	e1.pack(side="top")
	l2=tk.Label(crwn,text="Enter opening credit:",font=("Times New Roman","30","bold"),bg="orange",relief="flat")
	l2.pack(side="top")
	e2=tk.Entry(crwn,width=30,font=("Times New Roman","28","bold"))
	e2.pack(side="top")
	l3=tk.Label(crwn,text="Enter desired PIN:",font=("Times New Roman","30","bold"),bg="orange",relief="flat")
	l3.pack(side="top")
	e3=tk.Entry(crwn,width=30,font=("Times New Roman","28","bold"),show="*")
	e3.pack(side="top")
	b=tk.Button(crwn,text="Submit",font=("Times New Roman","30","bold"),bg="red",command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	crwn.bind("<Return>",lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	return


def Main_Menu():
	

	rootwn=tk.Tk()
	rootwn.geometry("1550x1100")
	rootwn.title("Personal Banking")
	rootwn.configure(background='orange')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	bg_image =ImageTk.PhotoImage(Image.open("img/currency.jpg"))
	x = tk.Label (image = bg_image)
	x.place(y=-400)
	l_title=tk.Message(text="IDFC BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Times New Roman","50","bold"))
	l_title.pack(side="top")
	imgc1=tk.PhotoImage(file="img/new.png")
	imglo=tk.PhotoImage(file="img/login.png")
	imgc=imgc1.subsample(2,2)
	imglog=imglo.subsample(2,2)

	b1=tk.Button(image=imgc,command=Create)
	b1.image=imgc
	b2=tk.Button(image=imglog,command=lambda: log_in(rootwn))
	b2.image=imglog
	img6=tk.PhotoImage(file="img/quit.png")
	myimg6=img6.subsample(2,2)

	b6=tk.Button(image=myimg6,command=rootwn.destroy)
	b6.image=myimg6
	b1.place(x=800,y=300)
	b2.place(x=800,y=200)	
	b6.place(x=800,y=400)

	rootwn.mainloop()

Main_Menu()
