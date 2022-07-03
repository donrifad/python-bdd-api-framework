from behave import *
from utils.GistsApiUtil import *
from resources.Payloads import *


@given('I have github auth credentials')
def step_impl(context):
    context.session = initiate_session()


@given('I have the details with {description} and {filename} and {public} and {content}')
def step_impl(context, description, filename, public, content):
    context.payLoad = get_create_gists_payload(description, public, filename, content)


@when('I execute the create gists api')
def step_impl(context):
    context.response, context.gist_id = send_create_gists_request(context.session, context.payLoad)


@then('Gists is successfully added with {description} and {file_name} and {public} and {content}')
def step_impl(context, description, file_name, public, content):
    assert context.response.json()['files'][file_name]['filename'] == file_name, 'file name should be' + file_name
    assert context.response.json()['files'][file_name]['content'] == content, 'content  name should be' + content
    assert context.response.json()['description'] == description, 'description name should be' + description


@then('I see the status code of {statuscode:d}')
def step_impl(context, statuscode):
    assert context.response.status_code == statuscode
