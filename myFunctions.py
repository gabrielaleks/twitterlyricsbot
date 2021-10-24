import secret
import json
import random
import tweepy
from datetime import datetime

# Main functions

def startApi(lg):
    return lg.Genius(secret.client_access_token, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)", "Ao Vivo"], remove_section_headers=True)

def selectRandomArtist():
    with open('/home/gabriel/Projects/TwitterBot/hardcoretriste/artists.json') as data_file:
        data = json.load(data_file)
        numberOfArtists = len(data['properties'])
        randomArtist = randomize(numberOfArtists, 1)
        return data['properties'][randomArtist]

def iterateArtistSongs(genius, chosenArtist):
    # artist = genius.search_artist(artist_name='', artist_id=chosenArtist['artistId'], sort='popularity', max_songs=5, get_full_info=False) # For tests
    artist = genius.search_artist(artist_name='', artist_id=chosenArtist['artistId'], sort='popularity')
    artist.songs = handleSpecialArtistCases(artist.songs, chosenArtist)
    return artist.songs

def handleSpecialArtistCases(artistSongs, chosenArtist):
    if (chosenArtist['artistName'] == 'Zander'):
        return artistSongs[0:19] + artistSongs[20:23]
    else:
        return artistSongs
    
def chooseSong(songs):
    # return 1 # TESTS - Return a specific song
    return randomize(len(songs), 1)

def getSongName(songs, chosenSong):
    return songs[chosenSong].title

def getSongLyrics(songs, chosenSong):
    return songs[chosenSong].lyrics

# For tests
def printSong(lyrics, artist, songName):
    print("----------------")
    print(lyrics)
    print("\n")
    print(artist['artistName'] + ' - ' + songName)
    print("----------------")
    
def assembleFourVerses(lyrics):
    lines = lyrics.split('\n')
    song = []
    for line in lines:
        line = removeUnnecessaryInfo(line)
        if not line:
            continue
        else:
            song.append(line)
            

    maxStartingPoint = len(song)
    startingPoint = randomize(maxStartingPoint, 4)

    # separatedVerses = song[5:9] # TESTS - Selecting a specific part of the lyrics
    separatedVerses = song[startingPoint:startingPoint+4]
    joinedVerses = '\n'.join(separatedVerses)

    return joinedVerses
    
def assembleTweet(fourVerses, chosenArtist, songName):
    authorship = chosenArtist['artistName'] + ' - ' + songName
    return (fourVerses + "\n\n" + authorship)
    
def tweetLyrics(tweet):
    try: 
        auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_secret)
        auth.set_access_token(secret.key, secret.secret)
        api = tweepy.API(auth)
        api.update_status(tweet)
        successMessage(tweet)
    except Exception as e:
        errorMessage(e, tweet)

# 
# -----
# 

# Utils

def randomize(integer, margin):
    return random.randint(0, integer-margin)

def removeUnnecessaryInfo(str):
    if "EmbedShare URLCopyEmbedCopy" in str:
        newStr = str.replace("EmbedShare URLCopyEmbedCopy", "")
        return newStr
    else:
        return str

def successMessage(tweet):
    currentTime = getTime()
    f = open("success.txt", "a")
    f.write("***" + currentTime + "***" + '\n')
    f.write(tweet)
    f.write("\n**********")
    f.write("\n\n")
    f.close()
    print("-----")
    print("The following tweet was made:\n")
    print(tweet)
    print("-----")

def errorMessage(exception, tweet):
    currentTime = getTime()
    f = open("errors.txt", "a")
    f.write("***" + currentTime + "***" + "\n" + str(exception) + "\n")
    f.write("Tweet: " + "\n" + tweet)
    f.write("\n**********")
    f.write("\n\n")
    f.close()
    print("-----")
    print("The following exception was thrown:\n")
    print(exception)
    print("\n-----")

def getTime():
    now = datetime.now()
    return now.strftime("%d/%m/%y %H:%M:%S")