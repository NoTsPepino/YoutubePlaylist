from pytube import Playlist

plsturl = input('Enter Youtube Playlist Url:')

  plst = Playlist(plsturl)

for vid in plst.videos:
  
  vid.streams.get_highest_resolution().download()
