import lyricsgenius as lg
import random
import secret
import json

# Starting API
genius = lg.Genius(secret.client_access_token, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

# Iterating through possible artists and randomly selecting one
chosenArtist = []
with open('artists.json') as data_file:
    data = json.load(data_file)
    numberOfArtists = len(data['properties'])
    randomArtist = random.randint(0, numberOfArtists-1)
    chosenArtist = data['properties'][randomArtist]
    
# Searching every song of the artist
# artist = genius.search_artist(artist_name='', artist_id=chosenArtist['artistId'], sort='popularity')
artist = genius.search_artist(artist_name='', artist_id=chosenArtist['artistId'], sort='popularity', max_songs=2, get_full_info=False) # test
songs = artist.songs

if (chosenArtist['artistName'] == 'Zander'):
    songs = songs[0:19] + songs[20:23]

# Picking one song and getting its lyrics
randomSong = random.randint(0, len(songs)-1)
songName = songs[randomSong].title
songLyrics = songs[randomSong].lyrics

# Selecting 4 random lines from the song
print("----------------")
print(songLyrics)
print("\n")
print(chosenArtist['artistName'] + ' - ' + songName)
print("----------------")

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