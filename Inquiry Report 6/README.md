#Inquiry Report 6
Music Information

#Problem
Find a better way to search for music information.

#Question
1. Can the information be shown in a more useful way?
2. Can more information for an artist be shown?
3. Will a separate search for artist and song title be better than the combined approach when not using a '-'?

#Resources
1. [Pyechonest]
2. [Check for '-' between artist and song title]
3. [Split string at '-']
4. [Replace + for ' ' in search]
5. [More API method calls]
6. [Raw_input]

###Abstract
The search can be further improved by allowing a variety of ways to search.
```python
python music_info.py pink floyd - money
python music_info.py pink floyd money
python music_info.py pink floyd
python music_info.py money
```

A biography of the artist you are searching for can also be displayed by entering y or n after the program displays the current results for your search words. This is performed with the following code.
```python
bio = raw_input('Would you like to see biography information for this artist (y/n): ')
print bio
if 'y' in bio:
    a_search_item = a_results[x]
    print a_search_item.biographies[1]
```
This is conducted in the first iteration of the program to find the biography of the most similar artist.

[Pyechonest]: https://github.com/echonest/pyechonest
[Check for '-' between artist and song title]: http://stackoverflow.com/questions/4877844/how-would-i-check-a-string-for-a-certain-letter-in-python
[Split string at '-']: http://www.tutorialspoint.com/python/string_split.htm
[Replace + for ' ' in search]: http://stackoverflow.com/questions/3136689/find-and-replace-string-values-in-python-list
[More API method calls]: http://developer.echonest.com/docs/v4
[Raw_input]: http://www.cyberciti.biz/faq/python-raw_input-examples/