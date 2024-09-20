from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "varun"
mydatabase="music_library"

con = pymysql.connect(host="localhost",user="root",password= mypass,database= mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "albums_issued" 
albumTable = "albums" #Album Table


def deleteAlbum():
    
    al_id = albumInfo1.get()
    
    deleteSql = "delete from "+albumTable+" where al_id = '"+al_id+"'"
    deleteIssue = "delete from "+issueTable+" where al_id = '"+al_id+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success',"Album Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Album ID")
    

    print(al_id)

    albumInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global albumInfo1,albumInfo2,albumInfo3,albumInfo4,Canvas1,con,cur,albumTable,root
    
    root = Toplevel()
    root.title("Delete Album")
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
        
    headingLabel = Label(headingFrame1, text="Delete Album", bg='black', fg='white', font=('Lucida Calligraphy',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Album ID to Delete
    lb2 = Label(labelFrame,text="Album ID : ", bg='black', fg='white', font=('Lucida Calligraphy',15))
    lb2.place(relx=0.05,rely=0.5)
        
    albumInfo1 = Entry(labelFrame)
    albumInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black', font=('Courier',15),command=deleteAlbum)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', font=('Courier',15), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
