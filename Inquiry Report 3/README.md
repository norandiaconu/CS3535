#Inquiry Report 3
Music Information

#Problem
Find a better way to search for music information.

#Question
1. Could the information be shown in a more useful way?
2. Can more information be shown?
3. Can a more natural way to search be implemented?

#Resources
1. [Pyechonest]

###Abstract
A better search could be conducted by checking the number of arguments and conducting the search without having any necessary + signs between the words.
```python
python music_info.py pink floyd money
```
This currently prints the artist location, danceability, tempo, loudness, and duration.

Time_signature, for example, could also be added, but does not provide much useful information if searching only for an artist. 

[Pyechonest]: https://github.com/echonest/pyechonest