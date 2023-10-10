# this is where carlos request html from a remote server using pythons socket module

import socket
import ssl


# making my class
# downloading my web page
# code to connect to host
class URL:
    # this is my constructor --> used to initialize objects when used in a claass so example the url i will be able to pass
    # it as argument when i call a method
    def __init__(self, url):
        self.url = url
        self.scheme, url = url.split("://", 1)
        assert self.scheme in ["http", "https"], \
            "Unknown Scheme {}".format(self.scheme)

        if "/" not in url:
            url = url + "/"
        self.host, url = url.split("/",
                                   1)  # note that the url now becomes the rest of the url after the domain name -- clever
        self.path = "/" + url  # path is now something like /home/index.html

        # add support for custom ports
        if ":" in self.host:
            self.host, port = self.host.split(":", 1)
            self.port = int(port)

        # switch ports for both schemes
        if self.scheme == "http":
            self.port = 80
        elif self.scheme == "https":
            self.port = 443

    def request(self):
        # create a socket instance named s
        s = socket.socket(
            family=socket.AF_INET,  # means i'm using IPv4
            type=socket.SOCK_STREAM,  # specify socket stream ;)
            proto=socket.IPPROTO_TCP,  # specify i'm using tcp -- a cool protocol
        )
        # adding the target and port for connecting - pair
        s.connect((self.host, self.port))

        # adding https support for secure connections
        if self.scheme == "https":
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=self.host)

        # we already have a connection now let's send a request -- url

        # note --> using this {} and the .format()means that the value inside the .format() is put in the curly braces
        s.send(("GET {} HTTP/1.0\r\n").format(self.path).encode("utf8") + "Host: {}\r\n\r\n".format(self.host).encode(
            "utf8"))

        # let's read the response from the server
        # this will return a file-like object
        response = s.makefile("r", encoding="utf8", newline="\r\n")

        statusline = response.readline()  # reads line by line
        version, status, explanation = statusline.split(" ", 2)
        assert status == "200", "{}: {}".format(status, explanation)

        # i want  to work with the response(pretty much html more)
        headers = {}
        while True:
            line = response.readline()
            if line == "\r\n": break
            header, value = line.split(":", 1)
            headers[header.lower()] = value.strip()

            # making sure i don't have weird headers that mean abnormalcy
            assert "transfer-encoding" not in headers
            assert "content-encoding" not in headers

        body = response.read()
        s.close()
        return headers, body

    # This is just filtering the html tags and just displaying the text only
    def parse(self):
        # display web-page to canvas
        headers, body = self.request()

        # fix this logic
        text = ""
        in_tag = False
        for c in body:
            if c == "<":
                in_tag = True
                if text: self.add_text(text)
                text = ""
            elif c == ">":
                in_ta = False
            elif not in_angle:
                text += c
        print(text)
        return text

    # load method calls the show method
    def load(self):
        self.clean_tags()
