import feedparser
weblist =(
    {'url': "https://feeds.bbci.co.uk/news/rss.xml", "name":"BBC"},
    
    {'url': 'https://www.thansettakij.com/rss/money_market.xml', 'name': 'ฐานเศรษฐกิจ'},
    {'url': 'https://www.khaosod.co.th/feed', 'name': 'ข่าวสด ข่าวล่าสุด'},
    {'url': 'https://bangkok-today.com/feed', 'name': 'Bangkok Today'},
    {'url': 'https://www.matichon.co.th/feed', 'name': 'มติชน'},   
    {'url': 'https://feeds.feedburner.com/prachatai', 'name': 'ประชาไทย'},  
        
    {'url': 'https://www.prachachat.net/feed', 'name': 'ประชาชาติ'},    
    {'url': 'https://www.prachachat.net/economy/feed', 'name': 'ประชาชาติ เศรษฐกิจ'},
    {'url': 'https://www.prachachat.net/marketing/feed', 'name': 'ประชาชาติ การตลาด'},
    {'url': 'https://www.prachachat.net/finance/feed', 'name': 'ประชาชาติ การเงิน'},
    {'url': 'https://www.prachachat.net/property/feed', 'name': 'ประชาชาติ อสังหาฯ'}

    {'url': 'https://mgronline.com/rss/home', 'name': 'MGR Online ข่าวหน้าแรก'},
    {'url': 'https://mgronline.com/rss/politics', 'name': 'MGR Online การเมือง'},
    {'url': 'https://mgronline.com/rss/business', 'name': 'MGR Online เศรษฐกิจ'},
    {'url': 'https://mgronline.com/rss/crime', 'name': 'MGR Online อาชญากรรม'},
    {'url': 'https://mgronline.com/rss/around', 'name': 'MGR Online ข่าวต่างประเทศ'},
    
    {'url': 'http://rssfeeds.sanook.com/rss/feeds/sanook/news.index.xml', 'name': 'สนุกดอทคอม'},
    {'url': 'https://rssfeeds.kapook.com/bulletin', 'name': 'Kapook ข่าวเด่น'},
    {'url': 'https://rssfeeds.kapook.com/money', 'name': 'Kapook เศรษฐกิจ'},
    {'url': 'https://www.car250.com/feed', 'name': 'CAR250 ข่าวยานยนต์'},
    {'url': 'https://www.headlightmag.com/category/news/new-cars-worldwide/feed', 'name': 'Headlightmag ข่าวรถใหม่โลก'},
    {'url': 'https://www.9carthai.com/feed', 'name': '9CarThai ข่าวยานยนต์'},
    
    
    {'url': 'https://www.flashfly.net/wp/feed', 'name': 'Flashfly ข่าวมือถือ'},
    {'url': 'https://droidsans.com/feed', 'name': 'Droidsans ข่าวไอที-มือถือ'},
    
    {'url': 'https://www.thairath.co.th/rss/news', 'name': 'ไทยรัฐ'},
    {'url': 'https://news.thaipbs.or.th/rss/news', 'name': 'Thai PBS ข่าวล่าสุด'},
    {'url': 'https://www.amarintv.com/feed', 'name': 'Amarin TV ข่าวเด่น'},
    {'url': 'https://voicetv.co.th/rss', 'name': 'Voice TV'},
    
    {'url': 'https://www.ryoiireview.com/feed', 'name': 'RyoiiReview รีวิวของกิน'},
    {'url': 'https://www.chillpainai.com/feed', 'name': 'ชิลไปไหน ท่องเที่ยว-คาเฟ่'},
    {'url': 'https://www.mushroomtravel.com/feed', 'name': 'Mushroom Travel'}
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
