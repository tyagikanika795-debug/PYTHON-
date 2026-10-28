# MCA I Semester - Lab Sheet 07
# Python File Handling: All 30 Programs in One File
# Run this file and choose a program from the menu.

import os
import csv

TEXT_FILE = "sample.txt"
CSV_FILE = "students.csv"

def ensure_sample_files():
    if not os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, "w", encoding="utf-8") as f:
            f.write("Hello Python!\nFile handling is easy.\nPython makes file work simple.")
    if not os.path.exists("numbers.txt"):
        with open("numbers.txt", "w", encoding="utf-8") as f:
            f.write("10\n20\n30\n40\n")
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([
                ["Name", "Age", "Marks"],
                ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 76]
            ])
    for filename in ("first.txt", "second.txt"):
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f:
                f.write("Sample content from " + filename + "\n")
    if not os.path.exists("extra_students.csv"):
        with open("extra_students.csv", "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([["Name", "Age", "Marks"], ["Meena", 21, 90]])

def p01():
    with open(TEXT_FILE, "w", encoding="utf-8") as f:
        f.write("Hello Python!\nFile handling is easy.\nPython makes file work simple.")
    print("File created and data written successfully.")

def p02():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        print(f.read())

def p03():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")

def p04():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        print("Total words:", len(f.read().split()))

def p05():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        data = f.read()
    print("Lines:", len(data.splitlines()))
    print("Characters:", len(data))

def p06():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            if number % 2 == 0:
                print(line, end="")

def p07():
    print("Enter lines. Type END to finish:")
    with open("user_lines.txt", "w", encoding="utf-8") as f:
        while True:
            line = input()
            if line == "END":
                break
            f.write(line + "\n")
    print("Saved to user_lines.txt")

def p08():
    with open(TEXT_FILE, "a", encoding="utf-8") as f:
        f.write("\nThis line was appended.")
    print("Content appended.")

def p09():
    with open(TEXT_FILE, "r", encoding="utf-8") as src:
        data = src.read()
    with open("copy.txt", "w", encoding="utf-8") as dst:
        dst.write(data)
    print("Copied to copy.txt")

def p10():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        print(f.read().upper())

def p11():
    word = input("Enter word to search: ").strip()
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        found = word.lower() in f.read().lower()
    print("Word found." if found else "Word not found.")

def p12():
    word = input("Enter word to count: ").strip().lower()
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        words = [w.strip(".,!?;:").lower() for w in f.read().split()]
    print("Occurrences:", words.count(word))

def p13():
    with open("numbers.txt", "r", encoding="utf-8") as f:
        nums = [float(x) for x in f.read().split()]
    if nums:
        print("Sum:", sum(nums))
        print("Average:", sum(nums) / len(nums))
    else:
        print("No numbers found.")

def p14():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    print("Longest line:", max(lines, key=len) if lines else "File is empty.")

def p15():
    old = input("Word to replace: ")
    new = input("Replace with: ")
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        data = f.read()
    with open(TEXT_FILE, "w", encoding="utf-8") as f:
        f.write(data.replace(old, new))
    print("Replacement completed.")

def p16():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    if lines:
        print("First line:", lines[0])
        print("Last line:", lines[-1])
    else:
        print("File is empty.")

def p17():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("nonblank.txt", "w", encoding="utf-8") as f:
        f.writelines(line for line in lines if line.strip())
    print("Blank lines removed. Output: nonblank.txt")

def p18():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        words = f.read().split()
    unique = list(dict.fromkeys(words))
    with open("unique_words.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(unique))
    print("Unique words saved to unique_words.txt")

def p19():
    with open(TEXT_FILE, "r", encoding="utf-8") as f:
        words = f.read().split()
    with open("sorted_words.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(words, key=str.lower)))
    print("Sorted words saved to sorted_words.txt")

def p20():
    with open("first.txt", "r", encoding="utf-8") as f1:
        a = f1.read()
    with open("second.txt", "r", encoding="utf-8") as f2:
        b = f2.read()
    with open("merged.txt", "w", encoding="utf-8") as out:
        out.write(a + "\n" + b)
    print("Merged into merged.txt")

def p21():
    rows = [["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 20, 76]]
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)
    print("students.csv created.")

def p22():
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            print(row)

def p23():
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    marks = [float(r["Marks"]) for r in rows if r.get("Marks", "").strip()]
    print("Average marks:", sum(marks) / len(marks) if marks else "No numeric marks.")

def p24():
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    print("Data rows:", max(0, len(rows) - 1))
    print("Columns:", len(rows[0]) if rows else 0)

def p25():
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(["Neha", 22, 88])
    print("New record appended.")

def p26():
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as src:
        rows = list(csv.reader(src))
    with open("students_copy.csv", "w", newline="", encoding="utf-8") as dst:
        csv.writer(dst).writerows(rows)
    print("Copied to students_copy.csv")

def p27():
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            print("Name:", row["Name"], "| Marks:", row["Marks"])

def p28():
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if rows:
        best = max(rows, key=lambda r: float(r["Marks"]))
        print("Highest marks:", best["Name"], "-", best["Marks"])
    else:
        print("No student records found.")

def p29():
    name = input("Enter student name: ").strip().lower()
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        found = [r for r in csv.DictReader(f) if r["Name"].lower() == name]
    if found:
        for row in found:
            print(row)
    else:
        print("Student not found.")

def p30():
    files = [CSV_FILE, "extra_students.csv"]
    with open("combined.csv", "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        for index, filename in enumerate(files):
            with open(filename, "r", newline="", encoding="utf-8") as src:
                for row_num, row in enumerate(csv.reader(src)):
                    if index > 0 and row_num == 0:
                        continue
                    writer.writerow(row)
    print("Combined data saved to combined.csv")

PROGRAMS = {
    1: ("Create and write a text file", p01),
    2: ("Read entire file", p02),
    3: ("Read line by line", p03),
    4: ("Count words", p04),
    5: ("Count lines and characters", p05),
    6: ("Display even-numbered lines", p06),
    7: ("Write multiple user lines", p07),
    8: ("Append content", p08),
    9: ("Copy text file", p09),
    10: ("Convert content to uppercase", p10),
    11: ("Search a word", p11),
    12: ("Count a specific word", p12),
    13: ("Sum and average numbers", p13),
    14: ("Display longest line", p14),
    15: ("Replace a word", p15),
    16: ("Display first and last lines", p16),
    17: ("Remove blank lines", p17),
    18: ("Save unique words", p18),
    19: ("Sort words alphabetically", p19),
    20: ("Merge two text files", p20),
    21: ("Create CSV file", p21),
    22: ("Read CSV file", p22),
    23: ("Average of marks", p23),
    24: ("Count CSV rows and columns", p24),
    25: ("Append CSV record", p25),
    26: ("Copy CSV file", p26),
    27: ("Display Name and Marks", p27),
    28: ("Find highest marks", p28),
    29: ("Search student by name", p29),
    30: ("Combine CSV files", p30),
}

def main():
    ensure_sample_files()
    while True:
        print("\\n===== PYTHON FILE HANDLING LAB: MENU =====")
        for number, (title, _) in PROGRAMS.items():
            print(f"{number}. {title}")
        print("0. Exit")
        try:
            choice = int(input("Enter program number (0-30): "))
            if choice == 0:
                print("Program ended.")
                break
            if choice in PROGRAMS:
                print("\\n--- Output ---")
                PROGRAMS[choice][1]()
            else:
                print("Please enter a number from 0 to 30.")
        except (ValueError, FileNotFoundError, KeyError) as error:
            print("Error:", error)

if __name__ == "__main__":
    main()
