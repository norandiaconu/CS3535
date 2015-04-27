#!/usr/bin/env python
# encoding: utf=8
"""
music_info.py

Search for information on a song or artist.

By Noran Diaconu, 2015-04-27.
"""

usage = """
Usage: 
    python music_info.py

Example (in GUI):
    pink floyd
    pink floyd - money
"""

from pyechonest import song, artist
#from Tkinter import Tk, Frame, BOTH, Button, Text, Entry
from Tkinter import *
from PIL import ImageTk, Image
import os

def main(search_words):

    root = Tk()
    img = ImageTk.PhotoImage(Image.open('nest.png'))
    root.geometry('600x250')
    panel = Label(root, image = img)
    panel.pack(side = 'bottom', fill = 'both', expand = 'yes')

    text1 = Text(root, height = 6, width = 44)
    text1.insert(END, 'Please enter a search in the text box to theright in either of the following formats:\n\nartist name\nartist name - song title', 'a')
    text1.pack(side = LEFT)

    text = Entry()
    text.pack()
    text.delete(0, END)
    text.insert(0, 'Search_Words')

    app = Music(root)
    root.mainloop()

    search_words = text.get()

    print search_words
    if '-' in search_words:
        lis = search_words.split('-')
        a_results = artist.search(name=lis[0])
        replaced = [l.replace('+', ' ') for l in lis[1]]
        new_song = ''
        new_song = ''.join(replaced)
        new_combined = lis[0] + new_song
        results = song.search(combined=new_combined)
        print 'song name: ', new_song
    else:
        results = song.search(title=search_words)
        print results[1]
        a_results = artist.search(name=search_words)
        print a_results
    x = 0
    try:
        for x in range(0, 5):
            print 'Result', x+1
            search_item = results[x]
            print 'Song: ', search_item
            a_search_item = a_results[x]
            print 'artist name: ', a_search_item.name
            print 'artist location:', search_item.artist_location
            print 'danceability:', search_item.audio_summary['danceability']
            print 'tempo:', search_item.audio_summary['tempo']
            print 'loudness:', search_item.audio_summary['loudness']
            print 'duration:', search_item.audio_summary['duration']
            if x == 0:
                bio = raw_input('Would you like to see biography information for this artist (y/n): ')
                print bio
                if 'y' in bio:
                    a_search_item = a_results[x]
                    print a_search_item.biographies[1]
                else:
                    print
            x += 1
            try:
                search_item = results[x]
                a_search_item = a_results[x]
            except IndexError:
                print 'Search complete!'
                break
            print

    except IndexError:
        print 'Search complete!'

def choiceY():
    print 'y'

def choiceN():
    print 'n'

class Music(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='#24A9E4')
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Music Info')
        continueButton = Button(self, text='Search', command = self.quit)
        continueButton.config(height = 3, width = 10)
        continueButton.place(x = 240, y = 0)
        yesButton = Button(self, text = 'Yes', command = choiceY)
        yesButton.config(height = 3, width = 10)
        yesButton.place(x = 0, y = 0)
        noButton = Button(self, text = 'No', command = choiceN)
        noButton.config(height = 3, width = 10)
        noButton.place(x = 100, y = 0)
        self.pack(fill=BOTH, expand=1)

def func(event):
    print 'returned'

if  __name__ == '__main__':
    import sys
    search_words = ''
    try:
        main(search_words)
    except:
        print usage
        sys.exit(-1)
