from flask import jsonify
from data_generator import Generator


class Service:
    def __init__(self):
        self.generator = Generator()

    def get_urls(self):
        return self.generator.generate_urls()

    def get_file(self,file_name):
        return self.generator.generate_random_dict(file_name)