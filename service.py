import json
import sys
import os
import time
from src.scrapers import GeniusScraper

def run_scraping(id = None):
  output_file_path = "storage/cache/"
  linesep = os.linesep
  script_path = os.path.realpath(os.path.dirname(__file__))
  opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

  if '-cm' in opts:
    try:
      song_id = sys.argv[1]
    except IndexError:
      msg = f"{linesep}When launching script you should provide " \
          + "song ID as command line argument." \
          + f"like: {linesep} python3 main.py song_id {linesep}"
      print(msg)
      exit(-1)
  else:
      song_id = id

  lyrics_file = script_path + '/' + output_file_path + str(song_id) + '.json'
  already_scraped = os.path.isfile(lyrics_file)

  if already_scraped:
    scraped = ''
    with open(lyrics_file, "r") as scraped_contents:
      scraped = scraped_contents.read()
    return scraped

  scraper = GeniusScraper(song_id)
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

  with open(lyrics_file, "w") as output_file:
    output_file.write(lyrics_json)

  return lyrics_json


