# Address Book 
by Alayna Ferdarko
*Created on 3 October 2024*

Welcome to **Address Book** – your one-stop solution for keeping track of all your contacts in a simple and intuitive interface. With this application, you can easily store, search, update, and export your contacts, including their name, email, birthday, phone number, zodiac sign, and the nature of your relationship with them. Say goodbye to scattered contact information!

### Features:
- **Add Contacts**: Store names, emails, birthdays, phone numbers, zodiac signs, and relationship details.
- **Search Contacts**: Find contacts by name to quickly locate the information you need.
- **Update Contacts**: Update any existing contact’s details effortlessly.
- **Export Contacts**: Export your entire address book into a CSV file for easy backup or sharing.
- **Simple Interface**: A clean and user-friendly interface designed for maximum convenience.

### Installation Instructions:

To get **Address Book** running on your machine, follow these steps:

1. **Download** this repository or clone it via Git:
    ```
    git clone https://github.com/your-username/address-book.git
    ```

2. **Install the Dependencies**:
    The project uses **SQLite** for database management, **Tkinter** for the GUI, and **csv** for exporting data. You’ll need Python 3 and the `sqlite3` library, which comes pre-installed with Python.
    
    Tkinter may need to be installed separately depending on your Python setup. If it's not installed, you can install it by running:
    ```
    pip install tk
    ```

3. **Run the Program**:
    Open your terminal (or command prompt), navigate to the directory where you've saved the program, and execute the following command:
    ```
    python address_book.py
    ```

---

### Requirements:

- **Python 3.x**: The program is built with Python 3.
- **Tkinter**: Required for the graphical user interface (GUI).
- **SQLite3**: Used for storing contacts data in a local database.
- **CSV**: Used for exporting contacts to a CSV file.

---

### Usage:

Once you've launched the program, the interface will guide you through the process. Here’s a quick rundown of the main actions you can take:

- **Add a Contact**: Enter the contact details (name, email, etc.) and hit "Add Contact."
- **Search for a Contact**: Enter a name in the search bar and hit "Search" to view matching contacts.
- **Update a Contact**: Double-click on a contact in the list to load their details. Modify the fields and hit "Update Contact."
- **Export Contacts**: Click on "Export Contacts" to save all your contacts in a CSV file.

---

### Directory Structure:
```
address_book/
├── address_book.py        # Main program file
└── address_book.db        # Database file (auto-generated)
```

### License:

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
