def write_data_to_file(filename, txt):
    try:
        with open(filename, 'a+') as f:
            f.write(txt)
            f.close()
    except Exception as e:
        print(e)


def get_last_timestamp():
    with open('log.txt') as f:
        last_timestamp = f.read()
    return last_timestamp
