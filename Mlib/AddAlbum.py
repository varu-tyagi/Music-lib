from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def albumRegister():
    
    al_id = albumInfo1.get()
    title = albumInfo2.get()
    singer = albumInfo3.get()
    status = albumInfo4.get()
    status = status.lower()
    
    insertAlbums = "insert into "+albumTable+" values('"+al_id+"','"+title+"','"+singer+"','"+status+"')"
    try:
        cur.execute(insertAlbums)
        con.commit()
        messagebox.showinfo('Success',"Album added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(al_id)
    print(title)
    print(singer)
    print(status)


    root.destroy()
    
def addAlbum(): 
    
    global albumInfo1,albumInfo2,albumInfo3,albumInfo4,Canvas1,con,cur,albumTable,root
    
    root = Toplevel()
    root.title("Add Album")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "varun"
    mydatabase="music_library"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    albumTable = "albums" # Album Table

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

    headingLabel = Label(headingFrame1, text="Add albums", bg='black', fg='white', font=('Lucida Calligraphy',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Album ID
    lb1 = Label(labelFrame,text="Album ID : ", bg='black', fg='white', font=('Lucida Calligraphy',15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    albumInfo1 = Entry(labelFrame)
    albumInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white', font=('Lucida Calligraphy',15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    albumInfo2 = Entry(labelFrame)
    albumInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Album Singer
    lb3 = Label(labelFrame,text="Singer : ", bg='black', fg='white', font=('Lucida Calligraphy',15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    albumInfo3 = Entry(labelFrame)
    albumInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
    # Album Status
    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white', font=('Lucida Calligraphy',15))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    albumInfo4 = Entry(labelFrame)
    albumInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black', font=('Courier',15),command=albumRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', font=('Courier',15), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
