#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import imageio
import pytesseract
from tkinter import *
from gtts import gTTS
import os
from PIL import Image, ImageTk
from tkinter import filedialog
import sqlite3
from tkinter.ttk import *

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# The following piece of code is executed only once to create the table
# The database contains one table that consists of two attributes the first is the name of the drug and the second is
# the times at which the drug should be taken in string form
'''
# DATABASE
# Create database and connect to it
conn = sqlite3.connect('Medicine_DB')

# Create cursor
c = conn.cursor()
# Create table.
c.execute("""CREATE TABLE Medicine (
Name text,
Times text
)
""")
'''

# Main Window
root = Tk()
root.title("Dawa2i")
root.geometry("900x700")

# Styling Buttons
style = Style()
style.configure('TButton', font=
('calibri', 10, 'bold',),
                foreground='red')


# Function to convert input string or text into speech
def play_audio(output):
    language = 'en'
    my_object = gTTS(text=output, lang=language, slow=False)
    my_object.save("welcome.mp3")
    os.system("start welcome.mp3")


# Function to extract text from image
def extract_text():

    # Extract all the text from the image
    extracted_text = pytesseract.image_to_string(image)

    # Convert the text into list
    list_extracted_text = extracted_text.split()
    # print(list_extracted_text)

    # Connect to the database
    conn = sqlite3.connect('Medicine_DB')

    # Create cursor
    c = conn.cursor()

    # Fetch all the records saved in the database
    c.execute("SELECT * FROM Medicine ")
    records = c.fetchall()
    # print(records)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    # Check if name of medicine matches any medicine name in the database
    # If yes it passes its name as well as the times it should be taken to the function play_audio
    # If not an audio is played that says drug not found and opens a window to add it to the database
    names = []
    times = []
    global to_speak
    to_speak = ''
    for record in records:
        names.append(record[0])
        times.append(record)
    # print(names)
    global flag
    flag = 0
    for element in list_extracted_text:
        for one_name in names:
            if element == one_name:
                flag = 1
                to_speak += element
                for record in records:
                    if record[0] == element:
                        to_speak += record[1]

    # If the drug is found in the database
    if flag == 1:
        print(to_speak)
        play_audio(to_speak)
        flag = 0
    # If the drug is not found in the database
    elif flag == 0:
        to_speak = "Drug Name Not Found Please Select Add New Drug"
        play_audio(to_speak)
        open_new_drug_window()

