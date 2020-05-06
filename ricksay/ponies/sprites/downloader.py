# This script parses sprites shared from Pocket Morties game
# Depends on Spriters Resource markup...

from requests_html import HTMLSession
import requests
import re, shutil, os.path
from urllib.parse import urlparse

def download_file(url, folder):
    local_filename = os.path.join(folder, url.split('/')[-1])
    print("Saving", local_filename)
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

print("Started Schwifting")
session = HTMLSession()
sprites_url = "https://www.spriters-resource.com/mobile/pocketmortys/"
host = urlparse(sprites_url).netloc
characters = ('Rick', 'Morty', 'Beth', 'Jerry', 'Summer')
for char in characters:
    if not os.path.exists(char):
        os.mkdir(char)

print("Parsing main page for imgs")
page = session.get(sprites_url).html
sprites = page.find("div.iconbody img")

for sprite in sprites:
    img_link = sprite.attrs['src']
    char = sprite.attrs['alt'].split()[-1]
    url = f"http://{host}/{img_link}" 
    if char in characters:
        download_file(url, char)

print("Wubba Lubba Dub Dub, Done!")
