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
issueTable = "albums_issued" #Issue Table
albumTable = "albums" #Album Table


allal_id = [] #List To store all Album IDs

def returnn():
    global SubmitBtn,labelFrame,lb1,albumInfo1,quitBtn,root,Canvas1,status
    
    al_id = albumInfo1.get()

    extractal_id = "select al_id from "+issueTable
    try:
        cur.execute(extractal_id)
        con.commit()
        for i in cur:
            allal_id.append(i[0])
        
        if al_id in allal_id:
            checkAvail = "select status from "+albumTable+" where al_id = '"+al_id+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Album ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Album IDs")
    
    
    issueSql = "delete from "+issueTable+" where al_id = '"+al_id+"'"
  
    print(al_id in allal_id)
    print(status)
    updateStatus = "update "+albumTable+" set status = 'avail' where al_id = '"+al_id+"'"
    try:
        if al_id in allal_id and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Album Returned Successfully")
        else:
            allal_id.clear()
            messagebox.showinfo('Message',"Please check the album ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allal_id.clear()
    root.destroy()
    
def returnAlbum(): 
    
    global albumInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Toplevel()
    root.title("Return Album")
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
        
    headingLabel = Label(headingFrame1, text="Return Album", bg='black', fg='white', font=('Lucida Calligraphy',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Album ID to Delete
    lb1 = Label(labelFrame,text="Album ID : ", bg='black', fg='white', font=('Lucida Calligraphy',15))
    lb1.place(relx=0.05,rely=0.5)
        
    albumInfo1 = Entry(labelFrame)
    albumInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black', font=('Courier',15),command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', font=('Courier',15), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
