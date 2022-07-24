from Health.SECRETS import *
import requests


response = requests.get(f'https://maps.googleapis.com/maps/api/place/details/json?place_id={PLACE_ID}&key={GOOGLE_KEY}') 


# GET GOOGLE COMMENT AND ADD WEBSITE EVERY WEEK