import json
import os


def create_student(name: str, age: int, grade: float) -> dict:

    return {"name": name, "age": age, "grade": grade}


DATA_FILE = "students.json"

def save_to_file(students: list) -> None:

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)
    print(f"✅ Деректер '{DATA_FILE}' файлына сақталды.")


def load_from_file() -> list:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def add_student(students: list, name: str, age: int, grade: float) -> list:
    students.append(create_student(name, age, grade))
    print(f"✅ '{name}' тізімге қосылды.")
    return students


def search_student(students: list, keyword: str) -> list:
    keyword = keyword.lower()
    results = [s for s in students if keyword in s["name"].lower()]
    return results


def sort_students(students: list, by: str = "name") -> list:
    if by not in ("name", "grade", "age"):
        print("⚠️ Сұрыптау өрісі: 'name', 'grade', 'age'")
        return students
    return sorted(students, key=lambda s: s[by])



def print_students(students: list, title: str = "Студенттер тізімі") -> None:
    if not students:
        print("📭 Тізім бос.")
        return
    print(f"\n{'─'*45}")
    print(f"  {title} ({len(students)} студент)")
    print(f"{'─'*45}")
    print(f"  {'Аты':<20} {'Жасы':>5} {'Бағасы':>8}")
    print(f"{'─'*45}")
    for s in students:
        print(f"  {s['name']:<20} {s['age']:>5} {s['grade']:>8.1f}")
    print(f"{'─'*45}\n")


def run_tests():
    print("🧪 Тестілеу басталды...\n")

    students = []
    students = add_student(students, "Айгерім Бекова", 20, 4.5)
    students = add_student(students, "Дәурен Сейтов", 21, 3.8)
    students = add_student(students, "Мадина Жанова", 19, 4.9)
    students = add_student(students, "Асқар Нұров", 22, 3.2)

    print_students(students)

    found = search_student(students, "Мадина")
    print_students(found, "Іздеу нәтижесі: 'Мадина'")

    sorted_by_grade = sort_students(students, by="grade")
    print_students(sorted_by_grade, "Баға бойынша сұрыпталған")

    save_to_file(students)
    loaded = load_from_file()
    print_students(loaded, "Файлдан жүктелген деректер")

    print("✅ Барлық тесттер сәтті өтті!")


if __name__ == "__main__":
    run_tests()