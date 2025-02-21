#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import csv
from tkinter import filedialog

# Function to create the database
def create_database():
    connection = sqlite3.connect('address_book.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            birthday TEXT,
            phone TEXT,
            zodiac_sign TEXT,
            nature_of_relation TEXT
        )
    ''')
    connection.commit()
    connection.close()

# Function to add a new contact to the database
def add_contact():
    name = entry_name.get()
    email = entry_email.get()
    birthday = entry_birthday.get()
    phone = entry_phone.get()
    zodiac_sign = entry_zodiac.get()
    nature_of_relation = entry_nature_of_relation.get()  # Get the input for nature of relation

    if name and email:  # Ensure both name and email are provided
        connection = sqlite3.connect('address_book.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO contacts (name, email, birthday, phone, zodiac_sign, nature_of_relation) VALUES (?, ?, ?, ?, ?, ?)', 
                       (name, email, birthday, phone, zodiac_sign, nature_of_relation))
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_fields()
    else:
        messagebox.showerror("Error", "Name and email are required!")

# Function to search for a contact by name
def search_contact():
    name = entry_search.get()
    connection = sqlite3.connect('address_book.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM contacts WHERE name LIKE ?', ('%' + name + '%',))
    results = cursor.fetchall()
    connection.close()

    # Clear previous search results
    for row in tree.get_children():
        tree.delete(row)

    # Insert new results into the treeview
    for contact in results:
        tree.insert('', 'end', values=contact)  # Show all columns including ID

# Function to load selected contact into input fields for editing
def load_contact(event):
    selected_item = tree.selection()  # Get the selected item
    if selected_item:
        item = tree.item(selected_item)  # Get the item data
        contact = item['values']  # The contact data
        entry_name.delete(0, tk.END)
        entry_name.insert(0, contact[1])  # Name
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact[2])  # Email
        entry_birthday.delete(0, tk.END)
        entry_birthday.insert(0, contact[3])  # Birthday
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact[4])  # Phone
        entry_zodiac.delete(0, tk.END)
        entry_zodiac.insert(0, contact[5])  # Zodiac Sign
        entry_nature_of_relation.delete(0, tk.END)
        entry_nature_of_relation.insert(0, contact[6])  # Nature of Relationship

# Function to update the selected contact
def update_contact():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        contact_id = item['values'][0]  # Get the ID of the selected contact

        name = entry_name.get()
        email = entry_email.get()
        birthday = entry_birthday.get()
        phone = entry_phone.get()
        zodiac_sign = entry_zodiac.get()
        nature_of_relation = entry_nature_of_relation.get()  # Get the updated nature of relation

        if name and email:  # Ensure both name and email are provided
            connection = sqlite3.connect('address_book.db')
            cursor = connection.cursor()
            cursor.execute('UPDATE contacts SET name=?, email=?, birthday=?, phone=?, zodiac_sign=?, nature_of_relation=? WHERE id=?',
                           (name, email, birthday, phone, zodiac_sign, nature_of_relation, contact_id))
            connection.commit()
            connection.close()
            messagebox.showinfo("Success", "Contact updated successfully!")
            clear_fields()
            search_contact()  # Refresh the contact list
        else:
            messagebox.showerror("Error", "Name and email are required!")

# Function to export contacts to a CSV file
def export_contacts():
    connection = sqlite3.connect('address_book.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    connection.close()

    if contacts:
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        
        if file_path:
            with open(file_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                # Write the header
                csv_writer.writerow(['ID', 'Name', 'Email', 'Birthday', 'Phone', 'Zodiac Sign', 'Nature of Relation'])
                # Write the contact data
                csv_writer.writerows(contacts)
            messagebox.showinfo("Success", "Contacts exported successfully!")
    else:
        messagebox.showinfo("Info", "No contacts to export.")

# Function to clear input fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_birthday.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_zodiac.delete(0, tk.END)
    entry_nature_of_relation.delete(0, tk.END)  # Correct variable
    entry_search.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Address Book")
root.geometry("600x600")

# Create the database
create_database()

# Input fields for new contacts
tk.Label(root, text="Name").pack(pady=6)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Email").pack(pady=6)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

tk.Label(root, text="Birthday (YYYY-MM-DD)").pack(pady=6)
entry_birthday = tk.Entry(root)
entry_birthday.pack(pady=5)

tk.Label(root, text="Phone").pack(pady=6)
entry_phone = tk.Entry(root)
entry_phone.pack(pady=5)

tk.Label(root, text="Zodiac Sign").pack(pady=6)
entry_zodiac = tk.Entry(root)
entry_zodiac.pack(pady=5)

tk.Label(root, text="Nature of Relation").pack(pady=6)
entry_nature_of_relation = tk.Entry(root)  # Ensure this matches the variable used throughout
entry_nature_of_relation.pack(pady=5)

# Button to add a new contact
btn_add = tk.Button(root, text="Add Contact", command=add_contact)
btn_add.pack(pady=10)

# Search section
tk.Label(root, text="Search by Name").pack(pady=10)
entry_search = tk.Entry(root)
entry_search.pack(pady=5)

# Button to search for a contact
btn_search = tk.Button(root, text="Search", command=search_contact)
btn_search.pack(pady=10)

# Button to update the selected contact
btn_update = tk.Button(root, text="Update Contact", command=update_contact)
btn_update.pack(pady=10)

# Button to export contacts to CSV
btn_export = tk.Button(root, text="Export Contacts", command=export_contacts)
btn_export.pack(pady=10)

# Treeview to display search results
columns = ('ID', 'Name', 'Email', 'Birthday', 'Phone', 'Zodiac Sign', 'Nature of Relation')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.pack(pady=10)

for col in columns:
    tree.heading(col, text=col)

# Bind double-click event to load contact
tree.bind("<Double-1>", load_contact)

# Start the GUI event loop
root.mainloop()
