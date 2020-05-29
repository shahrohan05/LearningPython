from flask import Flask
from flask import jsonify
from service import Service


app = app = Flask(__name__)


class Controller:
    def __init__(self):
        self.service = Service()

    def get_urls(self):
        return jsonify(self.service.get_urls())

    def get_file(self, file_name):
        return self.service.get_file(file_name)


# This code should perhaps be a part of a separate app.py file.

controller = Controller()


@app.route("/json_gen/urls")
def get_urls():
    return controller.get_urls()

@app.route("/json_gen/file/<file_name>")
def get_file(file_name):
    return controller.get_file(file_name)

if __name__ == "__main__":
    app.run()
