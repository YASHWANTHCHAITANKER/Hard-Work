# Import necessary packages
from gtts import gTTS, lang
import os
from tkinter import *
from tkinter import messagebox
import speech_recognition as sr

# Define functions

# Text to speech conversion
def text_to_speech():
    # Read inputs given by user
    text = text_entry.get("1.0","end-1c")
    language = accent_entry.get()
    # Check if the user submitted inputs
    if len(text.strip()) == 0:
        messagebox.showerror(message="Enter text to convert to speech")
        return
    if len(language.strip()) == 0:
        messagebox.showerror(message="Enter language code")
        return
    # Check if the language code is valid
    if language not in lang.tts_langs():
        messagebox.showerror(message="Language not supported: " + language)
        return
    # Using the inputs, convert the text to speech
    try:
        speech = gTTS(text=text, lang=language, slow=False)
        # Save the speech to an MP3 file
        speech.save("text.mp3")
        # Play the file using mpg123 in Linux and start in Windows
        os.system("start text.mp3")
    except Exception as e:
        messagebox.showerror(message="Error occurred: " + str(e))

# List the supported languages and their keys
def list_languages():
    # Access languages and access codes using lang.tts_langs()
    languages = list(lang.tts_langs().keys())
    messagebox.showinfo(message="Supported languages:\n" + ", ".join(languages))

# Python speech to text conversion
def speech_to_text(): 
    # Initialise the recognizer class
    recorder = sr.Recognizer()
    try:
        duration = int(duration_entry.get())
    except ValueError:
        messagebox.showerror(message="Enter a valid duration")
        return
    # Use the microphone
    messagebox.showinfo(message="Speak into the microphone and wait after finishing the recording")  
    with sr.Microphone() as mic: 
        # Record audio from the user
        recorder.adjust_for_ambient_noise(mic)
        audio_input = recorder.listen(mic, timeout=duration)   
        try:                        
            # Convert to text
            text_output = recorder.recognize_google(audio_input)
            # Display the output
            messagebox.showinfo(message="You said:\n" + text_output)       
        except sr.UnknownValueError:
            messagebox.showerror(message="Could not understand audio")
        except sr.RequestError:
            messagebox.showerror(message="Google Speech Recognition service unavailable")

# Create a window
window = Tk()
# Set dimensions of window and title
window.geometry("500x300")
window.title("Convert Speech to Text and Text to Speech: PythonGeeks")
title_label = Label(window, text="Convert Speech to Text and Text to Speech: PythonGeeks").pack()

# Read inputs

# Text to speech input
text_label = Label(window, text="Text:").place(x=10, y=20)
text_entry = Text(window, width=30, height=5)
text_entry.place(x=80, y=20)

# Accent input
accent_label = Label(window, text="Accent:").place(x=10, y=110)
accent_entry = Entry(window, width=26)
accent_entry.place(x=80, y=110)

# Duration input
duration_label = Label(window, text="Duration:").place(x=10, y=140)
duration_entry = Entry(window, width=26)
duration_entry.place(x=80, y=140)

# Perform the functions
button1 = Button(window, text='List languages', bg='Turquoise', fg='Red', command=list_languages).place(x=10, y=190)
button2 = Button(window, text='Convert Text to Speech', bg='Turquoise', fg='Red', command=text_to_speech).place(x=130, y=190)
button3 = Button(window, text='Convert Speech to Text', bg='Turquoise', fg='Red', command=speech_to_text).place(x=305, y=190)

# Close the app
window.mainloop()
