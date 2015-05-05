#Music Information

#Problem
Find a better way to search for music information.

#Question
1. Can the information be shown in a GUI?
2. Can information be displayed separately based on user preference?
3. Can a user who has never used the program able to utilize it?

#Resources
1. [Pyechonest]
2. [Check for '-' between artist and song title]
3. [Split string at '-']
4. [Replace + for ' ' in search]
5. [More API method calls]
6. [Global Variables]
7. [Tkinter]

###Abstract
The image is added to the GUI frame using ImageTk.
```python
root = Tk()
img = ImageTk.PhotoImage(Image.open('nest.png'))
root.geometry('550x350')
panel = Label(root, image = img)
panel.pack(side = 'bottom', fill = 'both', expand = 'yes')
```

The instruction pane is created using Message.
```python
text2 = Message(root, width = 200, text = 'Please enter a search in the text box ...’)
text2.pack(side = LEFT)
```

The text box is created using Entry.
```python
text = Entry()
text.pack()
text.delete(0, END)
text.insert(0, 'Search_Words')
text.config(width = 100) 
```

[Pyechonest]: https://github.com/echonest/pyechonest
[Check for '-' between artist and song title]: http://stackoverflow.com/questions/4877844/how-would-i-check-a-string-for-a-certain-letter-in-python
[Split string at '-']: http://www.tutorialspoint.com/python/string_split.htm
[Replace + for ' ' in search]: http://stackoverflow.com/questions/3136689/find-and-replace-string-values-in-python-list
[More API method calls]: http://developer.echonest.com/docs/v4
[Global Variables]: http://stackoverflow.com/questions/10588317/python-function-global-variables
[Tkinter]: http://effbot.org/tkinterbook/
