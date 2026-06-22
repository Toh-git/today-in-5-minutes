import feedparser

weblist =(
    {'url': "https://feeds.bbci.co.uk/news/rss.xml", "name":"BBC"},
    {'url': 'https://www.thairath.co.th/rss/news', 'name': 'ไทยรัฐ'},
    {'url': 'http://rssfeeds.sanook.com/rss/feeds/sanook/news.index.xml', 'name': 'สนุกดอทคอม'},
    {'url': 'https://news.thaipbs.or.th/rss/news', 'name': 'thaipbs'},
    {'url': 'https://www.prachachat.net/feed', 'name': 'ประชาชาติ'},
    {'url': 'http://www.lokwannee.com/web2013/?cat=69&feed=rss2', 'name': 'โลกวันนี้'},
    {'url': 'https://www.matichon.co.th/feed', 'name': 'มติชน'},
    {'url': 'https://voicetv.co.th/rss', 'name': 'Voice TV'}
    )

html = """
<html>
<head>
<title>Today in 5 Minutes</title>
</head>
<body>

<h1>🔥 ข่าวเด่นวันนี้</h1>

<ul>
"""
for web in weblist:
    url = web["url"]
    feed = feedparser.parse(url)
for item in feed.entries[:10]:

    html += f"""
    <li>
        <a href="{item.link}">
        {item.title}
        </a>
    </li>
    """

html += """
</ul>

</body>
</html>
"""

with open("index.html", "w", encoding="utf8") as f:
    f.write(html)

print("Done")
