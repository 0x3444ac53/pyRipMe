import json
import requests

def scraper(url : str) -> list:
    """
    Takes an imgur album url and return a list of
    a picture urls. This ustilises the imgur api.
    """
    album_id = url.split('/')[-1]
    image_links = []
    raw_response = get_link_list(album_id)
    if raw_response[0] != 200:
        raise thereIsSomeProblemException
    for i in raw_response[1]['data']:
        image_links.append(i['link'])
    return image_links


def get_link_list(album_id : str) -> dict:
    api_end_point = "https://api.imgur.com/3/gallery/r/{}/time/month/"
    headers = {"Authorization" : "Client-ID 6c45adac556176f"}
    r = requests.get(api_end_point.format(album_id), headers=headers)
    return (r.status_code, r.json())

def get_name(url : str) -> str:
    return f'reddit_{url.split("/")[-1]}'
