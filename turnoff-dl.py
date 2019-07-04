#! /usr/bin/env python3
import feedparser
from lxml import etree
import urllib3

URL = "https://turnoff.us/feed.xml"

if __name__ == "__main__":
    decoded_feed = feedparser.parse(URL)
    title = decoded_feed.entries[0].title
    summary = decoded_feed.entries[0].summary
    image_link = etree.XML(summary).get("src")

    http = urllib3.PoolManager()
    response = http.request("GET", image_link, preload_content=False)

    with open(f"%s.png" % title, "wb") as f:
        for chunk in response.stream(32):
            f.write(chunk)
