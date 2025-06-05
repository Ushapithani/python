def add_contact(contacts):
    name = input("Enter a name: ")
    number = input("Enter a number: ")
    contacts[name] = number
    print("Contact added.")

def view_contacts(contacts):
    for name, number in contacts.items():
        print(f"{name}: {number}")

def delete_contact(contacts):
    name = input("Enter the name to delete: ")
    del contacts[name]
    print("Deleted contact:", name)

def search_contact(contacts):
    name = input("Enter name to search: ")
    print(f"{name}'s number is {contacts[name]}")

def edit_contact(contacts):
    name = input("Enter contact name to edit: ")
    new_number = input("Enter new number: ")
    contacts[name] = new_number
    print("Contact updated.")

# Main program
contacts = {}

while True:
    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Delete a Contact")
    print("4. Search Contact")
    print("5. Edit Contact")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        add_contact(contacts)
    elif choice == 2:
        if contacts:
            view_contacts(contacts)
        else:
            print("No contacts found.")
    elif choice == 3:
        if contacts:
            name = input("Enter the name to delete: ")
            if name in contacts:
                delete_contact(contacts)
            else:
                print("Contact not found.")
        else:
            print("No contacts to delete.")
    elif choice == 4:
        if contacts:
            name = input("Enter name to search: ")
            if name in contacts:
                print(f"{name}'s number is {contacts[name]}")
            else:
                print("Contact not found.")
        else:
            print("No contacts to search.")
    elif choice == 5:
        if contacts:
            name = input("Enter contact name to edit: ")
            if name in contacts:
                new_number = input("Enter new number: ")
                contacts[name] = new_number
                print("Contact updated.")
            else:
                print("Contact not found.")
        else:
            print("No contacts to edit.")
    elif choice == 6:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
