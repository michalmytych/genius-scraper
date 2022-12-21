class LyricsElementNotFoundException(Exception):
  def __init__(self):
    self.message = "Lyrics element was not found in scraped content."
    super().__init__(self.message)

