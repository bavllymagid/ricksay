import os
from requests_html import HTMLSession
from collections import defaultdict

session = HTMLSession()
r = session.get("https://www.imdb.com/title/tt2861424/quotes")
# characters to save quotes
characters = ("Rick", "Morty")
# count quotes for each
counter = defaultdict(int)

qs = r.html.find("div.sodatext p")
# iterate over quotes
for q in qs:
    # who says
    span = q.find("span.character")
    char = span[0].element.text if len(span) else None
    if char and char in characters:
        # save quotes to separate files in folders
        if not os.path.isdir(char):
            os.mkdir(char)
        fname = "{}/{}.{}".format(char, char, counter[char])
        with open(fname, "w") as qfile:
            print("writing {}".format(fname))
            # says what?
            qfile.write(q.text)
            counter[char] += 1
