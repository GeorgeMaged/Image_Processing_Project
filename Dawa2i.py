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

