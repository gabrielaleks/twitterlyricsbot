from genius import genius

def searchArtistSongs(artist):
    artist = genius.search_artist(artist_name='', artist_id=artist, sort='popularity')
    songs = artist.songs
    return songs