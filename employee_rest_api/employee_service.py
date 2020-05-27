from employee_dao import DAO


class Service:
    def __init__(self):
        self.dao = DAO()

    def test(self):
        self.dao.print_data()

    def get_all_employees(self):
        return self.dao.get_all_employees()

    def get_employee(self, emp_id):
        return self.dao.get_employee(emp_id)

    def add_employee(self, emp):
        id = self.dao.add_employee(emp)
        return_copy = emp.copy()
        return_copy["id"] = id
        return return_copy

    def update_employee(self, emp_id, emp):
        emp_id = self.dao.update_employee(emp_id, emp)
        return_copy = emp.copy()
        return_copy["id"] = emp_id
        return return_copy

    def delete_employee(self, emp_id):
        resp = self.dao.delete_employee(emp_id)


if __name__ == "__main__":
    service = Service()
    service.test()
