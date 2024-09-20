import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox

def records_issued():
   df=pd.read_csv("C:\\Users\\varun\\Downloads\\Mlib\\records.csv")
   print(df)

def graph():
    songs=["Shape of You","God's Plan","Old Town Road","Blinding Lights","Levitating"]
    Records_is=[8994,6568,7570,7100,10942]
    plt.title("Most issued songs of the year")
    plt.xlabel("Name of songs")
    plt.ylabel("No. of albums issued")
    plt.bar(songs,Records_is)
    plt.show()
