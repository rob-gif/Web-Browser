# this is where carlos request html from a remote server using pythons socket module

import socket
import ssl


class URL:
    def __init__(self, url):
        self.url = url
        self.scheme, url = url.split("://", 1)
        assert self.scheme in ["http", "https"], \
            "Unknown Scheme {}".format(self.scheme)

        if "/" not in url:
            url = url + "/"
        self.host, url = url.split("/", 1)
        self.path = "/" + url  # path is now something like /home/index.html

        # adding support for custom ports
        if ":" in self.host:
            self.host, port = self.host.split(":", 1)
            self.port = int(port)

        # switch ports for both schemes
        if self.scheme == "http":
            self.port = 80
        elif self.scheme == "https":
            self.port = 443

    def request(self):
        s = socket.socket(
            family=socket.AF_INET,  # using IPv4
            type=socket.SOCK_STREAM,  # socket type of socket ;)
            proto=socket.IPPROTO_TCP,  # specify i'm using tcp -- a cool protocol
        )
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

        status_line = response.readline()  # reads line by line
        version, status, explanation = status_line.split(" ", 2)
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
        #print(body)
        s.close()

        return headers, body

    # method to filter tags
    def text(self, body):
        text = []
        in_angle = False
        for c in body:
            if c == "<":
                in_angle = True
            elif c == ">":
                in_angle = False
            elif not in_angle:
                text += c

        #cleaned_text = ''.join(text)

        return text

"""
if __name__=="__main__":
    url = URL("http://example.org/index.html")
    header, body = url.request()
    print(body)
    print(url.text(body))
"""
