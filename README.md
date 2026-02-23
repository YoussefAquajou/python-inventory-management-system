Inventory & Data Management Utility
A lightweight, console-based Python application designed to handle demographic data processing and persistent product inventory management. This project demonstrates core programming principles including Modular Programming, File I/O (CSV), and Data Structure manipulation.

Features
1. Product Inventory System (CRUD)
Persistent Storage: All product data is saved to and loaded from a produits.csv file.

Data Integrity: Includes validation logic to prevent duplicate entries based on unique Product IDs.

Formatted Display: View the current catalog with prices and stock levels in a clean, readable format.

2. Personnel Data Management
Algorithmic Analysis: Automatically calculates demographic metrics such as the average age of the group.

Dynamic Filtering: Efficiently filters and identifies "Adult" members (18+) using list comprehensions.

Data Organization: Handles complex data using lists of tuples for structured information.

Project Structure
Plaintext
├── main.py          # Entry point and Personnel Management logic
├── inventory.py     # Inventory logic and CSV file handling
└── produits.csv     # Persistent data storage (Database)
Installation & Usage
Prerequisites
Python 3.x installed on your machine.

Running the Application
Clone or Download the repository to your local machine.

Navigate to the project folder via your terminal/command prompt.

Run the application using the following command:

Bash
python main.py
Technical Skills Demonstrated
File Handling: Utilizing the native csv and os libraries for data persistence.

Modular Programming: Separating logic into different files (main.py vs inventory.py) for better maintainability.

Input Validation: Error handling for user inputs and duplicate data prevention.

Pythonic Code: Usage of lambda-like logic, list comprehensions, and formatted strings (f-strings).

License
This project is open-source and available under the MIT License.