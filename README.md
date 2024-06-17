# Order Processing System

### Overview

This project is an order processing system for a large company. The system integrates various specific business rules for different types of products and allows easy maintenance and expansion of these rules.

## Technologies Used

- **Python:** Programming language used for the implementation of the order processing system.
- **unittest:** Python's built-in unit testing framework used for writing and executing test cases.
- **sys and os modules:** Used for adjusting the PYTHONPATH dynamically in test files to ensure correct module imports.
- **StringIO:** Used for capturing and verifying standard output in test cases.
- **Git:** Version control system for managing project codebase.

## Project Structure

- **src/:** Contains the main modules (main.py, models.py) and subdirectories (processors/) with processor implementations.
- **tests/:** Contains unit test files (test_main.py, test_processors.py) for testing different aspects of the order processing system.

## How to Run the Project

### Prerequisites
- Python 3.x installed on your machine.

Clone the repository:
```
git clone https://github.com/jteoni/python-order-processing-system.git
cd python-order-processing-system
```
Install dependencies:
   ```
   pip install -r requeriments.txt
  ```
Execute the main script:
   ```
   python main.py
```
