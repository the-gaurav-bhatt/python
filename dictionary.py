import tkinter as tk
import speech_recognition as sr
import pyttsx3
from PyDictionary import PyDictionary

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Selecting a female voice

# Initialize PyDictionary
dictionary = PyDictionary()


# Function to update the label with text
def update_label(label, message):
    label.config(text=message)
    engine.say(message)  # Speak the message
    engine.runAndWait()


# Function to recognize and find the meaning
def recognize_and_find_meaning():
    try:
        # Reading Microphone as source
        with sr.Microphone() as source:
            update_label(status_label, "Adjusting for ambient noise...")
            root.update()
            r.adjust_for_ambient_noise(source)
            update_label(status_label, "Listening... (Speak now)")
            root.update()

            # Read the audio data from the default microphone
            audio_data = r.record(source, duration=4)

        update_label(status_label, "Recognizing...")
        root.update()
        # Convert the audio to text
        text = r.recognize_google(audio_data)
        update_label(recognized_word_label, "Recognized Word: " + text)
        root.update()

        # Check the meaning of the word
        meanings = dictionary.meaning(text)
        if meanings:
            message = "I found many meanings of the word " + text + ". One of the meanings is " + meanings['Noun'][0]
            update_label(recognized_word_label, message)
            root.update()
        else:
            message = "Could not find the meaning of " + text
            update_label(recognized_word_label, message)
            root.update()


    except sr.UnknownValueError:
        update_label(status_label, "Speech Recognition could not understand audio")
        root.update()
        tk.messagebox.showinfo("Error", "I'm sorry, I couldn't understand what you said.")

    except sr.RequestError as e:
        update_label(status_label, "Could not request results from Speech Recognition service")
        root.update()
        tk.messagebox.showinfo("Error", "I'm sorry, the speech recognition service failed. Please, try again later.")

    except Exception as e:
        update_label(status_label, "An error occurred: " + str(e))
        root.update()
        tk.messagebox.showinfo("Error", "An error occurred: " + str(e))


# Create the main application window
root = tk.Tk()
root.title("Word Meaning Finder")
root.geometry("500x400")

# Styling the window background
root.config(bg="#f2f2f2")

# Title label
title_label = tk.Label(root, text="Word Meaning Finder", font=("Helvetica", 20), bg="#f2f2f2")
title_label.pack(pady=10)

# Recognized word label
recognized_word_label = tk.Label(root, text="Recognized Word: ", font=("Helvetica", 12), bg="#f2f2f2")
recognized_word_label.pack(pady=10)

# Status label
status_label = tk.Label(root, text="Press the 'Start Listening' button and speak to find the meaning.",
                        font=("Helvetica", 12), bg="#f2f2f2")
status_label.pack(pady=10)

# Start Listening button
listen_button = tk.Button(root, text="Start Listening", font=("Helvetica", 14), command=recognize_and_find_meaning,
                          bg="#4CAF50", fg="white")
listen_button.pack(pady=20)

# Exit button
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 14), command=root.quit, bg="#f44336", fg="white")
exit_button.pack(pady=10)

# Start the main event loop
root.mainloop()
