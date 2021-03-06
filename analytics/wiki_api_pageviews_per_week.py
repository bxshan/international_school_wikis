#!/usr/bin/python3

# returns pageviews per week of a specific wikipedia article

from datetime import datetime
import requests

S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "prop": "pageviews",
    "titles": "International School of Beijing",
    "pvipdays": "60",
    "formatversion": "2",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

pageviews_per_week = {}
for page in PAGES:
    date_keys = page["pageviews"].keys()
    for date_key in date_keys:
        year_number = datetime.fromisoformat(date_key).isocalendar()[0]
        week_number = datetime.fromisoformat(date_key).isocalendar()[1]
        index = str(year_number) + "-" + str(week_number)
        if index in pageviews_per_week:
            pageviews_per_week[index] += page["pageviews"][date_key]
        else:
            pageviews_per_week[index] = page["pageviews"][date_key]

for index in pageviews_per_week.keys():
    print("Week: ", index, "Pageviews: ", pageviews_per_week[index])
