# Contact Management System (CMS)

## Overview of the Project
The **Contact Management System (CMS)** is a command-line application built in Python designed to help users securely store, organize, and manage their personal or professional contacts. It includes a built-in user authentication system for isolated access and strict input validation to ensure data integrity.

## Features
* **User Authentication:** Secure login and registration system (`users.txt`) to protect user directories.
* **Strict Input Validation:** Enforces digit-only validation for phone numbers to prevent formatting errors.
* **CRUD Operations:** Easily add, view, search, and delete contacts.
* **Persistent Storage:** Data is automatically saved to local text files (`users.txt` and `contacts.txt`), ensuring no data is lost upon exit.
* **Modular Architecture:** Clean separation of concerns across multiple files (`main.py`, `auth.py`, `contact_operations.py`, `contact_storage.py`, `user_storage.py`, and `config.py`).

## Technologies/Tools Used
* **Language:** Python 3.x
* **Standard Libraries:** `os` and `sys`
* **Data Persistence:** Plain text files with custom parsing (`.txt`)

## Steps to Install & Run the Project
1. **Download & Place Files:** Ensure all project modules (`main.py`, `auth.py`, `contact_operations.py`, `contact_storage.py`, `user_storage.py`, and `config.py`) are in the same working directory.
2. **Open Terminal / Command Prompt:** Navigate to your project folder directory:
   ```bash
   cd path/to/your/project-folder
   ```
3. **Run the Application:** Execute the main entry point script using Python:
   ```bash
   python main.py
   ```

## Instructions for Testing
1. **Authentication:** When the script runs, choose option `2` to register a new user, then log in using option `1` with your credentials.
2. **Adding a Contact:** Select option `1`, enter a name, and provide a phone number. (*Note: Typing letters instead of digits will be blocked by the validation loop.*)
3. **Viewing & Searching:** Select option `2` to view the full contact list or option `3` to search for a specific entry by phone number.
4. **Deleting & Exiting:** Choose option `4` to delete a contact by phone number, or option `5` to safely exit the program.
