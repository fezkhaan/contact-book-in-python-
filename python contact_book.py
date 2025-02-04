import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create the contacts table if it does not exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT
)
''')
conn.commit()

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address (optional): ")

    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()

    if contacts:
        print("\nContact List:")
        print("ID | Name | Phone | Email")
        print("----------------------------")
        for contact in contacts:
            print(f"{contact[0]} | {contact[1]} | {contact[2]} | {contact[3]}")
        print()
    else:
        print("No contacts found!")

# Function to search for a contact by name
def search_contact():
    name = input("Enter the name to search: ")
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
    contacts = cursor.fetchall()

    if contacts:
        print("\nSearch Results:")
        print("ID | Name | Phone | Email")
        print("----------------------------")
        for contact in contacts:
            print(f"{contact[0]} | {contact[1]} | {contact[2]} | {contact[3]}")
        print()
    else:
        print("No matching contacts found!")

# Function to update a contact
def update_contact():
    contact_id = input("Enter the ID of the contact to update: ")
    cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    contact = cursor.fetchone()

    if contact:
        print("Leave the field empty if you do not want to change it.")
        new_name = input(f"Enter new name (current: {contact[1]}): ") or contact[1]
        new_phone = input(f"Enter new phone number (current: {contact[2]}): ") or contact[2]
        new_email = input(f"Enter new email (current: {contact[3]}): ") or contact[3]

        cursor.execute("UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?",
                       (new_name, new_phone, new_email, contact_id))
        conn.commit()
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

# Function to delete a contact
def delete_contact():
    contact_id = input("Enter the ID of the contact to delete: ")
    cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    contact = cursor.fetchone()

    if contact:
        cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        conn.commit()
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# Main menu for the contact book
def main_menu():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Entry point of the application
if __name__ == "__main__":
    main_menu()

# Close the database connection when the program exits
conn.close()













