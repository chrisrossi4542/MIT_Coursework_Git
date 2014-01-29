##KBCO Code
##Name: CRossi
##Program to scrape the KBCO look_for_your_name page for my name, and email me if it is there
import urllib2
import re

def check_name():
    fucksoup = urllib2.urlopen('http://www.kbco.com/pages/lookforyourname.html').read()

    if (re.search(r"Christopher Rossi", fucksoup, re.IGNORECASE)):
        return True
    return False

if check_name():
    print "you're a winner ho!"




