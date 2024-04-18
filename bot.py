from tkinter import *
import sqlite3
from datetime import date

conn=sqlite3.connect(r"D:\sqlite\Chatbot.db")
cur=conn.cursor()


count=0
check=False

def Total_leaves():
    global check,count
    if check==True:
        sum=0
        (cur.execute("select * from Available_Leaves where employee_id='{}'".format(uid)))
        rows=cur.fetchall()
        for row in rows:
            sum=row[1]+row[2]+row[3]
        print("The total number of leaves are",sum)
        chatWindow.insert(END, "Bot : The total leaves: "+ str(sum) +'\n\n')
        chatWindow.config(font=("Verdana",12))
        chatWindow.insert(END, "Bot : Anything else" +'\n\n')
        chatWindow.see('end')
    else:
        chatWindow.insert(END,"Enter your uid" + '\n\n')
        count=count+1
   

def Casual_leaves():
    global check,count
    if check==True:
        sum=0
        (cur.execute("select * from Available_Leaves where employee_id='{}'".format(uid)))
        rows=cur.fetchall()
        for row in rows:
            sum=row[1]
        print("The total number of casual leaves are",sum)
        chatWindow.insert(END, "Bot:The total Casual leaves: "+ str(sum) +'\n\n')
        chatWindow.config(font=("Verdana",12))
        chatWindow.insert(END, "Bot : Anything else" +'\n\n')
        chatWindow.see('end')
    else:
         chatWindow.insert(END,"Enter your uid" + '\n\n')
         count=count+1
def Sick_leaves():
    global check,count
    if check==True:
        sum=0
        (cur.execute("select * from Available_Leaves where employee_id='{}'".format(uid)))
        rows=cur.fetchall()
        for row in rows:
            sum=row[2]
        print("The total number of sick leaves are",sum)
        chatWindow.insert(END, "Bot:The total Sick leaves: "+ str(sum) +'\n\n')
        chatWindow.config(font=("Verdana",12))
        chatWindow.insert(END, "Bot : Anything else" +'\n\n')
        chatWindow.see('end')
    else:
         chatWindow.insert(END,"Enter your uid" + '\n\n')
         count=count+1   
    
def Paid_leaves():
    global check,count
    if check==True:
        sum=0
        (cur.execute("select * from Available_Leaves where employee_id='{}'".format(uid)))
        rows=cur.fetchall()
        for row in rows:
            sum=row[3]
        print("The total number of  paid leaves are",sum)
        chatWindow.insert(END, "Bot:The total Paid leaves: "+ str(sum) +'\n\n')
        chatWindow.config(font=("Verdana",12))
        chatWindow.insert(END, "Bot : Anything else" +'\n\n')
        chatWindow.see('end')
    else:
         chatWindow.insert(END,"Enter your uid" + '\n\n')
         count=count+1   
    
def Total_Salary():
    global check,count
    if check==True:
        sum=0
        (cur.execute("select * from Health_Insurance_Details where employee_id='{}'".format(uid)))
        rows=cur.fetchall()
        for row in rows:
            value=row[3]
            if value=='Yes':
                premium_amt=row[6]
                premium_amt=premium_amt/3
        (cur.execute("select * from Salary_Details where employee_id='{}'".format(uid)))
        rows=cur.fetchall()
        for row in rows:
            if value=='No':
                sum=row[1]+row[2]+row[3]
                chatWindow.insert(END, "The Salary is:  "+ str(sum) +'\n\n')
                chatWindow.config(font=("Verdana",12)) 
            elif value=='Yes':
                sum=row[1]+row[2]+row[3]
                chatWindow.insert(END, "The Salary is:  "+ str(sum) +'\n\n')
                sum=sum-premium_amt
                chatWindow.insert(END, "The Salary(March,April,May) after deducting insurance premium amount:  "+ str(sum) +'\n\n')
                chatWindow.config(font=("Verdana",12))
        chatWindow.insert(END, "Bot : Anything else" +'\n\n')
        chatWindow.see('end')
    else:
         chatWindow.insert(END,"Enter your uid" + '\n\n')
         count=count+1         
    
def Basic_Salary():
    global check,count
    if check==True:
        sum=0
        (cur.execute("select * from Salary_Details where employee_id='{}'".format(uid)))
        rows=cur.fetchall()
        for row in rows:
            sum=row[1]
        print("The Basic Salary is: ",sum)
        chatWindow.insert(END, "The Basic Salary is:  "+ str(sum) +'\n\n')
        chatWindow.config(font=("Verdana",12)) 
        chatWindow.insert(END, "Bot : Anything else" +'\n\n')
        chatWindow.see('end')
    else:
        chatWindow.insert(END,"Enter your uid" + '\n\n')
        count=count+1     
    
