import re
import pickle
import os


STUDENT_FILE = "students.dat"
LESSON_FILE = "lessons.dat"
SELECTION_FILE = "selections.dat"

def show_menu():
    print("1) student")
    print("2) lesson")
    print("3) select lesson")
    print("4) report by student")
    print("5) report by lesson")
    print("0) Exit")
    choice = int(input("Enter your choice: "))
    print("-" * 60)
    return choice


def validated_name(name):
    return bool(re.match(r"^[a-zA-Z]{3,30}$",name,re.I))

def validated_code(code_student):
    return bool(re.match(r"^[0-9]{2,30}$", code_student,re.I))


def get_student():
    print("1) add")
    print("2) edit")
    print("3) remove")
    print("0) return")
    choice = int(input("Enter your choice: "))
    print("-" * 60)
    return choice

def get_student_add():

    code_student = input("Enter code: ")
    if not validated_code(code_student):
        print("Your code is not invalid")

    name_student = input("Enter name: ")
    if not validated_name(name_student):
        print("Your name is not invalid")

    family_student = input("Enter family: ")
    if not validated_name(family_student):
        print("Your family is not invalid")

    return {"code_student": code_student,"name_student": name_student,"family_student": family_student}


def get_lesson():
    print("1) add")
    print("2) edit")
    print("3) remove")
    print("0) return")
    choice = int(input("Enter your choice: "))
    print("-" * 60)
    return choice

def get_lesson_add():

        code_lesson= input("Enter code: ")
        if not validated_code(code_lesson):
            print("Your name is not invalid")

        name_lesson = input("Enter name lesson : ")
        if not validated_name(name_lesson):
            print("Your name is not invalid")


        lesson= {"code_lesson": code_lesson, "name_lesson": name_lesson}
        return lesson


def tekrari_code_lesson(lesson_list, new_lesson):
    filter_list = list(filter(lambda tekrari: tekrari["code_lesson"] == new_lesson["code_lesson"], lesson_list))
    if filter_list !=[]:
        print("tekrari ")
        return False
    else:
        return True

def tekrari_code_student( student_list,new_student):
    filter_list = list(filter(lambda tekrari: tekrari["code_student"] == new_student["code_student"] , student_list))
    if filter_list !=[]:
        print("tekrari ")
        return False
    else:
        return True


def show_all_students(student_list):
    print("Students List:")
    for student in student_list:
        print(
            f"Code: {student['code_student']} | Name: {student['name_student']} | Family: {student['family_student']}")
    print("-" * 60)

def show_all_lessons(lesson_list):
    print("Lessons List:")
    for lesson in lesson_list:
        print(f"Code: {lesson['code_lesson']} | Name: {lesson['name_lesson']}")
    print("-" * 60)



def edit_student(student_list):
    show_all_students(student_list)
    try:
        code = input("Enter student code to edit : ")
        if code == '0':
            return student_list


        code = int(code)

        for student in student_list:

            if int(student['code_student']) == code:
                print("student information:")
                print(f"1. Code: {student['code_student']}")
                print(f"2. Name: {student['name_student']}")
                print(f"3. Family: {student['family_student']}")
                print("0. back to menu ")

                while True:
                    field = input("Enter field number to edit : ")
                    if field == '1':
                        new_code = input("Enter new code: ")
                        if not validated_code(new_code):
                            print("Invalid code format!")
                            continue
                        student['code_student'] = new_code
                        break
                    elif field == '2':
                        new_name = input("Enter new name: ")
                        if not validated_name(new_name):
                            print("Invalid name format!")
                            continue
                        student['name_student'] = new_name
                        break
                    elif field == '3':
                        new_family = input("Enter new family: ")
                        if not validated_name(new_family):
                            print("Invalid family format!")
                            continue
                        student['family_student'] = new_family
                        break
                    elif field == '0':
                        return student_list
                    else:
                        print("Invalid choice!")

                print("Student updated successfully!")
                return student_list

        print("Student not found!")
        return student_list
    except ValueError:
        print("Invalid input! Please enter a number.")
        return student_list

def remove_student(student_list):

    show_all_students(student_list)
    try:
        code = input("Enter student code to remove : ")
        if code == 0:
            return student_list
        if not validated_code(code):
            print("invalid code")
            return student_list
        code = int(code)

        filter_student = list(filter(lambda remove: int(remove["code_student"]) != code, student_list))
        if len(filter_student) == len(student_list):
            print ("student not found!")
        else:
            print("Student removed successfully!")
            student_list =filter_student
        return student_list
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return student_list


def edit_lesson(lesson_list):
    show_all_lessons(lesson_list)
    try:
        code = input("Enter lesson code to edit : ")
        if code == '0':
            return lesson_list


        code = int(code)

        for lesson in lesson_list:

            if int(lesson['code_lesson']) == code:
                print("lesson information:")
                print(f"1. Code: {lesson['code_lesson']}")
                print(f"2. Name: {lesson['name_lesson']}")
                print("0. back to menu ")

                while True:
                    field = input("Enter field number to edit : ")
                    if field == '1':
                        new_code = input("Enter new code: ")
                        if not validated_code(new_code):
                            print("Invalid code format!")
                            continue
                        lesson['code_lesson'] = new_code
                        break
                    elif field == '2':
                        new_name = input("Enter new name: ")
                        if not validated_name(new_name):
                            print("Invalid name format!")
                            continue
                        lesson['name_lesson'] = new_name
                        break
                    elif field == '0':
                        return lesson_list
                    else:
                        print("Invalid choice!")

                print("Lesson updated successfully!")
                return lesson_list

        print("Lesson not found!")
        return lesson_list
    except ValueError:
        print("Invalid input! Please enter a number.")
        return lesson_list

