class Employee:
    def __init__(self, employee_id, base_salary):
        self.employee_id = employee_id
        self.base_salary = base_salary
        self.overtime_pay = 0
        self.bonus = 0
        self.total_salary = base_salary

    def calculate_salary(self):
        self.total_salary = self.base_salary + self.overtime_pay + self.bonus

    def add_salary_item(self, name, amount):
        if name == "overtime":
            self.overtime_pay += amount
        elif name == "bonus":
            self.bonus += amount
        else:
            # Handle invalid salary item names
            pass

class SalaryItem:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class SalaryTemplate:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_salary(self):
        # Calculate the total salary based on base salary
        # and any additional bonuses, deductions, etc.
        total_salary = self.base_salary
        
        # Add any bonuses or allowances to the total salary
        total_salary += self.calculate_bonus()
        
        # Deduct any taxes or other deductions from the total salary
        total_salary -= self.calculate_deductions()
        
        return total_salary
    
    def calculate_bonus(self):
        # Calculate any bonuses or allowances to be added to the salary
        # based on performance, sales targets, etc.
        return 0  # Default bonus is 0
    
    def calculate_deductions(self):
        # Calculate any taxes or other deductions to be subtracted from the salary
        # based on the employee's salary bracket, contributions, etc.
        return 0  # Default deductions is 0
    
    def print_salary_slip(self):
        # Print the salary slip for the employee
        print("Salary slip for", self.name)
        print("===============================")
        print("Base Salary:", self.base_salary)
        print("Bonus:", self.calculate_bonus())
        print("Deductions:", self.calculate_deductions())
        print("-------------------------------")
        print("Total Salary:", self.calculate_salary())

# Create an instance of the SalaryTemplate class

employee = SalaryTemplate("John Doe", 50000)

# Print the salary slip for the employee
employee.print_salary_slip()
Salary slip for John Doe
===============================
Base Salary: 50000
Bonus: 0
Deductions: 0
