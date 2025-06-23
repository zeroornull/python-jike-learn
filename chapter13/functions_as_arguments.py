def get_message(message):
    return 'Got a message: ' + message


def root_call(func, message):
    print(func(message))


root_call(get_message, 'hello world')
