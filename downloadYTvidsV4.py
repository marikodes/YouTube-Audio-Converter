##CREDITS
# YouTube vid downloading code from Geeks for Geeks: https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/

#PySimpleGUI Framework (example 2): https://pypi.org/project/PySimpleGUI/

# importing packages
from pytube import YouTube
import os
import PySimpleGUI as sg


# Define the window's contents
layout = [[sg.Text("Choose directory where audio will be downloaded:"), sg.FolderBrowse(size=(10, 1), key='-USER FOLDER-')],
          [sg.Text("Choose audio format:"), sg.Combo(["MP3","WAV"], key='-DROPDOWN-', size=(10, 1))],
          [sg.Text("Paste YouTube Video url to download:")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,2), key='-OUTPUT-')],
          [sg.Button("Download")],
          [sg.Button('Quit')]]

# Create the window
window = sg.Window('YouTube Audio Converter', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == "Download":
        yt = YouTube(
	str(values['-INPUT-']))
        video = yt.streams.filter(only_audio=True).first()
        debug_directory = values['-USER FOLDER-']
        print(debug_directory)  #its still going to downloads by default, I want users to be able to decide where the file is downloading
        destination = str(values['-USER FOLDER-'])#this might fix the problem -- it did yay!
        #path = destination + yt.title
        # if os.path.isfile(path) == True:
        #     window["-OUTPUT-"].update(yt.title + " already exists in this directory", text_color = "red")
        # else:
        #     out_file = video.download(output_path=destination)
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        debug_path = os.path.abspath(out_file)
        print(debug_path)
        if values['-DROPDOWN-'] == "MP3": #this conditional statement is working
            new_file = base + '.mp3'
        elif values['-DROPDOWN-'] == "WAV":#this conditional statement is working
            new_file = base + '.wav'
        #if os.path.isfile(out_file) == True: #***this is not working, but the program is not throwing the exception anymore *shrugs shoulders*
            #i also tried isfile which also didn't work
            #window["-OUTPUT-"].update(yt.title + " already exists in this directory", text_color = "red")
        try:
            os.rename(out_file, new_file) 
            window["-OUTPUT-"].update(yt.title + " has been successfully downloaded.", text_color = "yellow")
        except FileExistsError:
            window["-OUTPUT-"].update(yt.title + " already exists in this directory", text_color = "red")
   

# Finish up by removing from the screen
window.close()


#12/12/22 - what i still need to do
#need to have different pathways based on the file format chosen
#need to print a statement to the window to tell the user if they already have a file that exists with that name in the chosen directory
#need to figure out how to get the users chosen directory and use that when they download a vid


#notes/things to fix
#don't forget commas when adding new layout elements (you will get this error >>>TypeError: list indices must be integers or slices, not Text)


#12/13/22 
#okay so I added the different download options and that is working, but I am still dealing with the file exists error
#it is completely skipping over the conditional statement checking that the file exists, so it only downloads in mp4 audio

#12/16/22
#so it turns out that the win error 183 can be solved with try/except statement (never heard of this kind of statement before, the more you know!) 
#that is the last major issue I have run into(for now...)
