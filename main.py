def display_menu():
    print("\n--- Bug & Feature Tracker ---")
    print("1. Add an Entry (Bug or Feature)")
    print("2. View All Entries")
    print("3. Display Summary Statistics")
    print("4. Exit")

def add_entry(entries):
    title = input("Enter title or short description: ").strip()
    if not title:
        print("Error: Title cannot be empty!")
        return

    print("Select Type:")
    print("1. Bug")
    print("2. Feature")
    type_choice = input("Enter choice (1/2): ").strip()
    if type_choice == "1":
        entry_type = "Bug"
    elif type_choice == "2":
        entry_type = "Feature"
    else:
        print("Invalid choice. Defaulting to Bug.")
        entry_type = "Bug"

    print("Select Priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    priority_choice = input("Enter choice (1/2/3): ").strip()
    priorities = {"1": "Low", "2": "Medium", "3": "High"}
    priority = priorities.get(priority_choice, "Medium")

    print("Select Status:")
    print("1. Open")
    print("2. Resolved")
    status_choice = input("Enter choice (1/2): ").strip()
    statuses = {"1": "Open", "2": "Resolved"}
    status = statuses.get(status_choice, "Open")

    entry = {
        "title": title,
        "type": entry_type,
        "priority": priority,
        "status": status
    }
    entries.append(entry)
    print("Entry added successfully!")

def view_entries(entries):
    if not entries:
        print("\nNo entries recorded yet.")
        return
    print("\n--- All Entries ---")
    for idx, entry in enumerate(entries, 1):
        print(f"{idx}. [{entry['type']}] {entry['title']} | Priority: {entry['priority']} | Status: {entry['status']}")

def display_summary(entries):
    total = len(entries)
    bugs = sum(1 for e in entries if e["type"] == "Bug")
    features = sum(1 for e in entries if e["type"] == "Feature")
    open_count = sum(1 for e in entries if e["status"] == "Open")
    resolved_count = sum(1 for e in entries if e["status"] == "Resolved")

    print("\n--- Summary Statistics ---")
    print(f"Total number of entries: {total}")
    print(f"Number of bugs: {bugs}")
    print(f"Number of feature requests: {features}")
    print(f"Number of open entries: {open_count}")
    print(f"Number of resolved entries: {resolved_count}")

def main():
    entries = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            display_summary(entries)
        elif choice == "4":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
