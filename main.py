import tkinter as tk
import customtkinter as ctk
from tkinter import PhotoImage
from pytube import YouTube
import time
import threading
from pathlib import Path
import os


window = tk.Tk()  
window.geometry("340x560")
window.resizable(False,False)
window.title("Video Downloader And MP3 Converter")

font = ctk.CTkFont()
def start_thread(link,quality_box,frm):
    t = threading.Thread(target=lambda:video_dowmload(link,quality_box,frm))
    t.start()
def start_mp3thread(link,quality_box,frm):
    t = threading.Thread(target=lambda:audio_dowmload(link,quality_box,frm))
    t.start()


def get_quality_thread(link,frm,load):
    
    t = threading.Thread(target=lambda:get_quality(link,frm,load))
    t.start()
def get_mp3quality_thread(link,frm,load):
    t = threading.Thread(target=lambda:get_mp3quality(link,frm,load))
    t.start()

def video_dowmload(link,resv,frm):
    try:
        

        yt = YouTube(link)
        res1 = resv.split(" (")
        val = res1[0]
        value = str(val)
        dwn = ctk.CTkLabel(frm,text="",text_color="black",fg_color="transparent",font=("Helvetica",20))
        dwn.place(x=110,y=270)
    
        pb = ctk.CTkProgressBar(frm,orientation="horizontal",width=300,progress_color="#0c17b2",fg_color="#f0f0f0",mode="indeterminate",border_color="#0c17b2",border_width=2)
        pb.place(x=17,y=300)
        
        
        dwn.configure(text="Downloading.....")
        dwn.update_idletasks()
        pb.start()
        
        vid = yt.streams.filter(resolution=value,progressive=True).first().download(str(os.path.join(Path.home(), 'Downloads')))
        # vid.download()
        time.sleep(0.5)
        dwn.configure(text="Downloaded")
        pb.destroy()
     
    except Exception as e:
        sh = ctk.CTkLabel(frm,text="Something Error !",text_color="Black",fg_color="#e3e3e3",corner_radius=15,font=("Helvetica",20),width=30)
        sh.place(x=80,y=230)
        print(e)
        time.sleep(2.0)
        sh.destroy()
        
def audio_dowmload(link,resv,frm):
    
    try:
        

        yt = YouTube(link)
        res1 = resv.split(" (")
        val = res1[0]
        value = str(val)
        dwn = ctk.CTkLabel(frm,text="",text_color="black",fg_color="transparent",font=("Helvetica",20))
        dwn.place(x=110,y=270)
    
        pb = ctk.CTkProgressBar(frm,orientation="horizontal",width=300,progress_color="#0c17b2",fg_color="#f0f0f0",mode="indeterminate",border_color="#0c17b2",border_width=2)
        pb.place(x=17,y=300)
        
        
        dwn.configure(text="Downloading.....")
        dwn.update_idletasks()
        pb.start()
        
        # yt.streams.filter(only_audio=True,abr=val).first().download(str(os.path.join(Path.home(), 'Downloads')))
        out_file = yt.streams.filter(only_audio=True,abr=value).first().download(output_path = str(os.path.join(Path.home(), 'Downloads')))
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3' 
        os.rename(out_file, new_file)
        time.sleep(0.5)
        dwn.configure(text="Downloaded")
        pb.destroy()
     
    except Exception as e:
        sh = ctk.CTkLabel(frm,text="Something Error !",text_color="Black",fg_color="#e3e3e3",corner_radius=15,font=("Helvetica",20),width=30)
        sh.place(x=80,y=230)
        print(e)
        time.sleep(2.0)
        sh.destroy()
def switch(fr):

    fr.destroy()
    main_page(fr)

def back_page(fr):
    
    fr.destroy()
    main_page()

