from behave import *
from utils.GistsApiUtil import *
from resources.Payloads import *


@given('I have github auth credentials')
def step_impl(context):
    token = ""
    try:
        token = context.config.userdata['token']
    except:
        print("taking the token from property file")
    context.session = initiate_session(token)


@given('I have the details with {description} and {filename} and {public} and {content}')
def step_impl(context, description, filename, public, content):
    context.payLoad = get_create_gists_payload(description, public, filename, content)


@when('I execute the CREATE gists api')
def step_impl(context):
    context.response, context.gist_id = send_create_gists_request(context.session, context.payLoad)


@then('Gists is successfully added with {description} and {file_name} and {public} and {content}')
def step_impl(context, description, file_name, public, content):
    assert context.response.json()['files'][file_name]['filename'] == file_name, 'file name should be' + file_name
    assert context.response.json()['files'][file_name]['content'] == content, 'content  name should be' + content
    assert context.response.json()['description'] == description, 'description name should be' + description


@then('I see the status code of {statuscode:d}')
def step_impl(context, statuscode):
    assert context.response.status_code == statuscode, context.response.status_code


@given('I have the update details with {update_description} and {update_filename} and {update_public} and '
       '{update_content}')
def step_impl(context, update_description, update_filename, update_public, update_content):
    update_description = update_description + "update"
    update_filename = update_filename + "update"
    update_content = update_content + "update"
    context.update_payload = get_gists_update_payload_one(context.gist_id, update_description, update_filename,
                                                          update_content)


@when('I execute the UPDATE gists Api')
def step_impl(context):
    context.response = send_update_request(context.session, context.gist_id, context.update_payload)


@when('I execute the Delete gists Api')
def step_impl(context):
    context.response = send_delete_request(context.session, context.gist_id)


@when('I execute the GET gists api with GistS ID {gists_id}')
def step_impl(context, gists_id):
    context.response = send_get_gists_request(context.session, gists_id)


@then('I see the requested Gists ID {gists_id}')
def step_impl(context, gists_id):
    assert context.response.json()['id'] == gists_id, "User should have the id " + gists_id


@when('I execute the UPDATE gists api with Gists ID {gists_id}')
def step_impl(context, gists_id):
    context.response = send_update_request(context.session, gists_id, context.update_payload)


@given('I have the gists update details with gistsID  {update_description} and {update_filename} and {update_public} '
       'and {update_content} and {gist_id}')
def step_impl(context, update_description, update_filename, update_public, update_content, gist_id):
    update_description = update_description + "update"
    update_filename = update_filename + "update"
    update_content = update_content + "update"
    context.update_payload = get_gists_update_payload_one(gist_id, update_description, update_filename,
                                                          update_content)


@when('I execute the GETLIST api with {user_id}')
def step_impl(context, user_id):
    context.response = send_get_gists_list_request(context.session, user_id)


@then('I see the following Gist IDS {gist_id_list}')
def step_impl(context, gist_id_list):
    gist_id_list = gist_id_list.split(",")
    cnt = verify_id_list(gist_id_list, context.response)
    assert len(gist_id_list) == cnt, "All id's should be available"


def verify_id_list(gist_id_list, response):
    cnt = 0
    for gists_id in gist_id_list:
        print("...checking..." + gists_id)
        for item in response.json():
            if gists_id == item['id']:
                cnt = cnt + 1
    return cnt


@given("I have invalid github auth credentials")
def step_impl(context):
    context.session = initiate_invalid_session()


@given('I take a gists id for user {user_id}')
def step_impl(context, user_id):
    context.response = send_get_gists_list_request(context.session, user_id)
    context.gist_id_from_list = context.response.json()[0]['id']


@when('I execute the GET gists api with GistS ID')
def step_impl(context):
    context.response = send_get_gists_request(context.session, context.gist_id_from_list)


@then('I see the requested Gists ID')
def step_impl(context):
    assert context.response.json()[
               'id'] == context.gist_id_from_list, "User should have the id " + context.gist_id_from_list


@given('I have the gists update details with gistsID  {update_description} and {update_filename} and {update_public} '
       'and {update_content}')
def step_impl(context, update_description, update_filename, update_public, update_content):
    update_description = update_description + "update"
    update_filename = update_filename + "update"
    update_content = update_content + "update"
    context.update_payload = get_gists_update_payload_one(context.gist_id_from_list, update_description,
                                                          update_filename,
                                                          update_content)


@when('I execute the UPDATE gists api with Gists ID')
def step_impl(context):
    context.response = send_update_request(context.session, context.gist_id_from_list, context.update_payload)
