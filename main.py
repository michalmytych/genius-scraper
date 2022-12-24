import json
import sys
import os
import time
from src.scrapers import GeniusScraper


output_file_path = "storage/"
linesep = os.linesep
script_path = os.path.realpath(os.path.dirname(__file__))
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

try:
  song_id = sys.argv[1]
except IndexError:
  msg = f"{linesep}When launching script you should provide " \
      + "song ID as command line argument." \
      + f"like: {linesep} python3 main.py song_id {linesep}"
  print(msg)
  exit(-1)

scraper = GeniusScraper(song_id)

if '-cm' in opts:
  scraper.console_mode = True

lyrics = scraper.scrape()

if not lyrics:
  lyrics = scraper.scrape(webpage='old')

if not lyrics:
  lyrics = []

lyrics_data = {
  "id": int(song_id),
  "timestamp": time.time(),
  "lines": lyrics
}

lyrics_json = json.dumps(lyrics_data)
full_file_path = script_path + '/' + output_file_path + str(song_id) + '.json'

with open(full_file_path, "w") as output_file:
  output_file.write(lyrics_json)
