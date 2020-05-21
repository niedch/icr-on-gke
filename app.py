from flask import Flask
import requests
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    spotify_auth_token = os.getenv("SPOTIFY_OAUTH")
    respo = requests.get("https://api.spotify.com/v1/me/player/recently-played", headers={"Authorization": f"Bearer {spotify_auth_token}"})
    
    return f"""Hey, this is the Hello World endpoint, spotify token={spotify_auth_token}
        {respo}
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