def HR():
    global check,count
    if check==True:
        sum=0
        (cur.execute("select * from Salary_Details where employee_id='{}'".format(uid)))
        rows=cur.fetchall()
        for row in rows:
            sum=row[2]
        print("The Salary is: ",sum)
        chatWindow.insert(END, "The HR Salary is:  "+ str(sum) +'\n\n')
        chatWindow.config(font=("Verdana",12))
        chatWindow.insert(END, "Bot : Anything else" +'\n\n')
        chatWindow.see('end')
    else:
         chatWindow.insert(END,"Enter your uid" + '\n\n')
         count=count+1    
def Others():
    global check,count
    if check==True:
        sum=0
        (cur.execute("select * from Salary_Details where employee_id='{}'".format(uid)))
        rows=cur.fetchall()
        for row in rows:
            sum=row[3]
        print("The Salary is: ",sum)
        chatWindow.insert(END, "others:  "+ str(sum) +'\n\n')
        chatWindow.config(font=("Verdana",12))
        chatWindow.insert(END, "Bot : Anything else" +'\n\n')
        chatWindow.see('end')
    else:
        chatWindow.insert(END,"Enter your uid" + '\n\n')
        count=count+1    
    
def Holidayofyear(a):
    global check,count
    if check==True:
         if a=='all':
              (cur.execute("select * from Holiday_List"))
         else:
              (cur.execute("select * from Holiday_List where month='{}'".format(a)))
              
         rows=cur.fetchall()
         if len(rows)==0:
              chatWindow.insert(END,'No Holidays in this month' +'\n\n')
         else:
             m='Month\t\tDate\t\tDay\t\tFestival'
             chatWindow.insert(END,m+'\n\n')
             for row in rows:
                 print(type(row[3]))
                 chatWindow.insert(END,row[0]+'\t\t'+row[1]+'\t\t'+row[2]+'\t\t'+row[3])
                 chatWindow.insert(END,'\n\n')
                 chatWindow.config(font=("Verdana",12))
         chatWindow.insert(END, "Bot : Anything else" +'\n\n')
         chatWindow.see('end')
    else:
        chatWindow.insert(END,"Enter your uid" + '\n\n')
        count=count+1

def PF_details():
    global check,count
    if check==True:
        val=0
        chatWindow.config(state=NORMAL)
        (cur.execute("select * from Salary_Details where employee_id='{}'".format(uid)))
        rows=cur.fetchall()
        for row in rows:
            val=2*(0.12*row[1])
            print(val)
        chatWindow.insert(END, "The PF is: "+ str(val) +'\n\n')    
        chatWindow.config(font=("Verdana",12))    
        chatWindow.insert(END, "Bot : Anything else" +'\n\n')
        chatWindow.see('end')
    else:
        chatWindow.insert(END,"Enter your uid" + '\n\n')
        count=count+1
def health_insurance_details():
    global check,count
    if check==True:
        (cur.execute("select * from Health_Insurance_Details where employee_id='{}'".format(uid)))
        rows=cur.fetchall()
        for row in rows:
            chatWindow.insert(END, "Group Mediclaim Policy: " + str(row[1]) + " Total amount: "+ "  "+ str(row[2]) + '\n\n')
            val=row[3]
            if val=='Yes':
                chatWindow.insert(END, "Parental Policy:" + str(row[3]) + "   " + " Total amount:"+ str(row[4]) + "  "+"Opted members:" + str(row[5]) +"  "+"Premium amount:" + str(row[6]) + "  "+ "Highest age band:" + str(row[7]) + '\n\n')
            elif val=='No':
                 chatWindow.insert(END, "Parental Policy: " + str(row[3]) +  '\n\n')
                 
        chatWindow.config(font=("Verdana",12))
        chatWindow.insert(END, "Bot : Anything else" +'\n\n')
        chatWindow.see('end')
    else:
        chatWindow.insert(END,"Enter your uid" + '\n\n')
        count=count+1


def uid_check(msg):
    flag=0
    global check
    global uid
    global chatWindow1
    if conn is not None:
        (cur.execute("select * from Available_Leaves"))
        print("Connected successfully")
    else:
        print("Error while connecting database")
                
    rows=cur.fetchall()
    for row in rows:
        if msg==row[0]:
            flag=1
            break
    if flag==1:
        print("Valid user")
        uid=msg
        check=True
        chatWindow.insert('end', "Bot:"+'How can i help you'+'\n\n')
    else:
        print("invalid user")      
        chatWindow.insert(END, "Bot: " + "WRONG-Enter Again" + '\n\n')
        
                
