#On utilise ici le Composite. On est face à un cas de hiérarchie, c'est donc le design pattern adapté

class Departement:
    def __init__ (self):
        self.employees = []
        self.depts = {}
    
    def get_employees(self):
        return self.employees
    
    def add_employee(self, employee):
        self.employees.append(employee)

    def get_dept(self, nomDpts):
        return self.depts.get(nomDpts, None)
    
    def set_dept(self,name,value):
            self.depts[name] = value


class Employee:
    def __init__(self, first_name, last_name, job):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job


