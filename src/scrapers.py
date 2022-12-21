import requests
import re as regex
from bs4 import BeautifulSoup

from src.config import GeniusSongURL
from src.exceptions import LyricsElementNotFoundException

class GeniusScraper:
  LYRICS_CONTAINER_CLASS_LIKE = 'Lyrics__Container'

  def __init__(self, song_id):
    self.song_url = GeniusSongURL(song_id)

  def get_lyrics_element(self, soup):
    try:
      selector = f'div[class*="{self.LYRICS_CONTAINER_CLASS_LIKE}"]'
      hits = soup.select(selector)
      return hits[0]
    except:
      raise LyricsElementNotFoundException

  def split_soup_into_lines(self, element_soup):
    raw_html = str(element_soup)
    html_lines = raw_html.split("<br/>")
    return html_lines

  def scrape(self):
    page = requests.get(self.song_url)
    bs = BeautifulSoup(page.text, 'html.parser')

    first_found = self.get_lyrics_element(bs)
    html_lines = self.split_soup_into_lines(first_found)

    lyrics = []

    for line in html_lines:
      line_soup = BeautifulSoup(line, 'html.parser')
      line_text = line_soup.get_text()
      clean_line = regex.sub(r'[\(\[].*?[\)\]]', '', line_text)
      lyrics.append(clean_line)
    
    lyrics = filter(lambda l : l != '', lyrics)

    return list(lyrics)