def send():
     global count
     global msg
     msg=msgWindow.get('1.0','end-1c').strip()
     msgWindow.delete("1.0", "end")
     chatWindow.config(state=NORMAL)
     chatWindow.insert('end', "You:"+msg+'\n\n')
     if 'uie' in msg:
          uid_check(msg)
     
     if (re.search('leaves|leave',msg,re.IGNORECASE)):
          if(re.search('sick|Sick',msg,re.IGNORECASE)):
               Sick_leaves()
          elif(re.search('paid|Paid',msg,re.IGNORECASE)):
               Paid_leaves()
          elif(re.search('Casual|casual',msg,re.IGNORECASE)):
               Casual_leaves()
          else:
               Total_leaves()
               
     if (re.search('insurance|policy|Insurance',msg,re.IGNORECASE)):
          health_insurance_details()

     if (re.search('Salary|salary',msg,re.IGNORECASE)):
          if(re.search('basic|Basic',msg,re.IGNORECASE)):
               Basic_Salary()
          elif(re.search('HR|hr|Hr',msg,re.IGNORECASE)):
               HR()
          elif(re.search('Others|others',msg,re.IGNORECASE)):
               Others()
          else:
               Total_Salary()
          
     if (re.search('holidays|holiday',msg,re.IGNORECASE)):
          if(re.search('January|jan',msg,re.IGNORECASE)):
               Holidayofyear('Jan')

          elif(re.search('feb|feburary',msg,re.IGNORECASE)):
               Holidayofyear('Feb')

          elif(re.search('March|mar',msg,re.IGNORECASE)):
               Holidayofyear('Mar')

          elif(re.search('April|april',msg,re.IGNORECASE)):
               Holidayofyear('Apr')

          elif(re.search('May|may',msg,re.IGNORECASE)):
               Holidayofyear('May')

          elif(re.search('June|jun',msg,re.IGNORECASE)):
               Holidayofyear('Jun')

          elif(re.search('July|jul',msg,re.IGNORECASE)):
               Holidayofyear('Jul')

          elif(re.search('August|Aug',msg,re.IGNORECASE)):
               Holidayofyear('Aug')

          elif(re.search('September|Sept|sep',msg,re.IGNORECASE)):
               Holidayofyear('Sep')

          elif(re.search('October|oct',msg,re.IGNORECASE)):
               Holidayofyear('Oct')

          elif(re.search('November|Nov',msg,re.IGNORECASE)):
               Holidayofyear('Nov')

          elif(re.search('December|Dec',msg,re.IGNORECASE)):
               Holidayofyear('Dec')

          elif(re.search('This',msg,re.IGNORECASE)):
               today = date.today()
               d2 = today.strftime("%B")
               Holidayofyear(d2[:3])
          else:
               Holidayofyear('all')

          

     if(re.search('No|thank|Bye',msg,re.IGNORECASE)):
          chatWindow.insert(END, "BOT:"+'Bye!..Have a nice day.'+'\n\n')

     if(re.search('pf|PF|pF|Pf',msg,re.IGNORECASE)):
          PF_details()
          
     if count==0:
          chatWindow.insert("end", "Bot: " + "Enter your uid" + '\n\n')
          count=count+1

 

 

          
root=Tk()
root.title("Chat Bot")
root.geometry("1000x500")
root.resizable(width=True,height=True)
f=Frame(root)
f.pack(fill=BOTH,expand=True)

chatWindow = Text(f, bd=1, bg="white",  width="50", height="11", font=("Arial", 23), foreground="#00ffff")
chatWindow.pack(side=LEFT,fill=BOTH,expand=True)
chatWindow.config(state=DISABLED)

scrollbar = Scrollbar(f, command=chatWindow.yview, cursor="arrow")
chatWindow['yscrollcommand'] = scrollbar.set
scrollbar.pack(side=RIGHT)
chatWindow.config(state=NORMAL)
chatWindow.insert(END, "Bot:"+'hello'+'\n\n')
chatWindow.config(foreground="#442265", font=("Verdana", 12 ))

f1=Frame(root)
f1.pack(fill=BOTH)

msgWindow = Text(f1, bd=0, bg="gray",width="10", height="2", font=("Arial", 15), foreground="#00ffff")
msgWindow.pack(side=RIGHT,fill=BOTH,expand=True)

Button1= Button(f1, text="Send",  width="7", height=1,padx=4,bd=1, bg="blue", activebackground="green",foreground='#ffffff',font=("Arial", 12),command=send)
Button1.pack(side=RIGHT,fill=BOTH)


root.mainloop()
