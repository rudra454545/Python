# Python Lab 1 - ACC 3rd Semester B.Tech
### Author: Rudra Prasad
**Course**: ACC Python Sem 3rd Btech  
**Module**: Module 1 , 2 & 3

---

## 📖 Overview
This repository contains the Python lab codes for the database and experiments conducted in the 3rd Semester of B.Tech. These scripts cover fundamental Python concepts ranging from basic syntax and flow control to data structures and file handling.

Each experiment is designed to demonstrate specific logic and functionality as per the lab syllabus.

## 🛠️ Prerequisites
- **Python 3.x**: Ensure you have Python installed. You can check by running:
  ```bash
  python --version
  ```
- **Text Editor/IDE**: VS Code, PyCharm, or even a simple text editor like Notepad.

## 🚀 How to Run the Codes
1. **Navigate to the directory**: Open your terminal (Command Prompt/PowerShell) and change directory to where the file is located.
   ```bash
   cd path/to/Lab1/EXP
   ```
2. **Run a specific experiment**: Execute the python file using the `python` command.
   ```bash
   python 1a-exp.py
   ```
   *(Replace `1a-exp.py` with the filename you wish to run)*

---

## 📂 Experiment Logic & Code Breakdown

### Experiment 1: Python Basics
**Files**: `1a-exp.py`, `1b-exp.py`, `1c-exp.py`
- **Logic**: These scripts introduce basic input/output operations.
- **Example (`1a-exp.py`)**: Adds two numbers provided by the user.
    - Uses `input()` to get string input and `float()` to convert it for calculation.
    - Implements `try-except` blocks to handle non-numeric inputs gracefully.

### Experiment 2: Variables, Datatypes, and Operators
**Files**: `2a-exp.py`, `2b-exp.py`, `2c-exp.py`
- **Logic**: Focuses on arithmetic operations and user interaction via menus.
- **Example (`2a-exp.py`)**: A Menu-Driven Calculator.
    - Defines functions for `add`, `subtract`, `multiply`, and `divide`.
    - Uses a `while True` loop to keep the menu active until the user chooses to exit.
    - Demonstrates conditional logic (`if-elif-else`) to route user choices to the correct function.

### Experiment 3: Control Systems (If-Else, Loops) & Functions
**Files**: `3a-exp.py`, `3b-exp.py`, `3c-exp.py`, `3d-exp.py`
- **Logic**: control flow mechanisms.
- **Example (`3a-exp.py`)**: determines the day of the week based on a number (1-7).
    - Uses a chain of `if-elif-else` statements to map integers to string values (e.g., 1 -> Sunday).
    - Includes input validation to ensure the number is within range.

### Experiment 4: Lists and Dictionaries
**Files**: `4a-exp.py`, `4b-exp.py`, `4c-exp.py`
- **Logic**: Manipulation of mutable collections.
- **Example (`4a-exp.py`)**: Operations on a List of Supercars.
    - **Append**: Adds an item to the end (`.append()`).
    - **Insert**: Adds an item at a specific index (`.insert()`).
    - **Remove**: Deletes a specific item by value (`.remove()`).
    - **Pop**: Removes an item by index (`.pop()`).
    - **Clear**: Empties the entire list (`.clear()`).

### Experiment 5: Data Structures (Linked Lists)
**Files**: `5a-exp.py`, `5b-exp.py`, `5c-exp.py`
- **Logic**: Implementing custom data structures from scratch using Classes.
- **Example (`5a-exp.py`)**: Singly Linked List.
    - **Class Node**: Represents an individual element, holding `data` and a pointer to the `next` node.
    - **Class LinkedList**: Manages the `head` of the list and provides methods like `append()` to add new nodes by traversing to the end of the chain.
    - **Display**: Iterates through nodes starting from `head` until `None` is reached.

### Experiment 6: File Handling
**Files**: `6a-exp.py` to `6e-exp.py`
- **Logic**: Reading from and writing to external files.
- **Example (`6a-exp.py`)**: Basic Input/Output.
    - **Write Mode (`'w'`)**: Opens a file (creates it if missing) and writes content.
    - **Read Mode (`'r'`)**: Opens the existing file and prints its contents to the console.
    - Uses the `with open(...)` context manager to ensure files are automatically closed after operations.

### Experiment 7: Pickle Module
**Files**: `7a-exp.py`, `7b-exp.py`, `7c-exp.py`
- **Logic**: Serialization and Deserialization of Python objects.
- **Example (`7c-exp.py`)**: Storing structured data (Dictionaries).
    - **Pickle Dump**: Serializes a list of dictionaries (SUV records) into a binary file (`.dat`).
    - **Pickle Load**: Reads the binary file and reconstructs the Python list object exactly as it was.
    - Essential for saving complex data states between program runs.

---

### ✨ Note from the Author
These codes are written to be simple yet comprehensive for the **ACC Python Sem 3rd Btech** curriculum. Modify and experiment with parameters to see how the logic changes!

**Happy Coding!**  
*- Rudra Prasad*
