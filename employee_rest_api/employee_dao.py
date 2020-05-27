import json

# Sample initial db values, can be dumped into the JSON file for initialization
_emp_db_init = {
    101: {
        'name': 'Saravanan S',
        'title': 'Technical Leader'
    },
    102: {
        'name': 'Rajkumar P',
        'title': 'Sr Software Engineer'
    }
}


class DAO:
    """
    Employee DAO class defining data access logic for the employee data.
    """

    def __init__(self):
        self._emp_db = {}
        self._load_data()

    def _load_data(self):
        """
        Loads employee data from the employee.json file
        """
        try:
            json_file = open("employees.json", 'r')
            self._emp_db = json.load(json_file)
        except Exception as e:
            print("issue loading data!", e)
        finally:
            json_file.close()

    def _dump_data(self):
        """
        Dumps employee data onto the employee.json file
        """
        try:
            json_file = open("employees.json", "w")
            json.dump(self._emp_db, json_file)
            print("written to file")
        except Exception as e:
            print("Error dumping data into the file!", e)
        finally:
            json_file.close()

    def print_data(self):
        print(self._emp_db)

    def get_all_employees(self):
        try:
            return self._emp_db
        except Exception as e:
            return {"Error": "Cannot retrieve the data!"}

    def get_employee(self, emp_id):
        try:
            emp = self._emp_db[emp_id].copy()
            emp["id"] = emp_id
            return emp
        except Exception as e:
            return {"Error": "Cannot retrieve the data!"}

    def add_employee(self, new_emp):
        new_id = 0
        try:
            new_id = max([int(id) for id in self._emp_db.keys()]) + 1
            self._emp_db[str(new_id + 1)] = new_emp
            self._dump_data()
        except Exception as e:
            print(e)
        return new_id

    def update_employee(self, emp_id, emp_update):
        if emp_id in self._emp_db.keys():
            self._emp_db[emp_id] = emp_update
            self._dump_data()
            return emp_id
        else:
            return 0

    def delete_employee(self, emp_id):
        if emp_id in self._emp_db.keys():
            resp = self._emp_db[emp_id]
            del self._emp_db[emp_id]
            self._dump_data()
            return resp
        else:
            return {"Error": "Employee not found!"}


if __name__ == "__main__":
    employee_dao = DAO()
    employee_dao.print_data()
    emp = employee_dao._emp_db['101'].copy()
    emp["id"] = 101
    print(emp)
