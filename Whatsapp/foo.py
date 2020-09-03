def get_last_timestamp():
    with open('log.txt') as f:
        last_line = f.readlines()
    return last_line


