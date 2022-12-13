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
        #print(values['-USER FOLDER-'])  #its still going to downloads by default, I want users to be able to decide where the file is downloading
        destination = str(values['-USER FOLDER-'])
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        window["-OUTPUT-"].update(yt.title + " has been successfully downloaded.", text_color = "yellow")
   

# Finish up by removing from the screen
window.close()


#12/12 - what i still need to do
#need to have different pathways based on the file format chosen
#need to print a statement to the window to tell the user if they already have a file that exists with that name in the chosen directory
#need to figure out how to get the users chosen directory and use that when they 


#notes/things to fix
#don't forget commas when adding new layout elements (you will get this error >>>TypeError: list indices must be integers or slices, not Text)
