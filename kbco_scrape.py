##KBCO Code
##Name: CRossi
##Program to scrape the KBCO look_for_your_name page for my name, and email me if it is there
import urllib2
import re
from bs4 import BeautifulSoup

def check_name():
    soup = BeautifulSoup(urllib2.urlopen('http://www.kbco.com/pages/lookforyourname.html').read())

    name_search = soup.find_all(text=re.compile("Matthew Hooker"), limit = 1)
    if name_search != []:
        return True

print check_name()





