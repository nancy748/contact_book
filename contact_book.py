import json
import os

CONTACTS_FILE = 'contacts.json'

# Load contacts from JSON file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, 'r') as f:
        return json.load(f)

# Save contacts to JSON file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("Contact added.")

# Search for a contact by name or phone
def search_contacts(query):
    contacts = load_contacts()
    results = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
    return results

# Update an existing contact
def update_contact(old_name, new_name, new_phone, new_email):
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == old_name.lower():
            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email
            save_contacts(contacts)
            print("Contact updated.")
            return
    print("Contact not found.")

# Delete a contact
def delete_contact(name):
    contacts = load_contacts()
    contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    save_contacts(contacts)
    print("Contact deleted (if existed).")

# Display all contacts
def list_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        for c in contacts:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")

# Main menu loop
def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. List all contacts")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            query = input("Search by name or phone: ")
            results = search_contacts(query)
            if results:
                for c in results:
                    print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
            else:
                print("No matching contacts.")

        elif choice == '3':
            old_name = input("Enter name of contact to update: ")
            new_name = input("New name: ")
            new_phone = input("New phone: ")
            new_email = input("New email: ")
            update_contact(old_name, new_name, new_phone, new_email)

        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == '5':
            list_contacts()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
