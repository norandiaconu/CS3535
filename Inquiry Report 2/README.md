#Inquiry Report 2
Music Information

#Problem
Find a way to retrieve accurate information for an artist or song.

#Question
1. What will you need to know about a song?
2. Will a partial name work?
3. How long will it take to receive the results?

#Resources
1. [Pyechonest]

###Abstract
The search can be conducted by adding terms concatenated by + signs after the program call.
```python
python music_info.py pink+floyd+money
```
This will print the artist location, danceability, tempo, loudness, and duration.
```python
python beat_swap.py <input_filename> <output_filename>
python beat_swap.py lateralus.mp3 lateralus_swap.mp3
```
This allows the program to work for any song on your system.

[Pyechonest]: https://github.com/echonest/pyechonest