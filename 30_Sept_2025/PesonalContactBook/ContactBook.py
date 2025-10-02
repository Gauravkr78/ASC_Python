# def contact_book():
#     contacts = []  # List to store all contacts
#
#     while True:
#         print("\n--- PERSONAL CONTACT BOOK ---")
#         print("1. Add Contact")
#         print("2. View All Contacts")
#         print("3. Search Contact")
#         print("4. Exit")
#
#         choice = input("Choose an option (1-4): ")
#
#         if choice == '1':
#             # Add new contact
#             name = input("Enter name: ")
#             phone = input("Enter phone: ")
#             email = input("Enter email: ")
#
#             contact = {
#                 "name": name,
#                 "phone": phone,
#                 "email": email
#             }
#
#             contacts.append(contact)
#             print(f"Contact {name} added successfully!")
#
#         elif choice == '2':
#             # View all contacts
#             if not contacts:
#                 print("No contacts found!")
#             else:
#                 print("\n--- ALL CONTACTS ---")
#                 for i, contact in enumerate(contacts, 1):
#                     print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")
#
#         elif choice == '3':
#             # Search contact
#             search_name = input("Enter name to search: ")
#             found_contacts = [c for c in contacts if search_name.lower() in c['name'].lower()]
#
#             if found_contacts:
#                 print("\n--- SEARCH RESULTS ---")
#                 for contact in found_contacts:
#                     print(f"Name: {contact['name']}")
#                     print(f"Phone: {contact['phone']}")
#                     print(f"Email: {contact['email']}\n")
#             else:
#                 print("No contacts found with that name.")
#
#         elif choice == '4':
#             print("Goodbye!")
#             break
#
#         else:
#             print("Invalid choice! Please try again.")
#
#
# # Uncomment to run the contact book
# # contact_book()




# def contact_book():
#     contacts = []  # List to store all contacts
#
#     while True:
#         print("\n--- PERSONAL CONTACT BOOK ---")
#         print("1. Add Contact")
#         print("2. View All Contacts")
#         print("3. Search Contact")
#         print("4. Exit")
#
#         choice = input("Choose an option (1-4): ")
#
#         if choice == '1':
#             # Add new contact
#             name = input("Enter name: ").strip()
#             phone = input("Enter phone: ").strip()
#             email = input("Enter email: ").strip()
#
#             contact = {
#                 "name": name,
#                 "phone": phone,
#                 "email": email
#             }
#
#             contacts.append(contact)
#             print(f"\nContact '{name}' added successfully!")
#
#         elif choice == '2':
#             # View all contacts
#             if not contacts:
#                 print("\nNo contacts found!")
#             else:
#                 print("\n--- ALL CONTACTS ---")
#                 for i, contact in enumerate(contacts, 1):
#                     print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")
#
#         elif choice == '3':
#             # Search contact
#             search_name = input("Enter name to search: ").strip()
#             found_contacts = [c for c in contacts if search_name.lower() in c['name'].lower()]
#
#             if found_contacts:
#                 print("\n--- SEARCH RESULTS ---")
#                 for contact in found_contacts:
#                     print(f"Name: {contact['name']}")
#                     print(f"Phone: {contact['phone']}")
#                     print(f"Email: {contact['email']}\n")
#             else:
#                 print("\nNo contacts found with that name.")
#
#         elif choice == '4':
#             print("\nGoodbye!")
#             break
#
#         else:
#             print("\nInvalid choice! Please try again.")
#
#
# # Run the contact book
# contact_book()


import re


def is_valid_phone(phone):
    # Check if phone contains exactly 10 digits
    return phone.isdigit() and len(phone) == 10


def is_valid_email(email):
    # Simple regex for validating email
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def contact_book():
    contacts = []

    while True:
        print("\n--- PERSONAL CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            # Add new contact
            name = input("Enter name: ").strip()

            # Validate phone
            while True:
                phone = input("Enter phone (10 digits): ").strip()
                if is_valid_phone(phone):
                    break
                print("Invalid phone number! Please enter 10 digits.")

            # Validate email
            while True:
                email = input("Enter email: ").strip()
                if is_valid_email(email):
                    break
                print("Invalid email! Please enter a valid email address.")

            contact = {
                "name": name,
                "phone": phone,
                "email": email
            }

            contacts.append(contact)
            print(f"\nContact '{name}' added successfully!")

        elif choice == '2':
            if not contacts:
                print("\nNo contacts found!")
            else:
                print("\n--- ALL CONTACTS ---")
                for i, contact in enumerate(contacts, 1):
                    print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

        elif choice == '3':
            search_name = input("Enter name to search: ").strip()
            found_contacts = [c for c in contacts if search_name.lower() in c['name'].lower()]

            if found_contacts:
                print("\n--- SEARCH RESULTS ---")
                for contact in found_contacts:
                    print(f"Name: {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}\n")
            else:
                print("\nNo contacts found with that name.")

        elif choice == '4':
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# Run the contact book
contact_book()

