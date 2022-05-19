from wiki_box_api import *
from school_list import *

school_list = get_school_list()

for school in school_list:
    print ("\033[1m" + school + ": ")
    print ("    Languages available: ")
    get_languages(school)
    print ("    Latest revisions: ")
    get_last_revisions(school, False)
    print("    Pageviews: ")
    get_pageviews(school)
