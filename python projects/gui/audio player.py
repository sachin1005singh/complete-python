# here  we create an audio player
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pygame import mixer
from  mutagen.mp3 import MP3
# muagen is used to extract meta data from mp3 file like length of file length = 7:30
root = Tk()


mixer.init()   # initializing the mixer

root.title("SoundPlay")
root.wm_iconbitmap("images/gost.ico")
root.minsize(height=400,width=600)


# create menu bar
menubar= Menu(root)
root.config(menu=menubar)


filelabel = Label(root,text="Lets make some noise")
filelabel.pack(pady=15)

lengthlabel = Label(root,text="Total length - 00:00")
lengthlabel.pack(pady=15)

# create the submenu bar


subMenu = Menu(menubar,tearoff=0)


def browse_file():
    global  file_name
    filename = filedialog.askopenfile()
    print(filename)
    file_name = filename.name



menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Open",command=browse_file)
subMenu.add_command(label="Exit" ,command=root.destroy)

def about_us():
    messagebox.showinfo("About SoundPlay","This project is based on python and we used tkinter to create it.")

subMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About us",command=about_us)



# we create frame here to pack buttons

middleframe = Frame(root,relief=RAISED)
middleframe.pack(pady=15,padx=20)


#function for buttons
def show_details():
    filelabel['text']="Playing music" +"  " + os.path.basename(file_name)
    filedata = os.path.splitext(file_name)
    #print(filedata)
    if filedata[1] == 'mp3':
        auido = MP3(file_name)
        total_length = auido.info.length
        lengthlabel['text'] = "Total length : " + total_length
    else:
        a = mixer.Sound(file_name)
        total_length = a.get_length()
        mins,secs = divmod(total_length,60)
        mins = round(mins)
        secs = round(secs)
        timeformat = '(:02d):(:02d)'.format(mins,secs)
        lengthlabel['text'] = "Total length " + timeformat






def play_music():
    global paused
    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"
        paused =False

    else:

        try:
            mixer.music.load(file_name)
            mixer.music.play()
            statusbar['text'] ="Playing music" +"  " + os.path.basename(file_name)
            show_details()
        except:
            messagebox.showerror("file is not available","SoundPLay could not find the file. please check again")


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Stopped music"


paused=False

def set_vol(val):           # scale value is gone into val variable and the value is in string form
    volume = int(val)/100
    mixer.music.set_volume(volume)
# set the volume of mixer take values only from 0 to 1 example 0.1,0.5,0.7,1
def pause_music():
    global paused
    paused = True
    mixer.music.pause()
    statusbar['text']= "Music paused"



def rewind_music():
    play_music()
    statusbar['text'] = "Music Rewind"



muted = False
def mute_music():
    global muted
    if muted:   #unmute the music
        mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volumePhoto)
        scale.set(70)
        muted = False

    else:   #mute the music
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted =True


playPhoto = PhotoImage(file="images/play.png")   # use to add image
playBtn = Button(middleframe,image=playPhoto,command=play_music)
playBtn.grid(row= 0,column=0,padx=12)

stopPhoto= PhotoImage(file="images/stop.png")
stopBtn = Button(middleframe,image=stopPhoto,command=stop_music)
stopBtn.grid(row= 0,column=2,padx=12)


pausePhoto = PhotoImage(file="images/pause.png")
pauseBtn = Button(middleframe,image=pausePhoto,command=pause_music)
pauseBtn.grid(row= 0,column=4,padx=12)

bottomframe = Frame(root)
bottomframe.pack(padx=30,pady=30)

rewindPhoto = PhotoImage(file="images/rewind.png")
rewindBtn = Button(bottomframe,image=rewindPhoto,command=rewind_music)
rewindBtn.grid(row= 5,column=0)

mutePhoto = PhotoImage(file="images/mute.png")
volumePhoto = PhotoImage(file="images/volume.png")
volumeBtn = Button(bottomframe,image=volumePhoto,command=mute_music)
volumeBtn.grid(row= 5,column=6,pady=15,padx=10)

########################################################################


scale = Scale(bottomframe,from_=0,to=100,orient=HORIZONTAL,command=set_vol)  # this will send string value into val
scale.set(30)
mixer.music.set_volume(0.3)
scale.grid(row=5,column=5,pady=15,padx=15)


statusbar = Label(root,text="Welcome to SoundPlay",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM, fill= X)

root.mainloop()