import base64
import requests
import json

# GETTING LATEST VERSION FROM GITHUB
url = 'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
owner = 'zaladevdeep'
repo = 'website-deploy'
path = 'next.py'
params = {'ref': 'main'}

# Send the GET request to retrieve the file content
response = requests.get(url.format(owner=owner, repo=repo, path=path), params=params)
content = json.loads(response.content)

# Decode the base64-encoded content of the file
file_content = base64.b64decode(content['content']).decode('utf-8')
print(file_content)