from flask import Flask
from flask import Response
from flask import render_template
from flask import request
from flask import jsonify
from flask import session

from employee_service import Service


app = Flask(__name__, template_folder="app_ui")

service = Service()


@app.route("/")
def main():
    return Response(render_template("index.html"))


@app.route("/app/employee", methods=["GET"])
def get_all_employee():
    return jsonify(service.get_all_employees())


# URL Param

@app.route("/app/employee/<emp_id>", methods=["GET"])
def get_employee(emp_id):
    return jsonify(service.get_employee(emp_id))


# Getting request data through flask.request module :

# request.args: the key/value pairs in the URL query string
# request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
# request.files: the files in the body, which Flask keeps separate from form. HTML forms must
# use enctype=multipart/form-data or files will not be uploaded.
# request.values: combined args and form, preferring args if keys overlap
# request.json: parsed JSON data. The request must have the application/json content type,
# or use request.get_json(force=True) to ignore the content type.

# All of these are MultiDict instances (except for json).
# (https://werkzeug.palletsprojects.com/en/1.0.x/datastructures/#werkzeug.datastructures.MultiDict)

@app.route("/app/employee", methods=["POST"])
def add_employee():
    emp = {
        "name": request.form.get("name"),
        "title": request.form.get("title")
    }
    return jsonify(service.add_employee(emp))


@app.route("/app/employee/<emp_id>", methods=["PUT"])
def update_employee(emp_id):
    emp = {
        "name": request.form.get("name"),
        "title": request.form.get("title")
    }
    return jsonify(service.update_employee(emp_id, emp))


@app.route("/app/employee/<emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    return jsonify(service.delete_employee(emp_id))


if __name__ == "__main__":
    app.run()
