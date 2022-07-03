import requests
from utils.Configurations import *
from resources.ApiResources import *
from resources.Payloads import *


def initiate_session():
    session = requests.session()
    session.auth = auth = ("donrifad", get_password())
    return session


def send_create_gists_request(session, pay_load):
    url = get_config()['API']['endPoint'] + ApiResources.createGists
    headers = {"Content-Type": "application/vnd.github+json"}
    response = session.post(url, json=pay_load, allow_redirects=False, timeout=10, headers=headers)
    gist_id = response.json()['id']
    print(response.status_code)
    print(response.json())
    return response, gist_id


def send_get_gists_request(session, gist_id):
    # Get Request
    url = get_config()['API']['endPoint'] + ApiResources.createGists
    get_response = session.get(url, json={"gist_id": gist_id}, allow_redirects=False, timeout=3)
    print(get_response.json())
    print(get_response.status_code)
    return get_response


def send_update_request(session, gist_id, config):
    # update Request
    url = get_config()['API']['endPoint'] + ApiResources.createGists + "/" + gist_id

    update_response = session.patch(url,
                                    json=get_gists_update_payload_one(gist_id, "Update gists", "README13.md",
                                                                      "Update file "
                                                                      "content"),
                                    allow_redirects=False, timeout=3)
    print(update_response.json())
    print(update_response.status_code)
    return update_response


def send_delete_request(session, gist_id, config):
    # delete requests
    url = config['API']['endPoint'] + ApiResources.createGists + "/" + gist_id

    delete_response = session.delete(url, json={"gist_id": gist_id},
                               allow_redirects=False, timeout=3)
    print(delete_response.status_code)
    return delete_response
