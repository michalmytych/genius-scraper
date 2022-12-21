class GeniusSongURL:
  BASE_URL = "https://genius.com/songs/"
  song_id = None

  def __init__(self, song_id):
    self.song_id = str(song_id)

  def __str__(self):
    return self.BASE_URL + self.song_id
