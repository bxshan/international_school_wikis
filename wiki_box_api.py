from datetime import datetime
import requests

def get_languages(title: str):
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "prop": "langlinks",
        "titles": title,
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    PAGES = DATA["query"]["pages"]

    languages = ['en']
    for key in PAGES.keys():
        page = PAGES[key]
        page_title = page["title"]
        for item in page["langlinks"]:
            languages.append(item["lang"])

        # print("        Title: \"" + page_title + "\"")
        print("        Languages: ", languages)

        return(languages)


def get_last_revisions(title: str, print_mode: bool):
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        "action": "query",
        "prop": "revisions",
        "titles": str(title),
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

    if (print_mode):
        for page in PAGES:
            for revision in page["revisions"]:
                print("User: ", revision["user"])
                print("Time: ", revision["timestamp"])
                print("Comment: ", revision["comment"])
                print("")
    else:
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
            print("        Week: ", index, "Revisions: ", revisions_per_week[index])


def get_pageviews(title:str):
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "prop": "pageviews",
        "titles": title,
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
            if (type(page["pageviews"][date_key]) == int):
                pageviews = page["pageviews"][date_key]
            else:
                pageviews = 0
            if index in pageviews_per_week:
                # print(page["pageviews"][date_key])
                pageviews_per_week[index] += pageviews
            else:
                pageviews_per_week[index] = pageviews

    for index in pageviews_per_week.keys():
        print("        Week: ", index, "Pageviews: ", pageviews_per_week[index])
