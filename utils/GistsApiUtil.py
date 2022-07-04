import sys

import requests
from utils.Configurations import *
from resources.ApiResources import *


def initiate_session(token):
    session = requests.session()
    if len(token):
        session.auth = auth = (get_user(), token )
        return session
    else:
        session.auth = auth = (get_user(), get_token() )
        return session


def initiate_invalid_session():
    session = requests.session()
    session.auth = auth = ("donrifadsd", get_invalid_token())
    return session


# create request
def send_create_gists_request(session, pay_load):
    url = get_config()['API']['endPoint'] + ApiResources.createGists
    print("... sending POST request to ...." + url)
    headers = {"Content-Type": "application/vnd.github+json"}
    try:
        response = session.post(url, json=pay_load, allow_redirects=False, timeout=10, headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    print(response.status_code)
    if response.status_code == 201:
        gist_id = response.json()['id']
        print('successfully created gist with id ' + gist_id)
        return response, gist_id
    return response, 0


# Get Request
def send_get_gists_request(session, gist_id):
    url = get_config()['API']['endPoint'] + ApiResources.createGists+"/"+gist_id
    print("... sending GET request to ...." + url)

    get_response = session.get(url, json={"gist_id": gist_id}, allow_redirects=False, timeout=3)
    print(get_response.status_code)
    return get_response


# update Request
def send_update_request(session, gist_id, pay_load):
    url = get_config()['API']['endPoint'] + ApiResources.createGists + "/" + gist_id
    print("... sending PUT request to ...." + url)

    try:
        update_response = session.patch(url,
                                        json=pay_load,
                                        allow_redirects=False, timeout=3)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    print(update_response.status_code)
    return update_response


# delete requests
def send_delete_request(session, gist_id):
    url = get_config()['API']['endPoint'] + ApiResources.createGists + "/" + gist_id
    print("... sending DELETE request to ...." + url)

    try:
        delete_response = session.delete(url, json={"gist_id": gist_id},
                                         allow_redirects=False, timeout=3)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    print(delete_response.status_code)
    return delete_response


# get the user list
def send_get_gists_list_request(session, gist_user_id):
    url = get_config()['API']['endPoint'] + "users/" + gist_user_id + "/gists"
    print("... sending GET request to ...." + url)
    try:
        response = session.get(url, json={"username": gist_user_id}, allow_redirects=False, timeout=3)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    print(response.status_code)
    return response
