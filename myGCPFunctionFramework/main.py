# def myFirstFunction(requests):
#     request_args = requests.args

#     if request_args and "name" in request_args:
#         name = request_args['name']
#     else:
#         name = "NoName"
#     return f"Hi {name}, welcome to GCP Function Framework, to run it from local."


def myFirstFunction(requests):
    request_args = requests.args
    request_json = requests.get_json(silent = True)

    if request_args and "name" in request_args and 'msg' in request_args:
        name = request_args['name']
        msg = request_args['msg']
    elif request_json and "name" in request_json and 'msg' in request_json:
        name = request_args['name']
        msg = request_args['msg']
    else:
        name = "NoName"
        msg = "NoMessage"
    return f"Hi {name}, welcome to GCP Function Framework, to run it from local. Your comments : {msg}"
