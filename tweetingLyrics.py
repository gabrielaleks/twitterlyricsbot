#!/bin/sh

from myFunctions import *
import lyricsgenius as lg

# Starting API
genius = startApi(lg)

# Iterating through possible artists and randomly selecting one
chosenArtist = selectRandomArtist()
    
# Searching every song of the artist
songs = iterateArtistSongs(genius, chosenArtist)

# Picking one song and getting its lyrics and name
chosenSong = chooseSong(songs)
songLyrics = getSongLyrics(songs, chosenSong)
songName = getSongName(songs, chosenSong)

# Selecting 4 random verses from the song
fourVerses = assembleFourVerses(songLyrics)

# Assembling song + authorship into one string
tweet = assembleTweet(fourVerses, chosenArtist, songName)
# print(tweet) ### TEST

# Twitting the string
tweetLyrics(tweet)