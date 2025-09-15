import random 
from faker import Faker 

def generate_employee_data():
        """Generate fake employee data."""
    designations = ["Software Engineer", "Product Manager", "Data Analyst", "HR Executive", "Sales Lead"]
    departments = ["Engineering", "Product", "Data", "Human Resources", "Sales"] 
    
    employees = []
    for _ in range(num_records): 
        employee = {
            "name": faker.name(), 
            "employee_id": f"EMP{random.randint(1000, 9999)}", 
            "designation": random.choice(designations),
            "department": random.choice(departments),
        }
        employees.append(employee)
    return employees

    