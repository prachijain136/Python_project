from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext
import socket
import requests
import cx_Oracle
import matplotlib.pyplot as plt
import numpy as np
########################
class UsExRno(Exception):
	def __init__(self,msg):	
		self.msg=msg
class UsExName(Exception):
	def __init__(self,msg):	
		self.msg=msg
class UsExMarks(Exception):
	def __init__(self,msg):	
		self.msg=msg

def Rno(rno):
	rno=rno.strip()
	if len(rno)==0:
		raise UsExRno("RollNo. cannot be empty")
	if rno.isdigit()==False:
		raise  UsExRno("RollNo. should be Integer")
	if int(rno)<=0:
		raise UsExRno("Please enter +ve Rollno.") 

def Name(name):
	name=name.strip().title()
	if len(name)==0:
		raise UsExName("Name cannot be empty")
	if all(x.isalpha() or x.isspace() for x in name):
		pass
	else:
    		raise UsExName("Only A-Z/a-z characters allowed")
	if len(name)<3:
		raise UsExName("Name cannot be too small")
def Marks(marks):
	marks=marks.strip()
	if len(marks)==0:
		raise UsExMarks("Marks cannot be empty")
	
	if marks.isdigit()==False:
		raise  UsExMarks("Marks should be Integer")
	if int(marks)<0 or int(marks)>100:
		raise UsExMarks("Marks should be in btw 0-100") 
	
	
	
#################################
root=Tk()
root.title("CRUD operation")
root.geometry("400x600+500+150")
root.config(bg="steelblue")
#####################################

def f1():
	root.withdraw()
	addst.deiconify()
def f2():
	addst.withdraw()
	root.deiconify()
