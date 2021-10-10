import secret
import json
import random

# Main functions

def startApi(lg):
    return lg.Genius(secret.client_access_token, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

def selectRandomArtist():
    chosenArtist = []
    with open('artists.json') as data_file:
        data = json.load(data_file)
        numberOfArtists = len(data['properties'])
        randomArtist = random.randint(0, numberOfArtists-1)
        return data['properties'][randomArtist]

def iterateArtistSongs(genius, chosenArtist):
    # artist = genius.search_artist(artist_name='', artist_id=chosenArtist['artistId'], sort='popularity')
    artist = genius.search_artist(artist_name='', artist_id=chosenArtist['artistId'], sort='popularity', max_songs=5, get_full_info=False) # test
    artist.songs = handleSpecialArtistCases(artist.songs, chosenArtist)
    return artist.songs

def handleSpecialArtistCases(artistSongs, chosenArtist):
    if (chosenArtist['artistName'] == 'Zander'):
        return artistSongs[0:19] + artistSongs[20:23]
    else:
        return artistSongs
    
def chooseSong(songs):
    return random.randint(0, len(songs)-1)

def getSongName(songs, chosenSong):
    return songs[chosenSong].title

def getSongLyrics(songs, chosenSong):
    return songs[chosenSong].lyrics

# teste
def printSong(lyrics, artist, songName):
    print("----------------")
    print(lyrics)
    print("\n")
    print(artist['artistName'] + ' - ' + songName)
    print("----------------")
    
def pickFourLines():
    print("oi")
    
def assembleString():
    print("oi")
    
def tweet():
    print("oi")

# 
# -----
# 

# Utils

def randomize():
    print("oi")

def removeUnnecessaryInfo():
    print("oi")