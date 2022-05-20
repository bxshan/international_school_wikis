from wiki_box_api import *
from school_list import *

school_list = get_school_list()

for school in school_list:
    print ("\033[1m" + school[0] + ": ")
    print ("    Languages available: ")
    get_languages(school[0])
    print ("    Latest revisions: ")
    get_last_revisions(school[0], False)
    print("    Pageviews: ")
    get_pageviews(school[0])
