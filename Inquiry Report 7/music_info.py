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
from Tkinter import *
from PIL import ImageTk, Image
import os

global bio, blog, songType, hot
bio = False
blog = False
songType = False
hot = False


def main(search_words):
    root = Tk()
    img = ImageTk.PhotoImage(Image.open('nest.png'))
    root.geometry('550x350')
    panel = Label(root, image = img)
    panel.pack(side = 'bottom', fill = 'both', expand = 'yes')

    text2 = Message(root, width = 200, text='Please enter a search in the text box to the right in either of the following formats:\n\nartist name\nartist name - song title\n\nYou can also use the artist and song buttons to choose if you would like to see any of those options. All of the options are turned off by default.')
    text2.pack(side = LEFT)

    text = Entry()
    text.pack()
    text.delete(0, END)
    text.insert(0, 'Search_Words')
    text.config(width = 100)

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
        print 'Song Name: ', new_song
    else:
        results = song.search(title=search_words)
        print results[1]
        a_results = artist.search(name=search_words)
        print a_results
    x = 0
    try:
        for x in range(0, 5):
            if x == 1:
                print '-----Other Possible Artists-----'
                print
            print 'Result', x+1
            search_item = results[x]
            print 'Song: ', search_item
            a_search_item = a_results[x]
            print 'Artist Name: ', a_search_item.name
            print 'Artist Location:', search_item.artist_location
            print 'Danceability:', search_item.audio_summary['danceability']
            print 'Tempo:', search_item.audio_summary['tempo']
            print 'Loudness:', search_item.audio_summary['loudness']
            print 'Duration:', search_item.audio_summary['duration']
            print 'Artist Hotness:', a_search_item.hotttnesss
            print
            if x == 0:
                a_search_item = a_results[x]
                search_item = results[x]
                if bio == True:
                    print 'Biography:'
                    print a_search_item.biographies[0]
                    print
                else:
                    print
                if blog == True:
                    print 'Blog:'
                    print a_search_item.blogs[0]
                    print
                else:
                    print
                if songType == True:
                    print 'Song Type:'
                    print search_item.song_type
                    print
                if hot == True:
                    print 'Hotness:'
                    print search_item.song_hotttnesss
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

def bioChoice():
    global bio
    bio = not bio
    print 'Biography: '
    print bio

def blogChoice():
    global blog
    blog = not blog
    print 'Blog:'
    print blog

def songTypeChoice():
    global songType
    songType = not songType
    print 'Song Type:'
    print songType

def hotChoice():
    global hot
    hot = not hot
    print 'Track Info:'
    print hot

class Music(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='#24A9E4')
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Music Info')
        continueButton = Button(self, text='Search', command = self.quit)
        continueButton.config(height = 3, width = 10)
        continueButton.place(x = 240, y = 60)
        artistLabel = Label(self, text = 'Artist Options', bg = 'red')
        artistLabel.place(x = 0, y = 0)
        songLabel = Label(self, text = 'Song Options', bg = 'red')
        songLabel.place(x = 120, y = 0)
        bioButton = Button(self, text = 'Biography?', command = bioChoice)
        bioButton.config(height = 3, width = 10)
        bioButton.place(x = 0, y = 30)
        blogButton = Button(self, text = 'Blogs?', command = blogChoice)
        blogButton.config(height = 3, width = 10)
        blogButton.place(x = 0, y = 90)
        songTypeButton = Button(self, text = 'Song Type?', command = songTypeChoice)
        songTypeButton.config(height = 3, width = 10)
        songTypeButton.place(x = 120, y = 30)
        hotButton = Button(self, text = 'Hotness?', command = hotChoice)
        hotButton.config(height = 3, width = 10)
        hotButton.place(x = 120, y = 90)
        self.pack(fill=BOTH, expand=1)

if  __name__ == '__main__':
    import sys
    search_words = ''
    try:
        main(search_words)
    except:
        print usage
        sys.exit(-1)
