from random import randint
import json
from random_dict import random_string_dict


class Generator:

    def __init__(self):
        self._url_string = "http://localhost:5000/json_gen/file/{}"
        self._file_string = "file_{}"
        self.file_list = [self._file_string.format(i) for i in range(1, randint(1000, 1100))]

    def generate_urls(self):
        return [self._url_string.format(i) for i in self.file_list]

    def generate_random_dict(self, file_name):
        if file_name in self.file_list:
            return "{}.json\n{}".format(file_name, json.dumps(random_string_dict(randint(0, 1), randint(1, 2))))
        else:
            return "file not found"


if __name__ == "__main__":
    gen = Generator()
    print(gen.file_list)
    print(gen.generate_random_dict("file_1"))
