import requests

url = "http://127.0.01:8000/api/post/1/"

headers = {'Authorization': 'Token eb09cfcad34cf8eeb2a1438828c351260169a372'}

r = requests.get(url, headers=headers)

print(r.json())