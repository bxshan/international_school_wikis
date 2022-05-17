#!/usr/bin/python3

# returns latest revisions to a specific wikipedia article
# followed example from: https://www.mediawiki.org/wiki/API:Revisions#Python

from datetime import datetime
import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "International School of Beijing",
    "rvprop": "timestamp|user|comment",
    "rvslots": "main",
    "rvlimit": "5",
    "rvstart": "",
    "rvend": "2022-01-01T00:00:00Z",
    "formatversion": "2",
    "format": "json"
}

curr_date = datetime.today().strftime("%Y-%m-%d")
curr_date += "T00:00:00Z"
PARAMS["rvstart"] = curr_date

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for page in PAGES:
    for revision in page["revisions"]:
        print("User: ", revision["user"])
        print("Time: ", revision["timestamp"])
        print("Comment: ", revision["comment"])
        print("")

print("------------------------")

revisions_per_week = {}
for page in PAGES:
    for revision in page["revisions"]:
        date_key = revision["timestamp"]
        date_key = date_key[0:-1]
        year_number = datetime.fromisoformat(date_key).isocalendar()[0]
        week_number = datetime.fromisoformat(date_key).isocalendar()[1]
        index = str(year_number) + "-" + str(week_number)
        if index in revisions_per_week:
            revisions_per_week[index] += 1
        else:
            revisions_per_week[index] = 1

for index in revisions_per_week.keys():
    print("Week: ", index, "Revisions: ", revisions_per_week[index])
