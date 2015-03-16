#!/usr/bin/env python
# encoding: utf=8
"""
music_info.py

Search for information on a song or artist.

By Noran Diaconu, 2015-03-16.
"""

usage = """
Usage: 
    python music_info.py <search_query>

Example:
    python music_info.py pink+floyd+money
"""

def main(search_words):
	from pyechonest import song
    results = song.search(combined=search_words)
	search_item = results[0]
	print 'artist location:',search_item.artist_location
	print 'danceability:',search_item.audio_summary['danceability']
	print 'tempo:',search_item.audio_summary['tempo']
	print 'loudness:',search_item.audio_summary['loudness']
	print 'duration:',search_item.audio_summary['duration']

if  __name__ == '__main__':
    import sys
    try:
        search_words = sys.argv[1]
    except:
        print usage
        sys.exit(-1)
    main(search_words)
