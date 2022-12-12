# importing packages

from pytube import YouTube
import os
import PySimpleGUI as sg


# Define the window's contents
layout = [[sg.Text("Paste YouTube Video url to download:")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
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
        destination = '.'
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        window["-OUTPUT-"].update(yt.title + " has been successfully downloaded.", text_color = "yellow")
   

# Finish up by removing from the screen
window.close()



