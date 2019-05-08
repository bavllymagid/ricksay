from requests_html import HTMLSession
from collections import defaultdict

session = HTMLSession()
r = session.get("https://www.imdb.com/title/tt2861424/quotes")
characters = ("Rick", "Morty", "Summer", "Jerry", "Beth")
counter = defaultdict(int)

qs = r.html.find("div.sodatext p")
for q in qs:
    span = q.find("span.character")
    char = span[0].element.text if len(span) else None
    if char and char in characters:
        with open('{}.{}'.format(char, counter[char]), 'w') as qfile:
            qfile.write(q.text)
            counter[char] += 1

