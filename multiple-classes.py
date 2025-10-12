rom enum import Enum

# Enum representing performance multipliers
class Performance(Enum):
    AVERAGE = 1.0
    GOOD = 1.2
    EXCELLENT = 1.5


class Employee:
    def __init__(self, name, salary, fixed_bonus, performance):
        self.name = name
        self.salary = salary
        self.fixed_bonus = fixed_bonus
        self.performance = performance

    def calculate_annual_bonus(self, department):
        """
        Calculates the employee's total annual bonus.
        The bonus now depends on both department bonus rate and performance multiplier.
        """
        return (self.salary * department.bonus_rate * self.performance.value) + self.fixed_bonus


class Department:
    def __init__(self, bonus_rate):
        self.bonus_rate = bonus_rate

    def calculate_total_bonuses(self, employees):
        """
        Aggregates total bonuses for all employees in the department.
        Delegates the bonus calculation to each employee (composition principle).
        """
        return sum(employee.calculate_annual_bonus(self) for employee in employees)


def main():
    # Create employee objects with different performance levels
    employee1 = Employee("John Doe", 50000, 1000, Performance.GOOD)
    employee2 = Employee("Jane Smith", 60000, 1500, Performance.EXCELLENT)

    # Create a department with a fixed bonus rate
    department = Department(0.10)  # 10% bonus rate

    # Calculate and display bonuses per employee
    print(f"Annual Bonus for {employee1.name}: {employee1.calculate_annual_bonus(department)}")
    print(f"Annual Bonus for {employee2.name}: {employee2.calculate_annual_bonus(department)}")

    # Calculate and display total bonuses for the department
    employees = [employee1, employee2]
    print(f"Total Bonuses for all Employees: {department.calculate_total_bonuses(employees)}")


if __name__ == "__main__":
    main()
