import os
from dotenv import load_dotenv
from flask import Flask, request, abort
import service 
import json

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

def authorized(request):
    return True
    try:
      return request.headers['X-Api-Key'] == app.config['SECRET_KEY']
    except:
      return False

@app.route("/scrape", methods=['GET'])
def index():
    if authorized(request): 
        args = request.args
        song_id = args.get("song_id")
        if song_id is None:
            return json.dumps({
              "message": "You must provide ?song_id GET parameter."
            })
        else:
            return service.run_scraping(song_id)
    else:
        abort(401)
