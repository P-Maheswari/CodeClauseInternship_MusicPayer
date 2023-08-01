import os
import pygame
import tkinter as tk
from tkinter import filedialog

def browsing_files():
    global music_file
    music_file = filedialog.askopenfilename(defaultextension=" .mp3",filetypes=[("MP3 Files","*.mp3")])
    update_song_title()
def playing_Music():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        playing_status_label.config(text="Music status : playing")
        is_paused = False
    else:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        playing_status_label.config(text="Music status : playing")
def pause_music():
    global is_paused
    if pygame.mixer.music.get_busy() and not is_paused:
        pygame.mixer.music.pause()
        playing_status_label.config(text="Music status : paused")
        is_paused = True
def resume_music():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        playing_status_label.config(text="Music status : Playing")
        is_paused = False
def stop_music():
    global is_paused
    pygame.mixer.music.stop()
    playing_status_label.config(text="Music status : Stopped")
    is_paused = False
def update_song_title():
    song_name = os.path.basename(music_file)
    song_label.config(text=f"{song_name}")
    song_label.update_idletasks()
    frame_width = song_label.winfo_width()
    frame.config(width=frame_width)
def exit_music_player():
    app.destroy()
pygame.init()

#creating the application window
app = tk.Tk()
app.title("Music Player!")
app.configure(bg="lightblue")

#setting the dimensions for application window
app.geometry("550x450")

#button for browsing music files
btn_browse = tk.Button(app,text="search🔎",command=browsing_files)
#button for playing the selected music
btn_play = tk.Button(app,text="Play",command=playing_Music)
#button for pausing music
btn_pause = tk.Button(app,text="Pause",command=pause_music)
#button for resuming music
btn_resume = tk.Button(app,text="Resume",command=resume_music)
#button for stop music
btn_stop = tk.Button(app,text="stop",command=stop_music)
#button for exiting frm the window
btn_exit = tk.Button(app,text="Exit",command=exit_music_player)

btn_browse.pack(pady=25)

#creating a frame
frame = tk.Frame(app,width=500,height=300)
frame.pack()

#creating a label to display the selected song
song_label = tk.Label(frame,text="Selected Song: None",bg="#003366",fg="white",font=("Comic Sans MS",15,"underline"))
song_label.pack(side=tk.TOP)

#creating a label to display the playing status
playing_status_label = tk.Label(frame,text="MUSIC STATUS:None",bg="#003366",fg="white",font=("Verdana",10))
playing_status_label.pack(side=tk.TOP)

#arranging buttons in the window
btn_play.pack(pady=15)
btn_pause.pack(pady=15)
btn_resume.pack(pady=15)
btn_stop.pack(pady=15)
btn_exit.pack(pady=15)

is_paused = False

#main loop
app.mainloop()


