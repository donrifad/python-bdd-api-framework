def get_create_gists_payload(description, public, file_name, content):
    body = {
        "description": description,
        "public": public,
        "files": {
            file_name: {
                "content": content
            }
        }
    }
    return body


def get_gists_update_payload_one(gist_id, description, file_name, content):
    body = {
        "gist_id": gist_id,
        "description": description,
        "files": {
            file_name: {
                "content": content
            }
        }
    }
    return body


def get_gists_update_payload_two(gist_id, description, file_name):
    body = {
        "gist_id": gist_id,
        "description": description,
        "files": {
            file_name: {
                "content": "hello world update"
            }
        }
    }
    return body
