from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from threading import *

root = Tk()
root.title("Application de download des videos en youtube")
root.geometry("600x320")
root.resizable(False,False)

def choisir():
    repertoire= filedialog.askdirectory()
    liendossier.delete(0, "end")
    liendossier.insert(0, repertoire)

def download():
    statut.config(text="En Téléchargement.....")
    lien = lienvideo.get()
    dossier_down = liendossier.get()
    YouTube(lien,on_complete_callback=fin).streams.filter(progressive=True,file_extension="mp4").order_by("resolution").desc().first().download(dossier_down)

def fin(stream=None,chunk=None,file_handle=None,remaining=None):
    statut.config(text="Completer")

logo_image = Label(root,text="You Tube Downloader").place(relx=0.5,rely=0.25 ,anchor="center")


label1= Label(root,text="Entrer le lien youtube :").place(x=25,y=150)
lienvideo = Entry(root,width=60)
lienvideo.place(x=160,y=150)


dossier= Label(root,text="Le Dossier de download :").place(x=25,y=183)
liendossier = Entry(root,width=45)
liendossier.place(x=160,y=183)

choisir = Button(root,text="Choisir ",command=choisir ).place(x=455,y=180)



download = Button(root,text="Download", command=Thread(target=(download)).start).place(x=280,y=220)

statut = Label(root, text="Prêt" ,fg="black",bg="white",anchor="w")
statut.place(rely=1,anchor="sw",relwidth=1 )


root.mainloop()