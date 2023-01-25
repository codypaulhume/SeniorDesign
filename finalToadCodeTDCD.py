from tkinter import *
#from picamera import PiCamera, Color
from time import sleep

import os
import shutil

#camera = PiCamera()
#camera.rotation = 180
    
def save_info():
    toadname_info = toadname.get()
    
    #File Code
    
    path = "/media/pi/8E4C-0945/Toads' Data/Toad %s" % toadname_info
    try:
        os.mkdir(path)
    except OSError:
        print ("Nope")
    else:
        print("Yup")
    temp_info = temp.get()
    weatherCond_info = weatherCond.get()
    actStat_info = actStat.get()
    mSite_info = mSite.get()
    cObj_info = cObj.get()
    mass_info = mass.get()
    svl_info = svl.get()
    color_info = color.get()
    swabID_info = swabID.get()
    mBiome_info = mBiome.get()
    comments_info = actStat.get()
    
    print(toadname_info,temp_info,weatherCond_info,actStat_info,mSite_info,cObj_info,mass_info,svl_info,color_info,swabID_info,mBiome_info,comments_info)
    
    file = open("/media/pi/8E4C-0945/Toads' Data/Toad %s/Datasheet.txt" % toadname_info,"w")
    
    file.write("Toad ID: " + toadname_info)
    
    file.write("\n")
    
    file.write("Temperature: " + temp_info)
    
    file.write("\n")
    
    file.write("Weather Condition: " + weatherCond_info)

    file.write("\n")

    file.write("Activity Status: " + actStat_info)

    file.write("\n")

    file.write("Micro Site: " + mSite_info)

    file.write("\n")

    file.write("Cover Object: " + cObj_info)

    file.write("\n")

    file.write("Mass: " + mass_info)

    file.write("\n")

    file.write("Snout-Vent Length (mm): " + svl_info)

    file.write("\n")

    file.write("Color: " + color_info)

    file.write("\n")

    file.write("BD Swab ID: " + swabID_info)

    file.write("\n")

    file.write("Micro-Biome Swab ID: " + mBiome_info)

    file.write("\n")

    file.write("Comments: " + comments_info)

    file.write("\n")
    
    file.close()
    
    source = "/media/pi/8E4C-0945/Toads' Data/toadImage.png"
    
    destination = "/media/pi/8E4C-0945/Toads' Data/Toad %s" % toadname_info
    
    shutil.move(source, destination)
    
def take_pic():
    camera.start_preview()
    camera.annotate_text_size = 75
    #camera.framerate = 15
    #camera.annotate_background = Color('black')
    #camera.annotate_foreground = Color('white')
    camera.annotate_text = "3"
    sleep(1)
    camera.annotate_text = "2"
    sleep(1)
    camera.annotate_text = "1"
    sleep(1)
    camera.annotate_text = ""
    camera.capture("/media/pi/8E4C-0945/Toads' Data/toadImage.png")
    camera.stop_preview()

app = Tk()

#GUI Setup

app.geometry("800x1200")

app.title("Toad Data Collection Sheet")

heading = Label(text="Toad Data Collection Sheet",fg="black",bg="white",width="800",height="3",font="80")

heading.pack()

#Text Label for GUI

toadname_text = Label(text="Toad ID:")
temp_text = Label(text="Temperature:")
weatherCond_text = Label(text="Weather Condition:")
actStat_text = Label(text="Activity Status:")
mSite_text = Label(text="Micro Site:")
cObj_text = Label(text="Cover Object:")
mass_text = Label(text="Mass (g):")
svl_text = Label(text="Snout-Vent Length (mm):")
color_text = Label(text="Color:")
swabID_text = Label(text="BD Swab ID:")
mBiome_text = Label(text="Micro-Biome Swab ID:")
comments_text = Label(text="Comments:")

#Text Location for GUI

toadname_text.place(x=15,y=65)
temp_text.place(x=15,y=120)
weatherCond_text.place(x=15,y=175)
actStat_text.place(x=15,y=230)
mSite_text.place(x=15,y=285)
cObj_text.place(x=15,y=340)
mass_text.place(x=250,y=65)
svl_text.place(x=250,y=120)
color_text.place(x=250,y=175)
swabID_text.place(x=250,y=230)
mBiome_text.place(x=250,y=285)
comments_text.place(x=250,y=340)

#Value of Entry

toadname = StringVar()
temp = StringVar()
weatherCond = StringVar()
actStat = StringVar()
#8 MORE
mSite = StringVar()
cObj = StringVar()
mass = StringVar()
svl = StringVar()
color = StringVar()
swabID = StringVar()
mBiome = StringVar()
comments = StringVar()

#Size of Entry

toadname_entry = Entry(textvariable=toadname,width="20")
temp_entry = Entry(textvariable=temp,width="20")
weatherCond_entry = Entry(textvariable=weatherCond,width="20")
actStat_entry = Entry(textvariable=actStat,width="20")
mSite_entry = Entry(textvariable=mSite,width="20")
cObj_entry = Entry(textvariable=cObj,width="20")
mass_entry = Entry(textvariable=mass,width="20")
svl_entry = Entry(textvariable=svl,width="20")
color_entry = Entry(textvariable=color,width="20")
swabID_entry = Entry(textvariable=swabID,width="20")
mBiome_entry = Entry(textvariable=mBiome,width="20")
comments_entry = Entry(textvariable=comments,width="20")

#Entry Location on GUI

toadname_entry.place(x=15,y=90)
temp_entry.place(x=15,y=145)
weatherCond_entry.place(x=15,y=200)
actStat_entry.place(x=15,y=255)
mSite_entry.place(x=15,y=310)
cObj_entry.place(x=15,y=365)
mass_entry.place(x=250,y=90)
svl_entry.place(x=250,y=145)
color_entry.place(x=250,y=200)
swabID_entry.place(x=250,y=255)
mBiome_entry.place(x=250,y=310)
comments_entry.place(x=250,y=365)

#Save info button

button = Button(app,text="Submit Data",command=save_info,width="15",height="2",fg="white", bg="green", font="50")

button.place(x=500,y=160)

cameraButton = Button(app,text="Take Photo",command=take_pic,width="15",height="2",fg="white", bg="blue", font="50")

cameraButton.place(x=500, y=90)

mainloop()
