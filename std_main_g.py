from std_module_g import *

lesson_list=[]
student_list=[]

def main():
    student_list, lesson_list = load_data()

    while True:
        try:
            option =show_menu()

            if option == 1:
                student_choice = get_student()

                if student_choice == 1:
                    new_student = get_student_add()
                    if new_student and tekrari_code_student(student_list, new_student):
                        student_list.append(new_student)
                        print("Student added successfully.")
                        save_data(student_list, lesson_list)
                    else:
                            print("Student code already exists!")

                elif student_choice == 2:
                    if not student_list:
                        print("No students available!")
                        continue
                    student_list = edit_student(student_list)
                    save_data(student_list, lesson_list)

                elif student_choice == 3:
                    if not student_list:
                        print("No students available!")
                        continue

                    student_list = remove_student(student_list)
                    save_data(student_list, lesson_list)

            elif option == 2:
                lesson_choice = get_lesson()

                if lesson_choice == 1:
                    new_lesson = get_lesson_add()
                    if new_lesson and tekrari_code_lesson(lesson_list, new_lesson):
                        lesson_list.append(new_lesson)
                        print("Lesson added successfully!")
                        save_data(student_list, lesson_list)
                    else:
                            print("duplicate lesson code")

                elif lesson_choice == 2:
                    if not lesson_list:
                        print("No lessons available!")
                        continue
                    lesson_list = edit_lesson(lesson_list)
                    save_data(student_list, lesson_list)
                elif lesson_choice == 3:
                    if not lesson_list:
                        print("No lessons available!")
                        continue
                    lesson_list = remove_lesson(lesson_list)
                    save_data(student_list, lesson_list)

            elif option == 3:
                select_choice = get_selected_lesson()

                if select_choice == 1:
                    if not student_list or not lesson_list:
                        print("You need to add students and lessons first!")
                        continue
                select_lesson_for_student(student_list, lesson_list)
                save_data(student_list, lesson_list)

            elif option == 4:
                report_student(student_list)

            elif option == 5:
                report_lesson(lesson_list,student_list)

            elif option == 0:
                print("Exit")
                save_data(student_list, lesson_list)
                break

            else:
                print("Sorry, invalid")

                print("-" * 50)

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("-" * 50)

if __name__ == "__main__":
    main()
