import os
import requests
from dotenv import load_dotenv
import json


load_dotenv()

API_KEY = os.getenv("SPOTIFY_KEY")
CLIENT = os.getenv("CLIENT")


if not API_KEY:
    raise ValueError("API key is missing. Make sure to add it to the .env file.")




def get_token () : 
    url = "https://accounts.spotify.com/api/token"

    payload = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT,
        'client_secret': API_KEY
    }   
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }   
    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        token_data = response.json()
        return token_data["access_token"]
    else:
        print(f"Failed to retrieve token. Status code: {response.status_code}")
        print("Response:", response.text)

# Fonction pour récupérer les playlists depuis l'API
def get_playlists():
    try:
        API_URL = "https://api.spotify.com/v1/playlists/37i9dQZEVXbIPWwFssbupI"

        headers = {
            "Authorization": f"Bearer {get_token()}"
        }

        response = requests.get(API_URL, headers=headers) 
        
        if response.status_code == 200:
            playlists = response.json()  
            with open('playlists.json', 'w') as json_file:json.dump(playlists, json_file, indent=4)
        else:
            print(f"Erreur lors de la récupération des playlists: {response.status_code}")
    
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

# Appeler la fonction pour afficher les playlists
if __name__ == "__main__":
    get_playlists()