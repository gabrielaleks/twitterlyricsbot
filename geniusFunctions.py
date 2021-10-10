from myFunctions import *
import lyricsgenius as lg
import random
import secret
import json

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

# Selecting 4 random lines from the song
printSong(songLyrics, chosenArtist, songName)

# Assembling song + authorship into one string

# Twitting the string
# import tweepy
# import secret

# auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_secret)
# auth.set_access_token(secret.key, secret.secret)

# api = tweepy.API(auth)

# # tweets = api.mentions_timeline();
# # print(tweets[0])

# lyrics = 'ai ai ai'
# authorship = 'gabriel - sono'

# tweet = lyrics + '\n\n' + authorship

# api.update_status(tweet)

### possibilidades

## Dados de uma musica especifica
# http://api.genius.com/songs/:songId?access_token=:accessToken

## Dados de um artista
# http://api.genius.com/artists/:artistId?access_token=:accessToken

## Músicas de um artista específico
# http://api.genius.com/artists/:artistId/songs?access_token=:accessToken