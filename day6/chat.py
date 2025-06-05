contacts = {}  # Dictionary to store contact name and number

# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists.")
    else:
        number = input("Enter number: ")
        contacts[name] = number
        print("Contact added.")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts to show.")
    else:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

# Function to search for a contact
def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main program loop
def main():
    while True:
        print("\n---- Contact Manager ----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
