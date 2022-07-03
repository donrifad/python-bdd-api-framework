import requests
from utils.Configurations import *
from resources.ApiResources import *
from resources.Payloads import *

config = get_config()
session = requests.session()
session.auth = auth = ("donrifad", get_password())

url = config['API']['endPoint'] + ApiResources.createGists
headers = {"Content-Type": "application/vnd.github+json"}

response = session.post(url, json=get_create_gists_payload("Example of a gist", "false", "README10.md", "HELLOWORLD3"),
                        allow_redirects=False, timeout=1)
gist_id = response.json()['id']
print(response.status_code)
print(response.json())
print(gist_id)

# Get Request
response2 = session.get(url, json={"gist_id": gist_id}, allow_redirects=False, timeout=3)
print(response2.json())
print(response2.status_code)

# update Request
url = config['API']['endPoint'] + ApiResources.createGists + "/" + gist_id

response3 = session.patch(url, json=get_gists_update_payload_one(gist_id, "Update gists", "README13.md", "Update file "
                                                                                                         "content"),
                          allow_redirects=False, timeout=3)
print(response3.json())
print(response3.status_code)

# delete requests
# update Request
url = config['API']['endPoint'] + ApiResources.createGists + "/" + gist_id

response4 = session.delete(url, json={"gist_id": gist_id},
                           allow_redirects=False, timeout=3)
print(response4.status_code)
