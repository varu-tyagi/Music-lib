from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "varun"
mydatabase="music_library"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "albums_issued" 
albumTable = "albums"
    
#List To store all Album IDs
allal_id = [] 

def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    al_id = inf1.get()
    issued_to = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extractal_id = "select al_id from "+albumTable
    try:
        cur.execute(extractal_id)
        con.commit()
        for i in cur:
            allal_id.append(i[0])
        
        if al_id in allal_id:
            checkavail = "select status from "+albumTable+" where al_id = '"+al_id+"'"
            cur.execute(checkavail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == "'avail'":
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Album ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Album IDs")
    
    issueSql = "insert into "+issueTable+" values ('"+al_id+"','"+issued_to+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+albumTable+" set status = 'issued' where al_id = '"+al_id+"'"
    try:
        if al_id in allal_id and status == False:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Album Issued Successfully")
            root.destroy()
        else:
            allal_id.clear()
            messagebox.showinfo('Message',"Album Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(al_id)
    print(issued_to)
    
    allal_id.clear()
    
def issueAlbum(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Toplevel()
    root.title("Issue Album")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    same=True
    n=2
    # Adding a background image
    background_image =Image.open("op2.png")
    [imageSizeWidth, imageSizeHeight] = background_image.size
    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
    
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(root)
    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Album", bg='black', fg='white', font=('Lucida Calligraphy',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Album ID
    lb1 = Label(labelFrame,text="Album ID : ", bg='black', fg='white', font=('Lucida Calligraphy',15))
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white', font=('Lucida Calligraphy',15))
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black', font=('Courier',15),command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', font=('Courier',15), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
