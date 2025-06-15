# Implement an object-oriented solution for managing employees in a company, use appropriate classes and inheritance, and incorporate Dunder methods. 

# Instructions: 
# Implement the Employee class with basic attributes (name, id, department). 
# Implement a Manager class that inherits from Employee. 
# Implement Developer class that inherits from Employee. 
# Use Dunder methods for a meaningful representation of objects. 
# Implement specialized classes like HRManager, PythonDeveloper, and DataScientist. 
# Use an Enumeration for the department. 
# Demonstrate inheritance and relationships between classes. 

from enum import Enum, auto

class Department(Enum):
    HR = auto()
    Development = auto()
    Management = auto()
    Data_science = auto()

class Employee:
    def __init__(self, name: str, emp_id: int, department: Department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def __str__(self):
        return f"[Employee] Name: {self.name}, ID: {self.emp_id}, Department: {self.department.name}"

    def __repr__(self):
        return f"Employee('{self.name}', {self.emp_id}, Department.{self.department.name})"

class Manager(Employee):
    def __init__(self, name: str, emp_id: int, department: Department, Team_size : int):
        super().__init__(name, emp_id, department)
        self.Team_size = Team_size

    def __str__(self):
        return f"[Manager] {super().__str__()}, Team Size: {self.Team_size}"

class Developer(Employee):
    def __init__(self, name: str, emp_id: int, department: Department, programming_language: str):
        super().__init__(name, emp_id, department)  
        self.programming_language = programming_language  

    def __str__(self):
        return f"[Developer] {super().__str__()}, Programming Language: {self.programming_language}"

class HRManager(Manager):
    def __init__(self, name: str, emp_id: int, team_size: int):
        super().__init__(name, emp_id, Department.HR, team_size)

    def __str__(self):
        return f"[HRManager] {super().__str__()}"


class PythonDeveloper(Developer):
    def __init__(self, name: str, emp_id: int):
        super().__init__(name, emp_id, Department.Development, "Python")

    def __str__(self) -> str:
        return f"[PythonDeveloper] {super().__str__()}"

class DataScientist(Developer):
    def __init__(self, name: str, emp_id: int):
        super().__init__(name, emp_id, Department.Data_science, "Python, SQL, ML")

    def __str__(self) -> str:
        return f"[DataScientist] {super().__str__()}"


emp = Employee("Chirag Jaiswal", 101, Department.Management)
manager = Manager("Dean Winchester", 102, Department.Management, 5)
hr = HRManager("Alina Brown", 103, 3)
dev = Developer("Lalit Yogi", 104, Department.Development, "Java")
py_dev = PythonDeveloper("Ravi Kumar", 105)
ds = DataScientist("Anjali Sharma", 106)

employees = [emp, manager, hr, dev, py_dev, ds]

for e in employees:
    print(e)
