import json
import datetime
import hashlib


def write_file_func(data, path):
    with open(path, "w", encoding="utf-8") as write_file:
        json.dump(data, write_file)


def decorator(old_function):
    def new_function(**params):
        new_param = old_function(params['param'])
        data = {
            'Date': str(datetime.datetime.now()),
            'Function name': old_function.__name__,
            'Old params': params['param'],
            'New params': new_param
        }
        write_file_func(data, params["path"])
        return new_param

    return new_function


@decorator
def get_hash_string(file):
    def generator(file):
        with open(file, "r") as f:
            for line in f:
                hash_str = hashlib.md5(f.readline().strip().encode())
                yield hash_str.hexdigest()

    return [hash_string for hash_string in generator(file)]


get_hash_string(param='countries.json', path='data.json')




