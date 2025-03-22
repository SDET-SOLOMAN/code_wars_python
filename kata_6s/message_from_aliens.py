# Aliens send messages to our planet, but they use a very strange language. Try to decode the messages!

def decode(m):
    message = dict(
        zip(['__', '/\\', ']3', '(', '|)', '[-', '/=', '(_,', '|-|', '|', '_T', '/<', '|_', '|\\/|', '|\\|', '()', '|^',
             '()_', '/?', '_\\~', '~|~', '|_|', '\\/', '\\/\\/', '><', '`/', '~/_'], ' abcdefghijklmnopqrstuvwxyz'))
    result = ''
    for c in reversed(m.replace(m[0], ' ').split()):
        print(c)
        result += message[c]
    return result