def remove_lesson(lesson_list):

    show_all_lessons(lesson_list)
    try:
        code = input("Enter lesson code to remove : ")
        if code == 0:
            return lesson_list

        if not validated_code(code):
            print("invalid code")
            return lesson_list

        code = int(code)
        filter_lesson = list(filter(lambda remove_les: int(remove_les["code_lesson"]) != code, lesson_list))
        if len(filter_lesson) == len(lesson_list):
            print ("student not found!")
        else:
            print("Student removed successfully!")
            lesson_list =filter_lesson
        return lesson_list
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return lesson_list


def get_selected_lesson():
    print("1) add")
    print("0) return")
    choice = int(input("Enter your choice: "))
    print("-" * 60)
    return choice

def select_lesson_for_student(student_list, lesson_list):
    show_all_students(student_list)
    show_all_lessons(lesson_list)

    try:

        student_code = input("Enter student code to select lesson : ")
        if student_code == '0':
            return

        lesson_code = input("Enter lesson code to add : ")
        if lesson_code == '0':
            return

        if not validated_code(student_code) or not validated_code(lesson_code):
            print("Invalid code ")
            return

        student_code = int(student_code)
        lesson_code = int(lesson_code)



        student = None
        for s in student_list:
            if int(s['code_student']) == student_code:
                student = s
                break
        lesson = None
        for l in lesson_list:
            if int(l['code_lesson']) == lesson_code:
                lesson = l
                break


        if  student is None:
            print("Student not found!")
            return

        if  lesson is None:
            print("Lesson not found!")
            return


        if 'selected_lessons' not in student:
            student['selected_lessons'] = []

        if lesson in student['selected_lessons']:
            print("This lesson is already selected for the student!")
        else:
            student['selected_lessons'].append(lesson)
            print(f"Lesson '{lesson['name_lesson']}' added to student '{student['name_student']}'")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")



def report_student(student_list):
    if not student_list:
        print("No students available!")
        return
    sorted_list = sorted(student_list, key=lambda student: student["name_student"])
    print("Report by Student:")
    print("-" * 25)
    print(f"{'code':<5} {'name':<10} {'family':<10}")
    print("-" * 25)

    for student in sorted_list:
        print(f"{student['code_student']:<5} {student['name_student']:<10} {student['family_student']:<10}: ")
        print("\t\t{:<5} {:<15}".format("code", "name_lesson"))
        print("\t\t" + "-" * 23)

        if 'selected_lessons' not in student or not student['selected_lessons']:
            print("\t\tNo lessons selected")
        else:
            for lesson in student['selected_lessons']:
                print("\t\t{:<5} {:<15}".format(lesson['code_lesson'], lesson['name_lesson']))

        print()

    print("-" * 60)

def report_lesson(lesson_list, student_list):
    if not lesson_list:
        print("No lessons available!")
        return
    sorted_list = sorted(lesson_list, key=lambda lesson: lesson["name_lesson"])
    print("report by lesson")
    print("-" * 20)
    print(f"{'code':<5} {'name':<15}")
    print("-" * 20)

    for lesson in sorted_list:
        print(f"{lesson['code_lesson']:<5} {lesson['name_lesson']:<15}:")

        print("\t\t{:<5} {:<10} {:<10}".format("code", "name", "family"))
        print("\t\t" + "-" * 28)

        students_with_lesson = []
        for student in student_list:
            if 'selected_lessons' in student:
                for selected in student['selected_lessons']:
                    if selected['code_lesson'] == lesson['code_lesson']:
                        students_with_lesson.append(student)
                        break

        if not students_with_lesson:
            print("\t\tNo students selected this lesson")
        else:
            for student in students_with_lesson:
                print("\t\t{:<5} {:<10} {:<10}".format(
                    student['code_student'],
                    student['name_student'],
                    student['family_student']
                ))

        print()
def save_repr(data, filename):

    try:
        with open(filename, 'w') as f:
            if isinstance(data, dict):
                f.write("{\n")
                for i, (key, value) in enumerate(data.items()):
                    f.write(f"    {repr(key)}: {repr(value)}")
                    if i < len(data) - 1:
                        f.write(",\n")
                    else:
                        f.write("\n")
                f.write("}")
            else:
                f.write(repr(data))
        return True
    except Exception as e:
        print(f"Error saving {filename}: {e}")
        return False


def load_repr(filename):

    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return eval(f.read())
        return None
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return None


def save_data(student_list, lesson_list):
    try:

        students_to_save = []
        for student in student_list:
            student_copy = student.copy()
            if 'selected_lessons' in student_copy:
                del student_copy['selected_lessons']
            students_to_save.append(student_copy)

        if not save_repr(student_list, STUDENT_FILE):
            return False


        if not save_repr(lesson_list, LESSON_FILE):
            return False


        selections = {}
        for student in student_list:
            if 'selected_lessons' in student:
                selections[student['code_student']] = student['selected_lessons']

                if not save_repr(selections, SELECTION_FILE):
                    return False

        return True

    except Exception as e:
        print(f"Error in save_data: {e}")
        return False


def load_data():
    try:

        student_list = load_repr(STUDENT_FILE)
        if student_list is None:
            student_list = []


        lesson_list = load_repr(LESSON_FILE)
        if lesson_list is None:
            lesson_list = []


        selections = load_repr(SELECTION_FILE)
        if selections is None:
            selections = {}


        for student in student_list:
            if student['code_student'] in selections:
                student['selected_lessons'] = selections[student['code_student']]

        return student_list, lesson_list

    except Exception as e:
        print(f"Error in load_data: {e}")
        return [], []

