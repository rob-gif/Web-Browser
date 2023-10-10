# this is where cool shit happens

from classes import Browser
from classes import URL
from classes import Layout

print("It works")

if __name__ == "__main__":
    import sys
    url = URL("https://browser.engineering/index.html")
    text = url.clean_tags()
    Browser.start()
