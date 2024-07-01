DATA_FILE = "teachers.json"

def show_teachers(teachers):
    if not teachers:
        print("No teachers found.")
        return
    
    for i, teacher in enumerate(teachers, start=1):
        print(f"Teacher {i}:")
        print(f"  Full Name: {teacher['full_name']}")
        print(f"  Age: {teacher['age']}")
        print(f"  Date of Birth: {teacher['dob']}")
        print("-" * 20)

def main():
    teachers = {
        "full_name": "John Doe",
        "age": 40,
        "dob": "1983-05-15"
    }
    show_teachers(teachers)

if __name__ == "__main__":
    main()
