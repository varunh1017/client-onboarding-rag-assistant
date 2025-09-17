import random 
from faker import Faker 

fake = Faker(locale="en_GB")

def generate_employee_data(num_records=1):
    """Generate fake employee data."""
    designations = ["Software Engineer", "Product Manager", "Data Analyst", "HR Executive", "Sales Lead"]
    departments = ["Engineering", "Product", "Data", "Human Resources", "Sales"] 
    
    employees = []
    for _ in range(num_records): 
        employee = {
            "name": fake.name(), 
            "employee_id": f"EMP{random.randint(1000, 9999)}", 
            "designation": random.choice(designations),
            "department": random.choice(departments),
        }
        employees.append(employee)
    return employees

