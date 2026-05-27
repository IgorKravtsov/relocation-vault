import urllib.request, re

urls = [
    ('Lisbon', 'https://en.wikipedia.org/wiki/Climate_of_Lisbon'),
    ('Porto', 'https://en.wikipedia.org/wiki/Climate_of_Porto'),
    ('Malta', 'https://en.wikipedia.org/wiki/Climate_of_Malta'),
]

for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8')
        m = re.search(r'Percentage.*?possible sunshine.*?</th>(.*?)</tr>', html, re.DOTALL | re.IGNORECASE)
        if m:
            cells = re.findall(r'>(\d+)<', m.group(1))
            if cells:
                print(f'{name}: {cells[-1]}%')
            else:
                print(f'{name}: row found, no numbers')
        else:
            print(f'{name}: no data')
    except Exception as e:
        print(f'{name}: error {e}')
