import feedparser

feed = feedparser.parse(
    "https://feeds.bbci.co.uk/news/rss.xml"
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
