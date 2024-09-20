from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddAlbum import *
from DeleteAlbum import *
from ViewAlbum import *
from IssueAlbum import *
from ReturnAlbum import *
from records_issused import *
# Add your own database name and password here to reflect in the code

root =Tk()

root.title("Rhythm Music Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

mypass = "varun"
mydatabase="music_library"

con = pymysql.connect(host="localhost",user="root",password= mypass,database= mydatabase)
cur = con.cursor()

same=True
n=1.25

# Adding a background image
background_image =Image.open("mlib.jpg")
[ImageSizeWidth, ImageSizeHeight] = background_image.size

newImageSizeWidth = int(ImageSizeWidth*n)
if same:
    newImageSizeHeight = int(ImageSizeHeight*n) 
else:
    newImageSizeHeight = int(ImageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="black",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Rhythm Music Library", bg='black', fg='white', font=('Ink Free',25))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Album Details",bg='black', fg='white', font=('Ink Free',15), command=addAlbum)
btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.075)
    
btn2 = Button(root,text="Delete Album",bg='black', fg='white', font=('Ink Free',15), command=delete)
btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.075)
    
btn3 = Button(root,text="View Album List",bg='black', fg='white', font=('Ink Free',15), command=View)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.075)
    
btn4 = Button(root,text="Issue Album",bg='black', fg='white', font=('Ink Free',15), command = issueAlbum)
btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.075)
    
btn5 = Button(root,text="Return Album",bg='black', fg='white', font=('Ink Free',15), command = returnAlbum)
btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.075)

btn6 = Button(root,text="Records Issued",bg='black', fg='white', font=('Ink Free',15), command = records_issued)
btn6.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.075)

btn7 = Button(root,text="Records Graph",bg='black', fg='white', font=('Ink Free',15), command = graph)
btn7.place(relx=0.28,rely=0.9, relwidth=0.45,relheight=0.075)

root.mainloop()
