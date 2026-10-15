import urllib.request
import json
import base64

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

# 1. Load current menu data
with open('current_menu_data.json') as f:
    menu = json.load(f)

# 2. Fetch page 564
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/564?context=edit', headers={'Authorization': auth})
with urllib.request.urlopen(req) as resp:
    page = json.load(resp)

edata = json.loads(page['meta']['_elementor_data'])
root = edata[0]

grid_ids = {
    'lunes': '12dc898b',
    'martes': '4bf72f7d',
    'miercoles': '5bfd1736',
    'jueves': '2fd6c6a9',
    'viernes': '62f9bc94',
    'sabado': '74741324'
}

bag_html = '<img src="https://eatgopty.com/wp-content/uploads/2026/09/bag.svg" width="20" height="20" alt="bag" style="vertical-align: middle; stroke: #000000; fill: none; margin-right: 8px; display: inline-block;">'

# 3. Update each grid's 3 cards
for el in root.get('elements', []):
    eid = el.get('id')
    day_match = None
    for day, gid in grid_ids.items():
        if eid == gid:
            day_match = day
            break
    
    if not day_match or day_match not in menu['dias']:
        continue

    platos = menu['dias'][day_match]['platos']
    cards = el.get('elements', [])
    print(f'Updating grid for {day_match.upper()} with {len(platos)} dishes...')

    for idx, card in enumerate(cards):
        if idx >= len(platos):
            break
        p = platos[idx]
        secs = card.get('elements', [])
        if len(secs) < 2:
            continue
        
        cover = secs[0]
        body = secs[1]

        # In Cover:
        # Widget 0: e-image
        # Widget 1: bcat (PLATO ESTRELLA)
        # Widget 2: bpr (Price)
        for w in cover.get('elements', []):
            wtype = w.get('widgetType')
            title = w.get('editor_settings', {}).get('title', '')
            s = w.setdefault('settings', {})

            if wtype == 'e-image' or 'img' in title:
                if p.get('image_url'):
                    s['image'] = {
                        '$$type': 'image',
                        'value': {
                            'src': {'$$type': 'image-src', 'value': {'url': p['image_url']}},
                            'size': {'$$type': 'string', 'value': 'full'}
                        }
                    }
            elif 'bcat' in title:
                s['paragraph'] = {'$$type': 'escaped-html', 'value': 'PLATO ESTRELLA'}
            elif 'bpr' in title:
                s['paragraph'] = {'$$type': 'escaped-html', 'value': p['price']}
            elif 'bbox' in title:
                s['paragraph'] = {'$$type': 'escaped-html', 'value': ''}

        # In Body:
        # Widget 0: ttl (Title)
        # Widget 1: dsc (Desc)
        # Widget 2: slbl (Acompañamiento a tu gusto:)
        # Widget 3: sbox (Arroz Blanco Criollo ⌵)
        # Widget 4: btn (+ Agregar al Pedido)
        for w in body.get('elements', []):
            wtype = w.get('widgetType')
            title = w.get('editor_settings', {}).get('title', '')
            s = w.setdefault('settings', {})

            if wtype == 'e-heading' or 'ttl' in title:
                s['title'] = {'$$type': 'escaped-html', 'value': p['name']}
            elif 'dsc' in title:
                s['paragraph'] = {'$$type': 'escaped-html', 'value': p['description']}
            elif 'slbl' in title:
                s['paragraph'] = {'$$type': 'escaped-html', 'value': 'Acompañamiento a tu gusto:'}
            elif 'sbox' in title:
                s['paragraph'] = {'$$type': 'escaped-html', 'value': '<span>Arroz Blanco Criollo ⌵</span>'}
            elif 'btn' in title:
                btn_link = f'<a href="#" class="woosq-btn" data-id="{p["id"]}">{bag_html}+ Agregar al Pedido</a>'
                s['paragraph'] = {'$$type': 'escaped-html', 'value': btn_link}

# 4. Save updated _elementor_data
payload = {'meta': {'_elementor_data': json.dumps(edata)}}
req_save = urllib.request.Request(
    'https://eatgopty.com/wp-json/wp/v2/pages/564',
    headers={
        'Authorization': auth,
        'Content-Type': 'application/json'
    },
    data=json.dumps(payload).encode('utf-8')
)

with urllib.request.urlopen(req_save) as resp_save:
    print('Page 564 _elementor_data saved successfully! Code:', resp_save.getcode())
