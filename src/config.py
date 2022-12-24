class GeniusSongURL:
  @staticmethod
  def get_old_url(song_id):
    return f"https://genius.com/songs/{song_id}?bagon=1"

  @staticmethod
  def get_new_url(song_id):
    return f"https://genius.com/songs/{song_id}"

