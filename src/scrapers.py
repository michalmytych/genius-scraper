import requests
import re as regex
from bs4 import BeautifulSoup
from src.config import GeniusSongURL
from src.exceptions import LyricsElementNotFoundException


class GeniusScraper:
  NEW_LYRICS_CLASS = 'Lyrics__Container'
  OLD_LYRICS_CLASS = 'lyrics'
  console_mode = False

  def __init__(self, song_id):
    self.old_song_url = GeniusSongURL.get_old_url(song_id)
    self.new_song_url = GeniusSongURL.get_new_url(song_id)

  def get_lyrics_element(self, soup, webpage):
    class_ = self.NEW_LYRICS_CLASS if webpage == 'new' else self.OLD_LYRICS_CLASS
    if self.console_mode == True:
        print(f'Scraping from {webpage} webpage.')
    try:  
      selector = f'div[class*="{class_}"]'
      hit = soup.select(selector)[0]
      if self.console_mode == True:
        print(f'Successfully scraped from {webpage} webpage.')
      return hit
    except:
      if self.console_mode:
        print(f"Lyrics element was not found in scraped content ({webpage} webpage).")
        return None
      else:
        raise LyricsElementNotFoundException

  def split_soup_into_lines(self, element_soup):
    raw_html = str(element_soup)
    html_lines = raw_html.split("<br/>")
    return html_lines

  def scrape(self, webpage = 'new'):
    song_url = self.new_song_url
    if webpage == 'old':
      song_url = self.new_song_url
      
    page = requests.get(song_url)
    bs = BeautifulSoup(page.text, 'html.parser')
    
    first_found = self.get_lyrics_element(bs, webpage)

    if not first_found:
      return None

    html_lines = self.split_soup_into_lines(first_found)
    lyrics = []

    for line in html_lines:
      line_soup = BeautifulSoup(line, 'html.parser')
      line_text = line_soup.get_text()
      clean_line = regex.sub(r'[\(\[].*?[\)\]]', '', line_text)
      lyrics.append(clean_line)
    
    lyrics = filter(lambda l : l != '', lyrics)

    return list(lyrics)

