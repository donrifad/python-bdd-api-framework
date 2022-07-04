from utils.GistsApiUtil import send_delete_request


def before_scenario(context, scenario):
    print("......starting....... "+scenario.name)


def after_scenario(context, scenario):

    if "add" in scenario.tags:
        print("......cleaning ....... " + scenario.name)
        context.response = send_delete_request(context.session, context.gist_id)
        context.global_id = context.gist_id
        if context.response.status_code == 204:
            print("Successfully deleted " + context.gist_id)
        else:
            print("Issue in deleting " + context.gist_id)
