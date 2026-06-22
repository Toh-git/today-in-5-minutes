import feedparser
weblist =(
    {'url': "https://feeds.bbci.co.uk/news/rss.xml", "name":"BBC"},
    {'url': 'https://www.thairath.co.th/rss/news', 'name': 'ไทยรัฐ'},
    {'url': 'http://rssfeeds.sanook.com/rss/feeds/sanook/news.index.xml', 'name': 'สนุกดอทคอม'},
    {'url': 'https://news.thaipbs.or.th/rss/news', 'name': 'thaipbs'},
    {'url': 'https://www.prachachat.net/feed', 'name': 'ประชาชาติ'},
    {'url': 'https://feeds.feedburner.com/prachatai', 'name': 'ประชาไทย'},
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
    name = web["name"]
    feed = feedparser.parse(url)
    print("Running:", name, " ...")
    # เพิ่มหัวข้อชื่อเว็บ เพื่อให้ดูง่ายขึ้นว่าข่าวมาจากไหน
    html += f"<h3>📰 {name}</h3>" 
    
    # ย่อหน้า (Indent) ลูปนี้เข้ามาอยู่ข้างในลูปหลัก
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
print("Writing output file...")
with open("index.html", "w", encoding="utf8") as f:
    f.write(html)

print("Done")
