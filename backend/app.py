from flask import Flask
from flask import json
import requests
import os
from sample.core import get_hmm

app = Flask(__name__)

@app.route('/')
def hello_world():
    spotify_auth_token = os.getenv("SPOTIFY_OAUTH")
    respo = requests.get("https://spclient.wg.spotify.com/presence-view/v1/buddylist", headers={"Authorization": f"Bearer {spotify_auth_token}"})
    
    response = app.response_class(
        response=json.dumps(json.loads(respo.content)),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route("/hmm")
def hmm():
    return get_hmm()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
