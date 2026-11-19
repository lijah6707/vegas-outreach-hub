import json, re, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

QUERIES = [
 'Las Vegas Juneteenth festival parade 2027',
 'Las Vegas Black History Month events 2027',
 'Las Vegas Martin Luther King parade 2027',
 'Las Vegas Hispanic Heritage festival 2027',
 'Las Vegas Mexican Independence festival parade 2027',
 'Las Vegas Dia de los Muertos festival 2027',
 'Las Vegas Native American powwow 2027',
 'Nevada Indigenous Peoples Day event 2027',
 'Las Vegas Native American Heritage Month 2027',
 'Henderson North Las Vegas cultural festival vendor application 2027',
]
# RSS articles are leads only; no event dates, booth permission, or organizer approval are inferred.
leads = {}
for query in QUERIES:
    url = 'https://news.google.com/rss/search?' + urllib.parse.urlencode({'q':query,'hl':'en-US','gl':'US','ceid':'US:en'})
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 VegasOutreachHub/1.0'})
        with urllib.request.urlopen(req,timeout=20) as response:
            root=ET.fromstring(response.read())
        for item in root.findall('./channel/item')[:12]:
            title=(item.findtext('title') or '').strip()
            link=(item.findtext('link') or '').strip()
            if not title or not link: continue
            category=('Native American / Indigenous' if re.search(r'native american|indigenous|powwow|tribal',query,re.I) else 'Black / African American' if re.search(r'juneteenth|black history|martin luther',query,re.I) else 'Hispanic / Latino' if re.search(r'hispanic|mexican|muertos',query,re.I) else 'Multicultural')
            key=title.lower()
            if key not in leads: leads[key]={'title':title,'url':link,'category':category,'search':query,'published':item.findtext('pubDate') or ''}
    except Exception as ex:
        print('Feed unavailable:',query,str(ex))
output={'updated':datetime.now(timezone.utc).isoformat(),'note':'These are web search leads, not verified event listings or approved outreach opportunities.','leads':list(leads.values())[:120]}
Path(__file__).with_name('discovered-events.json').write_text(json.dumps(output,indent=2,ensure_ascii=False),encoding='utf-8')
print('Saved',len(output['leads']),'discovery leads')