def f3():
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print("connected")
		print(con.version)
		root.withdraw()
		viewst.deiconify()
		cursor=con.cursor()
		sql="select * from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg+"r:  "+str (d[0])+"n:  "+d[1].title()+"m:  "+str(d[2])+"\n"
		
		stData.insert(INSERT,msg)
		
	except cx_Oracle.DatabaseError as e:
		print("some issuse",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("Disconnected")
	
	
def f4():
	viewst.withdraw()
	stData.delete("1.0",END)
	root.deiconify()
def f5():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print("connected")
		print(con.version)
		grno=(entRno.get())
		gname=entName.get().strip()
		gmarks=(entMarks.get())
		Rno(grno)
		Name(gname)
		Marks(gmarks)
		grno=int(grno)
		gmarks=int(gmarks)
		cursor=con.cursor()
		sql="insert into students values('%d','%s','%d')"
		args=(grno,gname,gmarks)
		cursor.execute(sql%args)
		con.commit()
		print(cursor.rowcount,"records inserted")
		msg="1 record inseretd"
		messagebox.showinfo("sahi kiya re",msg)
		entRno.delete(0,END)
		entRno.focus()
		entName.delete(0,END)
		entMarks.delete(0,END)
	except UsExRno as r:
		messagebox.showwarning("Galat kiya re",r.msg)
		entRno.delete(0,END)
		entRno.focus()
		con.rollback()
	except UsExName as n:
		messagebox.showwarning("Galat kiya re",n.msg)
		entName.delete(0,END)
		entName.focus()
		con.rollback()
	except UsExMarks as m:
		messagebox.showwarning("Galat kiya re",m.msg)
		entMarks.delete(0,END)
		entMarks.focus()
		con.rollback()
		
	except cx_Oracle.DatabaseError as e:
		print("some issuese",e)
		messagebox.showwarning("Galat kiya ","Two students cannot have same rollno.")
		entRno.delete(0,END)
		entName.delete(0,END)
		entMarks.delete(0,END)
		entRno.focus()
		con.rollback()
	except Exception as e:
		messagebox.showwarning("Galat kiya re",e)
		entRno.delete(0,END)
		entName.delete(0,END)
		entMarks.delete(0,END)
		entRno.focus()
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("Disconnected")
	
def f6():
	root.withdraw()
	updatest.deiconify()
def f7():
	updatest.withdraw()
	root.deiconify()
def f8():
	root.withdraw()
	deletest.deiconify()
def f9():
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print("connected")
		print(con.version)
		gname=entuName.get()
		gmarks=(entuMarks.get())
		grno=(entuRno.get())
		Rno(grno)
		Name(gname)
		Marks(gmarks)
		grno=int(grno)
		gmarks=int(gmarks)
		cursor=con.cursor()
		sql="update students set name='%s' ,marks='%d' where rno='%d'"
		args=(gname,gmarks,grno)
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+" record updated"
		messagebox.showinfo("sahi kiya re",msg)
		entuRno.delete(0,END)
		entuRno.focus()
		entuName.delete(0,END)
		entuMarks.delete(0,END)
		
		
	except UsExRno as r:
		messagebox.showwarning("Galat kiya re",r.msg)
		entuRno.delete(0,END)
		entuRno.focus()
		con.rollback()
	except UsExName as n:
		messagebox.showwarning("Galat kiya re",n.msg)
		entuName.delete(0,END)
		entuName.focus()
		con.rollback()
	except UsExMarks as m:
		messagebox.showwarning("Galat kiya re",m.msg)
		entuMarks.delete(0,END)
		entuMarks.focus()
		con.rollback()
	except cx_Oracle.DatabaseError as e:
		print("RollNO does not exist",e)
		messagebox.showwarning("Galat kiya re","RollNO does not exist")
		con.rollback()
	except Exception as e:
		messagebox.showwarning("Galat kiya re",e)
		entuRno.delete(0,END)
		entuName.delete(0,END)
		entuMarks.delete(0,END)
		entuRno.focus()
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("Disconnected")
	
def f10():	
	import cx_Oracle
	con=None
	cursor=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print("connected")
		print(con.version)
		cursor=con.cursor()
		grno=(entdRno.get())
		Rno(grno)
		grno=int(grno)
		sql="delete from students where rno='%d'"
		args=(grno)
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+"record deleted"
		messagebox.showinfo("sahi kiya re",msg)
		entdRno.delete(0,END)
		entdRno.focus()
	except UsExRno as r:
		messagebox.showwarning("Galat kiya re",r.msg)
		entdRno.delete(0,END)
		entdRno.focus()
		con.rollback()
	except cx_Oracle.DatabaseError as e:
		print("some issuse",e)
		messagebox.showwarning("Galat kiya re","Rollno not present")
		con.rollback()
	except Exception as e:
		messagebox.showwarning("Galat kiya re",e)
		entdRno.delete(0,END)
		entdRno.focus()
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("Disconnected")
	
	

def f11():
	deletest.withdraw()
	root.deiconify()
def f12():
	
	import cx_Oracle
	con=None
	try:
		con=cx_Oracle.connect("system/abc123")
		print("connected")
		cursor=con.cursor()
		sql="select name,marks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		markli=[]
		nameli=[]
		for d in data:
			nameli.append(d[0])
			markli.append(d[1])
		x=np.arange(len(nameli))
		plt.bar(x,markli,width=0.25,color="r",alpha=0.5)
		plt.xticks(x,nameli,fontsize=14,rotation=30)
		plt.grid()
		plt.xlabel("Name",fontsize=12)
		plt.ylabel("Marks",fontsize=12)
		plt.show()
	except cx_Oracle.DatabaseError as e:
		print("some issuse",e)
		messagebox.showwarning("Galat kiya re","Rollno not present")
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("Disconnected")
def doSomething():
	root.destroy()
	
		
			
		
#######################################################3


btnAdd=Button(root,text="ADD",font=("arial",18,"bold"),command=f1)
btnView=Button(root,text="VIEW",font=("arial",18,"bold"),command=f3)
btnUpdate=Button(root,text="UPDATE",font=("arial",18,"bold"),command=f6)
btnDelete=Button(root,text="DELETE",font=("arial",18,"bold"),command=f8)
btnGraph=Button(root,text="GRAPH",font=("arial",18,"bold"),command=f12)
btnAdd.config(bg="dodgerblue4")
btnView.config(bg="dodgerblue4")
btnUpdate.config(bg="dodgerblue4")
btnDelete.config(bg="dodgerblue4")
btnGraph.config(bg="dodgerblue4")
############################################temp
socket.create_connection(("www.google.com",80))
res=requests.get("https://ipinfo.io/")
print(res)
data=res.json()
print(data)
city=data['city']
print(city)
lblLoc=Label(root,text=city,font=("arial",18,"bold"))
lblLoc.config(bg="skyblue")
a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
a2="&q="+city
a3="&appid=c6e315d09197cec231495138183954bd"
api_address=a1+a2+a3
res1=requests.get(api_address)
print(res1)
data=res1.json()
main=data['main']
print("tempertaure is",main['temp'])
lblTemp=Label(root,text=str(main['temp'])+"\u00b0",font=("arial",18,"bold"))
lblTemp.config(bg="skyblue")
###################################quote
import bs4
res1=requests.get("https://www.brainyquote.com/quote_of_the_day")
print(res1)
soup=bs4.BeautifulSoup(res1.text,'lxml')
quote=soup.find('img',{"class":"p-qotd"})
text=quote['alt']
lblQuote=Message(root,text=text,font=("arial",10,"bold"))
lblQuote.config(bg='lightgreen')
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)
lblLoc.pack(pady=10)

