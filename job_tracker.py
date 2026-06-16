applications = []

while True:
    print("\n===== JOB APPLICATION TRACKER =====")
    print("1. Add Application")
    print("2. View Applications")
    print("3. Search Company")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        company = input("Enter company name: ")
        role = input("Enter role: ")
        status = input("Enter status (Applied/Interview/Rejected/Selected): ")

        applications.append({
            "company": company,
            "role": role,
            "status": status
        })

        print("Application added successfully!")

    elif choice == "2":
        if not applications:
            print("No applications found.")
        else:
            for app in applications:
                print(
                    f"Company: {app['company']}, "
                    f"Role: {app['role']}, "
                    f"Status: {app['status']}"
                )

    elif choice == "3":
        search = input("Enter company name to search: ")

        found = False

        for app in applications:
            if app["company"].lower() == search.lower():
                print(
                    f"Company: {app['company']}, "
                    f"Role: {app['role']}, "
                    f"Status: {app['status']}"
                )
                found = True

        if not found:
            print("Company not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")