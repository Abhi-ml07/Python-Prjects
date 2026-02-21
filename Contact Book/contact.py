import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("✅ Contact Added Successfully!\n")

def search_contact(contacts):
    name = input("Enter Name to Search: ")

    if name in contacts:
        print("\n📞 Contact Found:")
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("❌ Contact Not Found!")
    print()

def delete_contact(contacts):
    name = input("Enter Name to Delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("🗑 Contact Deleted Successfully!\n")
    else:
        print("❌ Contact Not Found!\n")

def view_contacts(contacts):
    if not contacts:
        print("📂 No contacts available.\n")
        return

    print("\n📒 Contact List:")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("-" * 20)
    print()

def main():
    contacts = load_contacts()

    while True:
        print("==== CONTACT BOOK ====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            view_contacts(contacts)
        elif choice == "5":
            print("👋 Exiting Contact Book...")
            break
        else:
            print("❌ Invalid Choice! Try Again.\n")

if __name__ == "__main__":
    main()