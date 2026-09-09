subjects = ["Programming", "Networking", "Database", "Mathematics", "English"]

def collect_marks():
    student_name = input("Enter student's name: ").strip()
    student_marks = {}
    for subj in subjects:
        while True:
            try:
                m = float(input(f"Enter marks for {subj}: "))
                student_marks[subj] = m
                break
            except ValueError:
                print("Please enter a valid number.")

    tot = sum(student_marks.values())
    pct = tot / len(subjects)
    return student_name, student_marks, tot, pct

def write_record(fname, student_name, student_marks, tot, pct):
    f = open(fname, "w")
    f.write(f"Student Name: {student_name}\n")
    for subj, m in student_marks.items():
        f.write(f"{subj}: {int(m) if m.is_integer() else m}\n")
    f.write(f"Total: {int(tot) if tot.is_integer() else tot}\n")
    f.write(f"Percentage: {pct:.0f}%\n")
    f.close()

def load_record(fname):
    f = open(fname, "r")
    content = f.read()
    f.close()
    return content

def main():
    fname = "student_record.txt"
    student_name, student_marks, tot, pct = collect_marks()
    write_record(fname, student_name, student_marks, tot, pct)
    print(f"\nRecord saved to {fname}")
    print("\n--- Reading back saved record ---")
    print(load_record(fname))

if __name__ == "__main__":
    main()