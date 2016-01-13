import urllib2
import spotipy
import webbrowser
def findtitle(yturl):
"""Gets an youtube url as parameter and returns the title of the video
Using the string method find on the page
It does not work with characters like ' or % """
    url = yturl
    page = urllib2.urlopen(url)
    data = page.read()
    spos = data.find("<title>") + 7
    epos = data.find(" - YouTube</title>")
    title = data[spos:epos]
    if title.lower().find('official video'): #videos with ('Oficial Video')
        title = title[:title.lower().find('official video')-1]
    return title
    page.close()

def spotifysearch(song):
"""Does a search on spotify and returns the url for the first song on the search
Also using the find method on the spotify search
Not always accurate search """
    spotify = spotipy.Spotify()
    results = spotify.search(q=str(song), type='track')
    results = str(results)
    ssong = results.find("https://open.spotify.com/track/")
    endsong = results.find("'}, u'popularity'")
    song_url = results[ssong:endsong]
    newfile = open('newfile.txt','w')
    newfile.write(str(results))
    newfile.close()
    return song_url

#The input and the webbrowser.open method to open as a new tab
x = raw_input('Type an Youtube URL to get the song on spotify: ')
final = spotifysearch(findtitle(x))
tittle_song = findtitle(x)
webbrowser.open(final,2)
