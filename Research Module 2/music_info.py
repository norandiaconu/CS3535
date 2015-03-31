#!/usr/bin/env python
# encoding: utf=8
"""
music_info.py

Search for information on a song or artist.

By Noran Diaconu, 2015-03-31.
"""

usage = """
Usage: 
    python music_info.py <search_query>

Example:
    python music_info.py pink floyd - money
"""

def main(search_words):
    from pyechonest import song
    from pyechonest import artist
    print search_words
    if '-' in search_words:
        lis = search_words.split('-')
        a_results = artist.search(name=lis[0])
        replaced = [l.replace('+', '') for l in lis[1]]
        new_song = ''
        new_song = ''.join(replaced)
        new_combined = lis[0] + new_song
        results = song.search(combined=new_combined)
        print 'song name: ', new_song
    else:
        results = song.search(combined=search_words)
        a_results = artist.search(name=search_words)
    x = 0
    try:
        for x in range(0, 5):
            print 'Result', x
            search_item = results[x]
            a_search_item = a_results[x]
            print 'artist name: ', a_search_item.name
            print 'artist location:', search_item.artist_location
            print 'danceability:', search_item.audio_summary['danceability']
            print 'tempo:', search_item.audio_summary['tempo']
            print 'loudness:', search_item.audio_summary['loudness']
            print 'duration:', search_item.audio_summary['duration']
            print 
            x += 1
    except IndexError:
        print 'Search complete!'

if  __name__ == '__main__':
    import sys
    y = 0
    z = True
    search_words = ''
    while z:
        if len(sys.argv) > y:
            y += 1
        else:
            z = False
    try:
        if y == 2:
            search_words = sys.argv[1]
        else:
            search_words = sys.argv[1]
            for a in range(2, y):
                search_words = search_words + '+' + sys.argv[a]
            search_words
    except:
        print usage
        sys.exit(-1)
    main(search_words)
