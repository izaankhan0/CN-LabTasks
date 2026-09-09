import json

def collect_info():
    sid = input("Enter Student ID: ").strip()
    sname = input("Enter Name: ").strip()
    dept = input("Enter Department: ").strip()
    sem = int(input("Enter Semester: "))
    cgpa = float(input("Enter GPA: "))
    return {
        "student_id": sid,
        "name": sname,
        "department": dept,
        "semester": sem,
        "gpa": cgpa,
    }

def write_json(fname, info):
    f = open(fname, "w")
    json.dump(info, f, indent=4)
    f.close()

def load_json(fname):
    f = open(fname, "r")
    content = json.load(f)
    f.close()
    return content

def main():
    print("=== Student Information (JSON Storage) ===")
    fname = "student_info.json"

    info = collect_info()
    write_json(fname, info)
    print(f"\nData saved to {fname}")

    print("\n--- Reading back saved JSON ---")
    loaded = load_json(fname)
    for k, v in loaded.items():
        print(f"{k}: {v}")

if __name__=="__main__":
    main()