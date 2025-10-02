import re

# Validation functions
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Customer Feedback Manager
def customer_feedback_manager():
    feedback_list = []

    while True:
        print("\n--- CUSTOMER FEEDBACK MANAGER ---")
        print("1. Add Feedback")
        print("2. View All Feedback")
        print("3. Search Feedback")
        print("4. Delete Feedback")
        print("5. Filter by Category")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            name = input("Enter customer name: ").strip()

            # Phone validation
            while True:
                phone = input("Enter phone (10 digits): ").strip()
                if is_valid_phone(phone):
                    break
                print("Invalid phone number! Enter 10 digits.")

            # Email validation with duplicate check
            while True:
                email = input("Enter email: ").strip()
                if not is_valid_email(email):
                    print("Invalid email! Enter a valid email address.")
                elif any(f['email'] == email for f in feedback_list):
                    print("This email already submitted feedback!")
                else:
                    break

            category = input("Enter feedback category (Complaint/Suggestion): ").strip().title()
            feedback_text = input("Enter feedback: ").strip()

            feedback = {
                "name": name,
                "phone": phone,
                "email": email,
                "category": category,
                "feedback": feedback_text
            }

            feedback_list.append(feedback)
            print(f"\nFeedback from '{name}' added successfully!")

        elif choice == '2':
            if not feedback_list:
                print("\nNo feedback found!")
            else:
                print("\n--- ALL FEEDBACK ---")
                for i, f in enumerate(feedback_list, 1):
                    print(f"{i}. {f['name']} - {f['phone']} - {f['email']} - {f['category']} - {f['feedback']}")

        elif choice == '3':
            term = input("Enter name or email to search: ").strip().lower()
            found = [f for f in feedback_list if term in f['name'].lower() or term in f['email'].lower()]
            if found:
                print("\n--- SEARCH RESULTS ---")
                for f in found:
                    print(f"{f['name']} - {f['phone']} - {f['email']} - {f['category']} - {f['feedback']}")
            else:
                print("No feedback found with that name/email.")

        elif choice == '4':
            email = input("Enter email of feedback to delete: ").strip()
            for f in feedback_list:
                if f['email'] == email:
                    feedback_list.remove(f)
                    print("Feedback deleted successfully!")
                    break
            else:
                print("Feedback with that email not found.")

        elif choice == '5':
            cat = input("Enter category to filter (Complaint/Suggestion): ").strip().title()
            filtered = [f for f in feedback_list if f['category'] == cat]
            if filtered:
                print(f"\n--- FEEDBACK IN CATEGORY: {cat} ---")
                for f in filtered:
                    print(f"{f['name']} - {f['phone']} - {f['email']} - {f['feedback']}")
            else:
                print(f"No feedback found in category '{cat}'.")

        elif choice == '6':
            print("Exiting Customer Feedback Manager. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run the manager
customer_feedback_manager()
