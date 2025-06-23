def func(message):
    def get_message(message):
        print('Got a message: {}'.format(message))
    return get_message(message)

func('hello world')

