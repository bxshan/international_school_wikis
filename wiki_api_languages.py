#!/usr/bin/python3

# returns languages available of a specific wikipedia article

from datetime import datetime
import requests

S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "prop": "langlinks",
    "titles": "International School of Beijing",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

languages = []
for key in PAGES.keys():
    page = PAGES[key]
    page_title = page["title"]
    for item in page["langlinks"]:
        languages.append(item["lang"])

    print("Title: \"" + page_title + "\"")
    print("Languages: ", languages)
