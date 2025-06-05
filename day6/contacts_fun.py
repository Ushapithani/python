def add_contact(contacts):
    name = input("Enter a name: ")
    number = input("Enter a number: ")
    contacts[name] = number
    print("Contact added.")

def view_contacts(contacts):
    for name, number in contacts.items():
        print(f"{name}: {number}")

def delete_contact(contacts, name):
    del contacts[name]
    print("Deleted contact:", name)

def search_contact(contacts, name):
    print(f"{name}'s number is {contacts[name]}")

def edit_contact(contacts, name, new_number):
    contacts[name] = new_number
    print("Contact updated.")
