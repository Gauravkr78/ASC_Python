# ========================================
# Python Naming Conventions Examples
# ========================================

# Variables & Functions: snake_case
student_name = "Alice"       # variable
student_age = 20

def calculate_average_score(scores):   # function
    """Calculate the average score of a student."""
    return sum(scores) / len(scores)

average = calculate_average_score([85, 90, 78])
print(f"Average Score: {average}")

# Constants: UPPER_CASE
MAX_STUDENTS = 100
DEFAULT_TIMEOUT = 30
PI = 3.14159

print(f"Max students allowed: {MAX_STUDENTS}")

# Classes: PascalCase 
class StudentDatabase:
    """A class representing a simple student database."""

    def __init__(self):
        # Private variable (by convention, prefix with _)
        self._students = []

    def add_student(self, name, age):
        """Add a student to the database."""
        self._students.append({"name": name, "age": age})

    def list_students(self):
        """List all students in the database."""
        return self._students


class MathCalculator:
    """Class for performing math operations."""

    @staticmethod
    def square(number):  # static method, snake_case
        return number ** 2

    @staticmethod
    def cube(number):
        return number ** 3


# Using the classes:
db = StudentDatabase()
db.add_student("Alice", 20)
db.add_student("Bob", 22)
print("\nStudent Database:", db.list_students())

print("\nMath Calculator Examples:")
print("Square of 4:", MathCalculator.square(4))
print("Cube of 3:", MathCalculator.cube(3))


# Modules (file names): snake_case
# Example file name: student_database.py

# Private helper functions/variables inside a module:
def _private_helper_function():
    """This is a private helper (by convention, prefix with _)."""
    print("I am private to this module.")


_private_variable = "hidden"


# Mixed Naming Demo
class BankAccount:
    """Class showing more naming convention examples."""

    bank_name = "Python Bank"  # Class variable in snake_case

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder  # instance variable
        self._balance = balance               # private instance variable

    def deposit(self, amount):   # method snake_case
        """Deposit money."""
        self._balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient balance."""
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        """Return current balance."""
        return self._balance


# Example usage:
acc = BankAccount("Alice", 500)
acc.deposit(200)
acc.withdraw(100)
print("\nBank Account Balance:", acc.get_balance())
