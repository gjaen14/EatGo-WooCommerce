import json
import urllib.request
import base64
import copy

username = 'JaenDev'
password = '4n3FKy26SkBpwe8GPBzdbqEz'
auth_header = 'Basic ' + base64.b64encode(f'{username}:{password}'.encode()).decode()

bag_icon_html = '<img src="https://eatgopty.com/wp-content/uploads/2026/09/bag.svg" width="20" height="20" alt="bag" style="vertical-align: middle; margin-right: 8px; display: inline-block;">'

# Fetch current page 564
req = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/564?context=edit', headers={'Authorization': auth_header})
with urllib.request.urlopen(req) as resp:
    page = json.load(resp)
    edata = json.loads(page['meta']['_elementor_data'])

# Find grid-martes
grid_martes = None
for el in edata[0]['elements']:
    if el.get('id') == '5c59ff09':
        grid_martes = el
        break

if not grid_martes:
    raise Exception('grid-martes not found!')

# Martes Products data from reference image
martes_products = [
    {
        'title': 'Pernil al horno a la naranja',
        'price': '$5.75',
        'desc': 'Delicioso plato tradicional panameño preparado al momento.',
        'img_id': 618,
        'prod_id': 615,
        'tag': 'PLATO ESTRELLA'
    },
    {
        'title': 'Carne guisada a la jardinera',
        'price': '$5.50',
        'desc': 'Delicioso plato tradicional panameño preparado al momento.',
        'img_id': 613,
        'prod_id': 608,
        'tag': 'PLATO ESTRELLA'
    },
    {
        'title': 'Mondongo a la culona',
        'price': '$5.00',
        'desc': 'Delicioso plato tradicional panameño preparado al momento.',
        'img_id': 606,
        'prod_id': 593,
        'tag': 'PLATO ESTRELLA'
    }
]

# Update Martes cards
for i, card in enumerate(grid_martes['elements']):
    pinfo = martes_products[i]
    for section in card.get('elements', []):
        for widget in section.get('elements', []):
            cid = widget.get('id')
            wtype = widget.get('widgetType')
            s = widget.setdefault('settings', {})
            
            # Image
            if wtype == 'e-image':
                s['image'] = {
                    '$$type': 'image',
                    'value': {
                        'src': {'$$type': 'image-src', 'value': {'id': {'$$type': 'image-attachment-id', 'value': pinfo['img_id']}}},
                        'size': {'$$type': 'string', 'value': 'full'}
                    }
                }
            # Category Badge
            elif 'bcat' in str(widget.get('title', '')) or cid == '7b81b789' or cid == '2457d7c2' or cid == 'b8bd5b8':
                s['paragraph'] = {'$$type': 'escaped-html', 'value': pinfo['tag']}
            # Price Badge
            elif 'bpr' in str(widget.get('title', '')) or cid == '2a4c599c' or cid == '20bfda4e' or cid == '6b7069e6':
                s['paragraph'] = {'$$type': 'escaped-html', 'value': pinfo['price']}
            # Hide box badge (Ver en Caja 75°C)
            elif 'bbox' in str(widget.get('title', '')) or cid in ['7a466aab', '217a4710', '25a756bf']:
                s['paragraph'] = {'$$type': 'escaped-html', 'value': ''}
            # Title
            elif wtype == 'e-heading':
                s['title'] = {'$$type': 'escaped-html', 'value': pinfo['title']}
            # Description
            elif 'dsc' in str(widget.get('title', '')) or cid in ['14cebdf8', '2bf8a073', '5124e6b1']:
                s['paragraph'] = {'$$type': 'escaped-html', 'value': pinfo['desc']}
            # Side Label
            elif 'slbl' in str(widget.get('title', '')) or cid in ['1c579cb4', '4c7c908f', '5998a376']:
                s['paragraph'] = {'$$type': 'escaped-html', 'value': 'Acompañamiento a tu gusto:'}
            # Side Box
            elif 'sbox' in str(widget.get('title', '')) or cid in ['3ff81b66', '63347e33', '181b7a25']:
                s['paragraph'] = {'$$type': 'escaped-html', 'value': '<span>Arroz Blanco Criollo ⌵</span>'}
            # Button
            elif 'btn' in str(widget.get('title', '')) or cid in ['16177b67', '232fe96d', '74eea7f4']:
                btn_link = f'<a href="#" class="woosq-btn" data-id="{pinfo["prod_id"]}">{bag_icon_html}+ Agregar al Pedido</a>'
                s['paragraph'] = {'$$type': 'escaped-html', 'value': btn_link}

print('Martes cards updated successfully!')

# Now prepare Lunes cards by cloning Martes cards structure
lunes_products = [
    {
        'title': 'Sancocho Tradicional de Gallina de Patio',
        'price': '$6.50',
        'desc': 'Delicioso plato tradicional panameño preparado al momento.',
        'img_id': 303,
        'prod_id': 420,
        'tag': 'PLATO ESTRELLA'
    },
    {
        'title': 'Mondongo a la Culantro con Papitas',
        'price': '$5.00',
        'desc': 'Delicioso plato tradicional panameño preparado al momento.',
        'img_id': 607,
        'prod_id': 593,
        'tag': 'PLATO ESTRELLA'
    },
    {
        'title': 'Pollo Guisado Campesino en Achiote',
        'price': '$6.00',
        'desc': 'Delicioso plato tradicional panameño preparado al momento.',
        'img_id': 614,
        'prod_id': 97,
        'tag': 'PLATO ESTRELLA'
    }
]

