#Inquiry Report 4
Music Information

#Problem
Find a better way to search for music information.

#Question
1. Can the information be shown in a more useful way?
2. Can an artist and song be searched at the same time without knowing the Echonest API?
3. Can multiple suggestions be displayed for a possible artist if typed incorrectly?

#Resources
1. [Pyechonest]
2. [Check for '-' between artist and song title]
3. [Split string at '-']
4. [Replace + for ' ' in search]

###Abstract
The search can be further improved by allowing specific artist and song title search.
```python
python music_info.py pink floyd - money
```
This now prints a list of possible artists and statistics for the most similar song to each possible artist. This includes the artist location, danceability, tempo, loudness, and duration.

The program supports both artist searches and artist/song title searches by checking for a '-' between the two using methods provided by Python. This includes the split and replace to allow for easier. This is done by checking for the symbol in an if statement:
```python
if '-' in search_words:
        lis = search_words.split('-')
        a_results = artist.search(name=lis[0])
        replaced = [l.replace('+', '') for l in lis[1]]
        new_song = ''
        new_song = ''.join(replaced)
        new_combined = lis[0] + new_song
        results = song.search(combined=new_combined)
```
By default, the program searches for the 5 most similar artist to a search query. If any fewer are found, an IndexError is thrown. I resolved this issue by catching the exception and having a proper message printed.
```python
except IndexError:
        print 'Search complete!'
```

[Pyechonest]: https://github.com/echonest/pyechonest
[Check for '-' between artist and song title]: http://stackoverflow.com/questions/4877844/how-would-i-check-a-string-for-a-certain-letter-in-python
[Split string at '-']: http://www.tutorialspoint.com/python/string_split.htm
[Replace + for ' ' in search]: http://stackoverflow.com/questions/3136689/find-and-replace-string-values-in-python-list