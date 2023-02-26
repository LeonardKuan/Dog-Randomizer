# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:08:55 2023

@author: Leonard
"""

from tkinter import *
window=Tk()
# add widgets here

btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)
lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=150)

window.title('Hello Python')
window.geometry("300x200+10+20")
window.mainloop()

import urllib2
import simplejson
import cStringIO

#SO link: https://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search
#The problem here is that can't pip install anything due to pip install -h index address showing bloomberg link, need to investigate further

fetcher = urllib2.build_opener()
searchTerm = 'parrot'
startIndex = 0
searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + startIndex
f = fetcher.open(searchUrl)
deserialized_output = simplejson.load(f)