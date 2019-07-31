import tkinter as tk
from pytube import YouTube

def videolink():
    url = input("Enter URL :")
    y1 = YouTube(url)
    title = y1.title
    #thumbnail = y1.thumbnail_url
    alltype = y1.streams.all()
    for i in alltype:
        print(i)




"""import tkinter as tk
from pytube import YouTube

def downloadVid():
    global e1
    string = e1.get()
    yt = YouTube(str(string))
    videos = yt.get_videos()

    s=1
    for v in videos:
        print(str(s) +'.'+str(v))
        s += 1

    n = int(input("Enter your choice"))
    vid = videos[n-1]
    destination = str(input("Enter your destination :"))
    vid.download(destination)
    print(yt.filename +'\n has been downloaded')
    
       
root = tk.Tk()

w = tk.Label(root,text = "youtube Download")
w.pack()

e1 = tk.Entry(root,bd=5)
e1.pack(side=tk.TOP)

button = tk.Button(root,text="Download",fg="red",command=downloadVid)
button.pack(side=tk.BOTTOM)

root.mainloop()
"""