grid_lunes_cards = []
for i, pinfo in enumerate(lunes_products):
    card = copy.deepcopy(grid_martes['elements'][i])
    card['id'] = f'card-lun-{i+1}'
    for section in card.get('elements', []):
        section['id'] = f'sec-lun-{i+1}-{section.get("id")[-3:]}'
        for widget in section.get('elements', []):
            widget['id'] = f'wid-lun-{i+1}-{widget.get("id")[-3:]}'
            wtype = widget.get('widgetType')
            s = widget.setdefault('settings', {})
            if wtype == 'e-image':
                s['image'] = {
                    '$$type': 'image',
                    'value': {
                        'src': {'$$type': 'image-src', 'value': {'id': {'$$type': 'image-attachment-id', 'value': pinfo['img_id']}}},
                        'size': {'$$type': 'string', 'value': 'full'}
                    }
                }
            elif 'bcat' in str(widget.get('title', '')) or '7b81b789' in str(widget.get('id', '')):
                s['paragraph'] = {'$$type': 'escaped-html', 'value': pinfo['tag']}
            elif 'bpr' in str(widget.get('title', '')) or '2a4c599c' in str(widget.get('id', '')):
                s['paragraph'] = {'$$type': 'escaped-html', 'value': pinfo['price']}
            elif 'bbox' in str(widget.get('title', '')):
                s['paragraph'] = {'$$type': 'escaped-html', 'value': ''}
            elif wtype == 'e-heading':
                s['title'] = {'$$type': 'escaped-html', 'value': pinfo['title']}
            elif 'dsc' in str(widget.get('title', '')):
                s['paragraph'] = {'$$type': 'escaped-html', 'value': pinfo['desc']}
            elif 'slbl' in str(widget.get('title', '')):
                s['paragraph'] = {'$$type': 'escaped-html', 'value': 'Acompañamiento a tu gusto:'}
            elif 'sbox' in str(widget.get('title', '')):
                s['paragraph'] = {'$$type': 'escaped-html', 'value': '<span>Arroz Blanco Criollo ⌵</span>'}
            elif 'btn' in str(widget.get('title', '')):
                btn_link = f'<a href="#" class="woosq-btn" data-id="{pinfo["prod_id"]}">{bag_icon_html}+ Agregar al Pedido</a>'
                s['paragraph'] = {'$$type': 'escaped-html', 'value': btn_link}
    grid_lunes_cards.append(card)

# Put the 3 cards into grid-lunes
for el in edata[0]['elements']:
    if el.get('id') == '69a6b14f':
        el['elements'] = grid_lunes_cards
        print('grid-lunes updated with 3 native cards!')

# Clean bbox and update buttons in other grids (miercoles, jueves, viernes, sabado)
for el in edata[0]['elements']:
    gid = el.get('id')
    if gid in ['777795ed', '777c2879', '5b7538c7', '7ed1d723']:
        for card in el.get('elements', []):
            for section in card.get('elements', []):
                for widget in section.get('elements', []):
                    s = widget.setdefault('settings', {})
                    # Clean bbox
                    if 'bbox' in str(widget.get('title', '')):
                        s['paragraph'] = {'$$type': 'escaped-html', 'value': ''}
                    # Clean bcat to PLATO ESTRELLA
                    if 'bcat' in str(widget.get('title', '')):
                        s['paragraph'] = {'$$type': 'escaped-html', 'value': 'PLATO ESTRELLA'}
                    # Ensure sbox
                    if 'sbox' in str(widget.get('title', '')):
                        s['paragraph'] = {'$$type': 'escaped-html', 'value': '<span>Arroz Blanco Criollo ⌵</span>'}
                    # Update button icon
                    if 'btn' in str(widget.get('title', '')):
                        p_val = s.get('paragraph', {}).get('value', '')
                        import re
                        m = re.search(r'data-id="([0-9]+)"', p_val)
                        pid = m.group(1) if m else '420'
                        s['paragraph'] = {'$$type': 'escaped-html', 'value': f'<a href="#" class="woosq-btn" data-id="{pid}">{bag_icon_html}+ Agregar al Pedido</a>'}

print('All other day grids updated cleanly!')

# Save page 564
payload = {'meta': {'_elementor_data': json.dumps(edata)}}
req_post = urllib.request.Request('https://eatgopty.com/wp-json/wp/v2/pages/564', headers={
    'Authorization': auth_header,
    'Content-Type': 'application/json'
}, data=json.dumps(payload).encode('utf-8'))

with urllib.request.urlopen(req_post) as resp_post:
    print('Page 564 updated status:', resp_post.getcode())
