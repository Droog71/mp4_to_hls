import os
import sys
import tkinter as tk
import ffmpeg
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# converts a file
def convert_file(filename):
    if filename != None and filename != "":
        if (filename.endswith(".mp4")):
            ffmpeg.input(filename).output(filename[:-4] + '.m3u8', format='hls', start_number=0, hls_time=10, hls_list_size=0).run()

# converts all files in the directory
def convert_dir(directory):
    if directory != None and directory != "":
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                if (filename.endswith(".mp4")):
                    ffmpeg.input(f).output(f[:-4] + '.m3u8', format='hls', start_number=0, hls_time=10, hls_list_size=0).run()
                else:
                    continue
            else:
                continue

# file explorer window
def browse_files():
    filename = filedialog.askopenfilename(
        initialdir = os.getcwd(),
        title = "Select a File",
        filetypes = (("mp4","*.mp4*"),("all files","*.*"))
    )    
    convert_file(filename)     
            
# directory explorer window
def browse_dirs():
    directory = filedialog.askdirectory()
    convert_dir(directory)
		
# exits the program
def exit():
	sys.exit()
   
# main program
def init():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-f":
            convert_file(sys.argv[2])
        elif sys.argv[1] == "-d":
            convert_dir(sys.argv[2])
    else:
        window = Tk()
        window.title('mp4 to hls') 
        window.geometry("300x150")  
        window.config(background = "gray")
        
        explore_files_border = LabelFrame(window, bd = 4, bg = "black")
        explore_files_border.pack(pady = 8)
        
        explore_dirs_border = LabelFrame(window, bd = 4, bg = "black")
        explore_dirs_border.pack(pady = 8)
        
        exit_border = LabelFrame(window, bd = 4, bg = "black")
        exit_border.pack(pady = 8)
        
        button_explore_files = Button(explore_files_border,text = "Select File", fg='black', bg='gray', command = browse_files)
        button_explore_dirs = Button(explore_dirs_border,text = "Select Directory", fg='black', bg='gray', command = browse_dirs)
        button_exit = Button(exit_border,text = "Exit", fg='black', bg='gray', command = exit) 
        
        button_explore_files.pack()
        button_explore_dirs.pack()
        button_exit.pack()
        
        window.mainloop()
    
# starts the program. 
if __name__ == "__main__":
    init()
