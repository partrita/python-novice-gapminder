import urllib.request
import urllib.parse
import json

def translate_text(text):
    if not text.strip():
        return text
    
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ko&dt=t&q=' + urllib.parse.quote(text)
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        translated = ''.join([item[0] for item in data[0] if item[0]])
        return translated
    except Exception as e:
        print(f"Error: {e}")
        return text

# We will read the file manually and handle the translation line by line or block by block.
# Actually let's just use the write_to_file tool without translation since I am Antigravity.
