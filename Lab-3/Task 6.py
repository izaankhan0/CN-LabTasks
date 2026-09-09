grade_map = {
    "A": 4.0, "A-": 3.67,
    "B+": 3.33, "B": 3.0, "B-": 2.67,
    "C+": 2.33, "C": 2.0, "C-": 1.67,
    "D+": 1.33, "D": 1.0,
    "F": 0.0,
}

def input_courses():
    course_list = []
    n = int(input("How many courses? "))
    for i in range(n):
        print(f"\nCourse {i+1}:")
        cname = input("  Course name: ").strip()
        ch = float(input("  Credit hours: "))
        while True:
            g = input("  Letter grade: ").strip().upper()
            if g in grade_map:
                break
            print(f"  Invalid grade. Choose from: {', '.join(grade_map.keys())}")

        pts = grade_map[g]
        qp = pts * ch
        course_list.append((cname, ch, g, pts, qp))
    return course_list

def show_report(course_list):
    total_ch = sum(c[1] for c in course_list)
    total_qp = sum(c[4] for c in course_list)
    semester_gpa = total_qp/total_ch if total_ch else 0

    print(f"\n{'Course':<15}{'CH':<6}{'Grade':<8}{'GP':<7}{'Quality Points':<15}")
    print("-"*55)
    for cname, ch, g, pts, qp in course_list:
        print(f"{cname:<15}{ch:<6.0f}{g:<8}{pts:<7.2f}{qp:<15.2f}")
    print("-"*55)
    print(f"{'Total':<15}{total_ch:<6.0f}{'':<8}{'':<7}{total_qp:<15.2f}")
    print(f"\nSemester GPA = {semester_gpa:.2f}")

def main():
    print("=== Semester GPA Report ===")
    course_list = input_courses()
    show_report(course_list)

if __name__=="__main__":
    main()