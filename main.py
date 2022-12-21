import json
import sys
import os
import time

from scrapers import GeniusScraper
 
output_file_path = "storage/"
script_path = os.path.realpath(os.path.dirname(__file__))

class NoSongIdProvided(Exception):
  def __init__(self):
    self.message = "When launching script you should provide " \
      + "song ID as command line argument." \
      + "like: python3 main.py song_id"
    super().__init__(self.message)

try:
  song_id = sys.argv[1]
except IndexError:
  raise NoSongIdProvided

scraper = GeniusScraper(song_id)
lyrics = scraper.scrape()

lyrics_data = {
  "id": int(song_id),
  "timestamp": time.time(),
  "lines": lyrics
}

lyrics_json = json.dumps(lyrics_data)
full_file_path = script_path + '/' + output_file_path + str(song_id) + '.json'

with open(full_file_path, "w") as output_file:
  output_file.write(lyrics_json)


