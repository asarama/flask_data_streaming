import requests

import definitions

url = f"http://localhost:{definitions.port}/stream"
s = requests.Session()
r = s.get(url, stream=True)
for line in r.iter_content(chunk_size=1024):
    if line:
        print(line)