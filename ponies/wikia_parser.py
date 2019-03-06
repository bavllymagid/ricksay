# This script parses Rick'n'Morty wikia for nice pngs

from requests_html import HTMLSession
import requests
import re, shutil, os.path

session = HTMLSession()

# Start with Morties
for i in range(1, 313):
    fname = "PM-{:03d}.png".format(i)
    if os.path.exists("png/" + fname):
        continue
    l = "http://rickandmorty.wikia.com/wiki/File:{}".format(fname)
    r = session.get(l)
    if r.ok:
        img_link = r.html.find("#file a img")[0].attrs['data-src']
        if img_link:
            print("Downloading {}".format(img_link))
            img = requests.get(img_link, stream=True)
            with open('png/{}'.format(fname), 'wb') as out:
                shutil.copyfileobj(img.raw, out)

# Time for Ricks
page = session.get("http://rickandmorty.wikia.com/wiki/List_of_Pocket_Mortys_trainers_and_NPCs")
links = page.html.find("#WikiaArticle table.wikitable.sortable tr td a.image")
for l in links:
    img_link = l.attrs['href']
    m = re.findall("\w*rick\w*\.png", img_link, re.IGNORECASE)
    if m and not os.path.exists("png/{}".format(m)):
        print("Downloading {}".format(img_link))
        img = requests.get(img_link, stream=True)
        with open('png/{}'.format(m[0]), 'wb') as out:
            shutil.copyfileobj(img.raw, out)
