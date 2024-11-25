#Contact book using python

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact for {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not found_contacts:
            print("No matching contacts found.")
        else:
            print("\nSearch Results:")
            for contact in found_contacts:
                print(contact)

    def update_contact(self, name):
        contact_to_update = None
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact_to_update = contact
                break
        
        if not contact_to_update:
            print("Contact not found.")
            return

        print(f"Updating contact for {contact_to_update.name}:")
        contact_to_update.name = input(f"Enter new name (current: {contact_to_update.name}): ") or contact_to_update.name
        contact_to_update.phone = input(f"Enter new phone number (current: {contact_to_update.phone}): ") or contact_to_update.phone
        contact_to_update.email = input(f"Enter new email (current: {contact_to_update.email}): ") or contact_to_update.email
        contact_to_update.address = input(f"Enter new address (current: {contact_to_update.address}): ") or contact_to_update.address
        print("Contact updated successfully.")

    def delete_contact(self, name):
        contact_to_delete = None
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact_to_delete = contact
                break
        
        if not contact_to_delete:
            print("Contact not found.")
            return
        
        self.contacts.remove(contact_to_delete)
        print(f"Contact for {name} deleted successfully.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        
        elif choice == "2":
            contact_book.view_contacts()
        
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            contact_book.update_contact(name)
        
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        
        elif choice == "6":
            print("Exiting the contact book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
