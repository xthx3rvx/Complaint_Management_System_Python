import os
import uuid

FILENAME = "complaints.txt"

def generate_complaint_id():
    return str(uuid.uuid4())[:8] 

def add_complaint():
    try:
        name = input("Enter your name: ").strip()
        issue = input("Describe your issue: ").strip()
        if not name or not issue:
            raise ValueError("Name and issue description cannot be empty.")
        
        complaint_id = generate_complaint_id()
        with open(FILENAME, "a") as file:
            file.write(f"{complaint_id},{name},{issue},Open\n")
        print(f"Complaint submitted successfully!\n Your Complaint ID is: {complaint_id}\n")
    except Exception as e:
        print(f"Error while submitting complaint: {e}\n")

def view_complaints():
    try:
        if not os.path.exists(FILENAME):
            raise FileNotFoundError("No complaints found.")
        
        with open(FILENAME, "r") as file:
            complaints = file.readlines()
            if not complaints:
                print("No complaints recorded.\n")
                return
            print("\n--- Complaint List ---")
            for line in complaints:
                cid, name, issue, status = line.strip().split(",", 3)
                print(f"ID: {cid} | Name: {name} | Issue: {issue} | Status: {status}")
            print()
    except FileNotFoundError as fnf:
        print(f"Error: {fnf}\n")
    except Exception as e:
        print(f"Unexpected error: {e}\n")

def search_complaint():
    try:
        cid = input("Enter Complaint ID to search: ").strip()
        found = False
        with open(FILENAME, "r") as file:
            for line in file:
                complaint_id, name, issue, status = line.strip().split(",", 3)
                if complaint_id == cid:
                    print(f"\nFound Complaint:\nID: {complaint_id}\nName: {name}\nIssue: {issue}\nStatus: {status}\n")
                    found = True
                    break
        if not found:
            print("No complaint found with that ID.\n")
    except Exception as e:
        print(f"Error during search: {e}\n")

def resolve_complaint():
    try:
        cid = input("Enter Complaint ID to mark as resolved: ").strip()
        updated = False
        if not os.path.exists(FILENAME):
            raise FileNotFoundError("No complaints to update.")

        with open(FILENAME, "r") as file:
            complaints = file.readlines()
        
        with open(FILENAME, "w") as file:
            for line in complaints:
                complaint_id, name, issue, status = line.strip().split(",", 3)
                if complaint_id == cid:
                    file.write(f"{complaint_id},{name},{issue},Resolved\n")
                    updated = True
                else:
                    file.write(line)
        
        if updated:
            print("Complaint marked as resolved.\n")
        else:
            print("Complaint ID not found.\n")
    except FileNotFoundError as fnf:
        print(f"Error: {fnf}\n")
    except Exception as e:
        print(f"Error updating complaint: {e}\n")

def menu():
    while True:
        print("==== Complaint Management System ====")
        print("1. Submit Complaint")
        print("2. View All Complaints")
        print("3. Search Complaint by ID")
        print("4. Resolve Complaint")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_complaint()
            elif choice == 2:
                view_complaints()
            elif choice == 3:
                search_complaint()
            elif choice == 4:
                resolve_complaint()
            elif choice == 5:
                print("Exiting Complaint Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric choice.\n")

if __name__ == "__main__":
    menu()
