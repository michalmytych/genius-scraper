import os
from dotenv import load_dotenv
from flask import Flask, request, abort
import service 
import json

load_dotenv()

app = Flask(__name__)
app.config['API_KEY'] = os.environ.get('API_KEY')

def authorized(request):
    try:
      return request.headers['X-Api-Key'] == app.config['API_KEY']
    except:
      return False

@app.route("/scrape", methods=['GET'])
def index():
    if authorized(request): 
        args = request.args
        song_id = args.get("song_id")
        if song_id is None or song_id == '':
            return json.dumps({
              "message": "You must provide ?song_id GET parameter."
            })
        else:
            return service.run_scraping(song_id)
    else:
        abort(401)
