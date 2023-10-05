#this is where cool shit happens

from classes import Browser
from classes import URL

print("It works")

if __name__ == "__main__":
    #import sys
    url = URL("http://example.org/index.html")

    #so cool that my logic worked
    text = url.clean_tags()


    browser = Browser()
    browser.layout(text)
    browser.start()
