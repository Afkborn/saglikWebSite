from Health.SECRETS import *
import requests
from home.models import Comment
from datetime import datetime

def getCommentFromGoogle():
    """ GET COMMENT FROM GOOGLE, \nPlace IDs uniquely identify a place in the Google Places database and on Google Maps, GOOGLE_KEY = Google API Key """
    commentList = []
    response = requests.get(f'https://maps.googleapis.com/maps/api/place/details/json?place_id={PLACE_ID}&key={GOOGLE_KEY}') 
    responseJson = response.json()
    reviews = responseJson['result']['reviews']
    for review in reviews:
        author_name, author_url,profile_photo_url,score,relative_time_description,comment,time = review['author_name'],review['author_url'],review['profile_photo_url'],review['rating'],review['relative_time_description'],review['text'],review['time']   
        isim_sayisi = author_name.count(' ')
        if isim_sayisi == 0:
            author_first_name = author_name
            author_last_name = ""
        elif isim_sayisi == 1:
            author_first_name = author_name.split(' ')[0]
            author_last_name =  author_name.split(' ')[1]
        else:
            author_first_name = "".join(author_name.split(' ')[:-1])
            author_last_name =  "".join(author_name.split(' ')[-1:])
        # unix time to datetime
        comment_date = datetime.fromtimestamp(time)
        is_google_comment = True
        show_home_page = True
        photo = profile_photo_url
        commentList.append(Comment(author_first_name=author_first_name,author_last_name=author_last_name,comment_date=comment_date,is_google_comment=is_google_comment,show_home_page=show_home_page,score=score,comment=comment,photo=photo))
    return commentList
            
        
    