def main_page(fr):
    fr.destroy()

    main_frame = ctk.CTkFrame(window, width=330,height=560,fg_color="#f0f0f0")

    yt_button = ctk.CTkButton(main_frame,text="Download YouTube Video",width=340, corner_radius=5,height=60,font=("Helvetica",20),fg_color="#753626",text_color="white",hover_color="#9a442f",border_color="#ffedb6",border_width=4,command=lambda:youtube(main_frame))
    yt_button.pack()

    coverter_button = ctk.CTkButton(main_frame,text="YouTube to MP3 Converter",width=340, corner_radius=5,height=60,font=("Helvetica",20),fg_color="#753626",text_color="white",hover_color="#9a442f",border_color="#ffedb6",border_width=4,command=lambda:Converter(main_frame))
    coverter_button.pack(pady=20)

   
    main_frame.pack(pady=20)
    main_frame.pack_propagate(False)
def get_mp3quality(link,frm,load):
    sh = ctk.CTkLabel(frm,text="",text_color="Black",fg_color="#e3e3e3",corner_radius=15,font=("Helvetica",20),width=30)
    sh.place(x=80,y=230)

    if link == "":
            sh.configure(text="Please Enter URL")
            time.sleep(2.0)
            sh.destroy()
            
            
    else :

        try:
            
            
            yt = YouTube(link)
            load.configure(text="Loading.....")
            load.update_idletasks()
            video = yt.streams.filter(only_audio=True)
            q = []
            for i in video :
                qc = i.abr
                mb = yt.streams.filter(only_audio=True,abr=qc).first().filesize_mb
                result = qc +" ("+ str(mb)+"mb)"
                q.append(result)

            
            load.destroy()
            time.sleep(0.05)
            quality_box = ctk.CTkComboBox(frm,border_color="#1221ff",text_color="black",fg_color="#f0f0f0",border_width=2,button_color="#1221ff",dropdown_fg_color="#135ef7",dropdown_hover_color="#1341ff",values=q)
            quality_box.place(x=20,y=115)
            title = ctk.CTkLabel(frm,text=yt.title,text_color="black",wraplength=320,fg_color="#f0f0f0",font=("Helvetica",15,"bold"))
            title.place(x=12,y=160)
            download = ctk.CTkButton(frm,text="Download",width=320, corner_radius=5,height=60,font=("Helvetica",20),border_color="yellow",border_width=2,fg_color="#9a442f",text_color="white",hover_color="#c1593e",command=lambda:start_mp3thread(link,quality_box.get(),frm))
            download.place(x=5,y=380)
        

        except Exception as e:
            
            sh.configure(text="Invalid Link")
            time.sleep(2.0)
            sh.destroy()


def get_quality(link,frm,load):
    sh = ctk.CTkLabel(frm,text="",text_color="Black",fg_color="#e3e3e3",corner_radius=15,font=("Helvetica",20),width=30)
    sh.place(x=80,y=230)

    if link == "":
            sh.configure(text="Please Enter URL")
            time.sleep(2.0)
            sh.destroy()
            
            
    else :

        try:
            
            
            yt = YouTube(link)
            load.configure(text="Loading.....")
            load.update_idletasks()
            resolution =[int(i.split("p")[0]) for i in (list(dict.fromkeys([i.resolution for i in yt.streams.filter(progressive=True) if i.resolution])))]
            
            q = []
            for i in resolution:
                
                yt2 = yt.streams.filter(res=str(i)+"p",progressive=True).first().filesize_mb
                i = str(i)+"p ("+str(yt2)+"mb)"
                q.append(i)

            load.destroy()
            time.sleep(0.05)
            quality_box = ctk.CTkComboBox(frm,border_color="#1221ff",text_color="black",fg_color="#f0f0f0",border_width=2,button_color="#1221ff",dropdown_fg_color="#135ef7",dropdown_hover_color="#1341ff",values=q)
            quality_box.place(x=20,y=115)
            title = ctk.CTkLabel(frm,text=yt.title,text_color="black",wraplength=320,fg_color="#f0f0f0",font=("Helvetica",15,"bold"))
            title.place(x=12,y=160)
            download = ctk.CTkButton(frm,text="Download",width=320, corner_radius=5,height=60,font=("Helvetica",20),border_color="yellow",border_width=2,fg_color="#9a442f",text_color="white",hover_color="#c1593e",command=lambda:start_thread(link,quality_box.get(),frm))
            download.place(x=5,y=380)
        

        except Exception as e:
            
            sh.configure(text="Invalid Link")
            time.sleep(2.0)
            sh.destroy()

