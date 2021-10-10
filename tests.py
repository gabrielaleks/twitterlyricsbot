x = [4, 3, 4, 6]

x = x[0:1] + x[2:3]

print(x)
print(len(x))

import lyricsgenius as lg
import secret

genius = lg.Genius(secret.client_access_token, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
artist = genius.search_artist(artist_name='-', artist_id=48020, sort='popularity')
print(artist)