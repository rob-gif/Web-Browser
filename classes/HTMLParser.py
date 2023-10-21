from classes.text import Text


class HTMLParser:
    def __init__(self, body):
        self.body = body
        self.unfinished = []

    def add_text(self, text):
        parent = self.unfinished[-1]
        node = Text(text, parent)

    def add_tag(self, tag):
        if tag.startswith("/"):
            node = self.unfinished.pop()
            parent = self.unfinished[-1]
            parent.children.append(node)
        else:
            parent = self.unfinished[-1]
            node = Element(tag, parent)
            self.unfinished.append(node)

    def finished(self):
        if len(self.unfinished) == 0:
            self.add_tag("html")
            while len(self.unfinished) > 1:
                node = self.unfinished.pop()
                parent = self.unfinished[-1]
                parent.children.append(node)
            return self.unfinished.pop()