def youtube(fr):
    fr.destroy()
    f = ctk.CTkFrame(window,fg_color="#f0f0f0", width=330,height=550)
    l13 = ctk.CTkLabel(f,text="Download Youtube Videos",font=("Lucida Calligraphy",20),text_color="#1221ff",fg_color="#f0f0f0",width=20)
    l13.pack()

    url_entry = ctk.CTkEntry(f,fg_color="#f0f0f0",placeholder_text="Enter video url",placeholder_text_color="#3f84f7",font=("Helvetica",20,"italic"),text_color="#3f84f7",width=320 ,corner_radius=5,height=60,border_color="#1221ff")
    url_entry.pack(pady=20)
    url_entry.focus_set()
    load = ctk.CTkLabel(f,text="",fg_color="transparent",font=("Helvetica",20),text_color="black")
    load.place(x=130,y=180)
    
    

    get_quality_button = ctk.CTkButton(f,text="Get Quality",width=130, corner_radius=5,height=30,font=("Helvetica",15),fg_color="#753626",text_color="white",hover_color="#c1593e",command=lambda:get_quality_thread(url_entry.get(),f,load))
    get_quality_button.place(x=180,y=115)
    

    back = ctk.CTkButton(f,text="BACK",width=320, corner_radius=5,height=60,font=("Helvetica",20),command=lambda:main_page(f))
    back.place(x=5,y=450)


    f.pack(pady=20)
    f.pack_propagate(False)
   


def Converter(fr):
    fr.destroy()
    f = ctk.CTkFrame(window,fg_color="#f0f0f0", width=330,height=550)
    l13 = ctk.CTkLabel(f,text="Youtube To MP3",font=("Lucida Calligraphy",20),text_color="#1221ff",fg_color="#f0f0f0",width=20)
    l13.pack()

    url_entry = ctk.CTkEntry(f,fg_color="#f0f0f0",placeholder_text="Enter video url",placeholder_text_color="#3f84f7",font=("Helvetica",20,"italic"),text_color="#3f84f7",width=320 ,corner_radius=5,height=60,border_color="#1221ff")
    url_entry.pack(pady=20)
    url_entry.focus_set()
    load = ctk.CTkLabel(f,text="",fg_color="transparent",font=("Helvetica",20),text_color="black")
    load.place(x=130,y=180)
    
    

    get_quality_button = ctk.CTkButton(f,text="Get Quality",width=130, corner_radius=5,height=30,font=("Helvetica",15),fg_color="#753626",text_color="white",hover_color="#c1593e",command=lambda:get_mp3quality_thread(url_entry.get(),f,load))
    get_quality_button.place(x=180,y=115)
    

    back = ctk.CTkButton(f,text="BACK",width=320, corner_radius=5,height=60,font=("Helvetica",20),command=lambda:main_page(f))
    back.place(x=5,y=450)


    f.pack(pady=20)
    f.pack_propagate(False)

def land():
    landing_frame = ctk.CTkFrame(window,fg_color="#f0f0f0", width=340,height=560)
    f1 = ctk.CTkFrame(landing_frame,fg_color="#f0f0f0")
    l1 = ctk.CTkLabel(f1,text="Created by",font=("lucida Calligraphy",30),text_color="Blue",fg_color="#f0f0f0")
    l1.pack()
    f1.place(x=40,y=160)

    f2 = ctk.CTkFrame(landing_frame,fg_color="#f0f0f0")
    l2 = ctk.CTkLabel(f2,text="Tejas Tikkas",font=("lucida Calligraphy",30,'bold'),text_color="Blue",fg_color="#f0f0f0")
    l2.pack()
    f2.place(x=80,y=200)

    f3 = ctk.CTkFrame(landing_frame,fg_color="#f0f0f0")
    b1 = ctk.CTkButton(f3,text="Start",font=("Helvetica",30),corner_radius=30,fg_color="#4766ff",border_width=2,border_color="#e9d700",hover_color="#fc6c95",command=lambda:switch(landing_frame))
    b1.pack(ipady=5,ipadx=5)
    f3.pack(side="bottom",pady=200)

    landing_frame.pack()
    landing_frame.pack_propagate(False)

land()
window.mainloop()
