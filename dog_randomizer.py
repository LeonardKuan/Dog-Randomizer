# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:08:55 2023

@author: Leonard
"""
# This part of the code is to test set up the tkinter window

from tkinter import *
window=Tk()

btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)
lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=150)

window.title('Hello Python')
window.geometry("300x200+10+20")
window.mainloop()

# SO link: https://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search
# This part of the code is the actual dog randomizer
# The current problem is that it's throwing the error "Error loading image: cannot identify image file <_io.BytesIO object at 0x0000025F5E83EEF0>"
# This is potentially due to the fact that image_url spits out https://www.parrot.com/us, which is not an image url

import urllib.request
import json
import io
from tkinter import *
from PIL import ImageTk, Image

# Function to fetch and display the image
def display_image():
    searchTerm = 'parrot'
    startIndex = 0
    searchUrl = "https://www.googleapis.com/customsearch/v1?key=AIzaSyD_iezfuoouyPC7vIU9QfdK6nboZvODsMA&cx=42c297e38eae54568&q=" + searchTerm + "&start=" + str(startIndex)

    with urllib.request.urlopen(searchUrl) as response:
        search_results = json.load(response)

    # Extract the URL of the first image from the search results
    image_url = search_results['items'][0]['link']

    # Test print the image_url for debugging purposes
    print(image_url)

    try:
        # Fetch the image and display it
        image_data = urllib.request.urlopen(image_url).read()
        image = Image.open(io.BytesIO(image_data))

        # Resize the image if needed
        image = image.resize((300, 200), Image.ANTIALIAS)

        # Create a Tkinter window
        window = Tk()

        # Create a Tkinter label to display the image
        img = ImageTk.PhotoImage(image)
        label = Label(window, image=img)
        label.pack()

        # Run the Tkinter event loop
        window.mainloop()
    except IOError as e:
        print("Error loading image:", e)

# Call the function to display the image
display_image()