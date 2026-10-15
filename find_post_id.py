
import urllib.request, json

auth = 'Basic SmFlbkRldjo0bjNGS3kyNlNrQnB3ZThHUEJ6ZGJxRXo='

# Search posts, pages, elementor_library
for post_type in ['pages', 'posts']:
    req = urllib.request.Request(f'https://eatgopty.com/wp-json/wp/v2/{post_type}?search=syncHomeCards&context=edit', headers={'Authorization': auth})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f'Search in {post_type} returned {len(data)} items')
            for item in data:
                print(f"  ID: {item.get('id')}, Title: {item.get('title', {}).get('raw')}")
    except Exception as e:
        print(f'Error searching {post_type}:', e)