lblTemp.pack(pady=10)

lblQuote.pack(pady=10)

#####################################add frame
addst=Toplevel(root)
addst.protocol("WM_DELETE_WINDOW",doSomething)
addst.title("ADD STUDENT")
addst.geometry("500x500+300+200")
addst.withdraw()
lblRno=Label(addst,text="Enter rollno",font=("arial",18,"bold"))
entRno=Entry(addst,bd=5)
lblName=Label(addst,text="Enter name",font=("arial",18,"bold"))
entName=Entry(addst,bd=5)
lblMarks=Label(addst,text="Enter marks",font=("arial",18,"bold"))
entMarks=Entry(addst,bd=5)
btnAddsave=Button(addst,text="SAVE",font=("arial",18,"bold"),command=f5)
btnAddback=Button(addst,text="BACK",font=("arial",18,"bold"),command=f2)
lblRno.pack(pady=10)
entRno.pack(pady=10)
lblName.pack(pady=10)
entName.pack(pady=10)
lblMarks.pack(pady=10)
entMarks.pack(pady=10)
btnAddsave.pack(pady=10)
btnAddback.pack(pady=10)

#######################################view frame
viewst=Toplevel(root)
viewst.protocol("WM_DELETE_WINDOW",doSomething)
viewst.title("View Student")
viewst.geometry("400x300+300+200")
viewst.withdraw()
stData=scrolledtext.ScrolledText(viewst,width=40,height=10)
btnViewBack=Button(viewst,text="BACK",font=("arial",18,"bold"),command=f4)
stData.pack(pady=10)
btnViewBack.pack(pady=10)

######################################update frame
updatest=Toplevel(root)
updatest.protocol("WM_DELETE_WINDOW",doSomething)
updatest.title("UPDATE STUDENT")
updatest.geometry("500x500+300+200")
updatest.withdraw()
lbluRno=Label(updatest,text="Enter rollno",font=("arial",18,"bold"))
entuRno=Entry(updatest,bd=5)
lbluName=Label(updatest,text="Enter name",font=("arial",18,"bold"))
entuName=Entry(updatest,bd=5)
lbluMarks=Label(updatest,text="Enter marks",font=("arial",18,"bold"))
entuMarks=Entry(updatest,bd=5)
btnUpdatesave=Button(updatest,text="SAVE",font=("arial",18,"bold"),command=f9)
btnUpdateback=Button(updatest,text="BACK",font=("arial",18,"bold"),command=f7)
lbluRno.pack(pady=10)
entuRno.pack(pady=10)
lbluName.pack(pady=10)
entuName.pack(pady=10)
lbluMarks.pack(pady=10)
entuMarks.pack(pady=10)
btnUpdatesave.pack(pady=10)
btnUpdateback.pack(pady=10)


#################################################delete frame
deletest=Toplevel(root)
deletest.protocol("WM_DELETE_WINDOW",doSomething)
deletest.title("DELETE STUDENT")
deletest.geometry("400x400+300+200")
deletest.withdraw()
lbldRno=Label(deletest,text="Enter rollno",font=("arial",18,"bold"))
entdRno=Entry(deletest,bd=5)
btnDeletedelete=Button(deletest,text="DELETE",font=("arial",18,"bold"),command=f10)
btnDeleteback=Button(deletest,text="BACK",font=("arial",18,"bold"),command=f11)
lbldRno.pack(pady=10)
entdRno.pack(pady=10)
btnDeletedelete.pack(pady=10)
btnDeleteback.pack(pady=10)
############################################graph frame
'''graphst=Toplevel(root)
graphst.title("Graph Student")
graphst.geometry("500x500+200+200")
graphst.withdraw()'''

root.mainloop()


	

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       