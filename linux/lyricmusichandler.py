#pro-tips pack accepts arguments for position, tkinter.quit or root.quit quits, element.destroy destroys element
import sys
import subprocess
import Tkinter
from Tkinter import *
bol = True
mvar = 1
urls = []
index = 1
def YDL(into):
    p = subprocess.Popen(r'ffmpeg\bin\youtube-dl.exe --extract-audio --no-check-certificate --audio-format mp3 '+into+' -k',shell= True)
    p.wait()
    print 'finished download'
def SDL(into):
    p = subprocess.Popen(r'ffmpeg\bin\youtube-dl.exe --verbose --no-check-certificate '+into,shell= True)
    p.wait()
    print 'finished download'
def Ypop():
    y = Tkinter.Tk(); yframe = Frame(y, width=250, height=250,bg='red'); yframe.pack(); y.wm_title("LyricMusicHandler")
    def empty(event):
        e.delete(0, END)
    def handler():
        global bol, mvar, index, urls
        if(bol):
            mvar = int(e.get())
            bol = False
            empty(0)
            e.insert(0,"Enter url 1 of "+str(mvar)+".")
        elif(not bol):
            urls.insert(index, e.get())
            if(index == mvar):
                for num in range(0,mvar):
                    YDL(urls[num])
                bol = True;mvar = 1;urls = [];index = 1
                y.destroy()
            else:
                index += 1 
                empty(0)
                e.insert(0,"Enter url "+str(index)+" of "+str(mvar)+".")
    e = Entry(yframe); e.insert(0,"Enter the number of urls."); e.place(relx=0.5, rely=0.5, anchor=CENTER); e.bind('<Button-1>', empty)
    b = Button(yframe, text="Submit", command=handler); b.place(relx=1, rely=0.5, anchor = E)

def Spop():
    s = Tkinter.Tk(); sframe = Frame(s, width=250, height=250,bg='red'); sframe.pack(); s.wm_title("LyricMusicHandler")
    def empty(event):
      e.delete(0, END)    
    def handler():
        url = e.get()
        SDL(url)
        s.destroy()
    e = Entry(sframe); e.insert(0,"Enter your url."); e.place(relx=0.5, rely=0.5, anchor=CENTER); e.bind('<Button-1>', empty)
    b = Button(sframe, text="Submit", command=handler); b.place(relx=1, rely=0.5, anchor = E)
root = Tkinter.Tk()
root.wm_title("LyricMusicHandler")
frame = Frame(root, width=250, height=250, bg='red')
frame.pack_propagate(0)
frame.pack()
exp = Label(frame,text="This is a GUI test application for Youtube-DL.")
exp.place(relx=0.5, rely=0.4, anchor=CENTER)
ydl = Button(frame, text='Youtube-DL', command=Ypop)
ydl.place(relx=0.01,rely=0.5)
sdl = Button(frame, text='SoundCloud-DL', command=Spop)
sdl.place(relx=0.6,rely=0.5)
root.mainloop()
