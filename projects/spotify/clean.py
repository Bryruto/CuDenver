import pandas as pd
import sqlite3
from lookup import find

#open the database
conn = sqlite3.connect('spot.db', check_same_thread=False)

#pd.options.display.max_rows = 10
#open the csv into a data frame
def get_data(csv):

    df = pd.read_csv(csv)

#rename columns
    df= df.rename(columns = {
        'Track Name': 'song',
        'Artist Name(s)': 'artist',
        'Genres': 'genre',
        'Popularity':'popularity'
    })

    #get the columns i want only then sent to database
    songs = df[['song','popularity','artist','genre']]

    #loop through the artists # day 2 i want to look up the song because i get a genre every time
    for artists in songs['artist']:
        if ',' in artists:
            art = artists.split(",")
            genre = find(art[0])
        else:
            genre = find(artists)
        songs.loc[songs['artist'] == artists , 'genre'] =genre

    songs.to_sql('songs',conn,if_exists = 'append',index = False)
