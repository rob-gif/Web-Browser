# this is where cool shit happens

from classes import Browser
from classes import URL
from classes import Layout

print("browser v1.0.0")

if __name__ == "__main__":
    url = URL("http://example.org/index.html")

    header, body = url.request()
    text = url.text(body)

    layout = Layout(text)
    display_list = layout.display_list()

    browser = Browser(body)
