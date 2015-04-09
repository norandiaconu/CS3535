#Inquiry Report 5
Music Information

#Problem
Find a better way to search for music information.

#Question
1. Can the information be shown in a more useful way?
2. Can the song title be better displayed?
3. Will a separate search for artist and song title be better than the combined approach when not using a '-'?

#Resources
1. [Pyechonest]
2. [Check for '-' between artist and song title]
3. [Split string at '-']
4. [Replace + for ' ' in search]
5. [More API method calls]

###Abstract
The search can be further improved by allowing a variety of ways to search.
```python
python music_info.py pink floyd - money
python music_info.py pink floyd money
python music_info.py pink floyd
python music_info.py money
```
This now prints a list of possible artists and statistics for the most similar song to each possible artist. This includes the artist location, danceability, tempo, loudness, and duration.

The song title now includes spaces when being searched by modifying this line.
```python
replaced = [l.replace('+', ' ') for l in lis[1]]
```
The extra result printed at the bottom of each search is unnecessary and removed with another try catch to see whether the next loop is an IndexError or not.
```python
try:
       search_item = results[x]
       a_search_item = a_results[x]
except IndexError:
       print 'Search complete!'
       break
```

The iterations for each search are 0-based, but the result number has been changed on the output to better show the user what iteration the program is on by printing the result+1.
```python
print 'Result', x+1
```

[Pyechonest]: https://github.com/echonest/pyechonest
[Check for '-' between artist and song title]: http://stackoverflow.com/questions/4877844/how-would-i-check-a-string-for-a-certain-letter-in-python
[Split string at '-']: http://www.tutorialspoint.com/python/string_split.htm
[Replace + for ' ' in search]: http://stackoverflow.com/questions/3136689/find-and-replace-string-values-in-python-list
[More API method calls]:
http://developer.echonest.com/docs/v4
