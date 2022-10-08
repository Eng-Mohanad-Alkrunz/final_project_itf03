from models import Student,Course
import  random

student_list = []
courses_list = []

def get_courses_list(courses):
    print("ID\t\t|Name\t\t|Class")
    for course in courses:
        course.get_course_details()


def get_students_details(students):

    print("ID\t\t|Name\t\t|Class")
    for student in students:
        print(student.get_student_details())


def find_student(student_id,students):
    index = 0
    for student in students:
        if student.student_id == student_id:
            return index
        index += 1
    return -1


def find_course(course_id,courses):
    index = 0
    for course in courses:
        if course.course_id == course_id:
            return index
        index += 1
    return -1


while True:
    selection = int(input("Select Choice Please\n1.Add New Student\n2.Remove Student"
                          "\n3.Edit Student\4.Display All Students\n5.Create New Course"
                          "\n6.Add Course To Student"
                          "\n7.Exit"))

    if selection == 1:
        student_name = input("Enter Student Name")
        while True:
            student_class = input("Select Student Class (A-B-C)")
            if student_class in ('A','B','C'):
                break
        student_id = len(student_list) + 1
        student = Student(student_id,student_name,student_class)
        student_list.append(student)
        print("Student Created Successfully")
    elif selection == 2:
        get_students_details(student_list)
        student_id = int(input("Enter Student ID"))
        student_index = find_student(student_id,student_list)
        if student_index == -1 :
            print("Student Not Exist")
        else:
            student_list.pop(student_index)
            print("Student Removed Successfully")
            get_students_details(student_list)

    elif selection == 3:
        get_students_details(student_list)
        student_id = int(input("Enter Student ID"))
        student_index = find_student(student_id, student_list)
        if student_index == -1:
            print("Student Not Exist")
        else:
            student_name = input("Enter Student Name")
            while True:
                student_class = input("Select Student Class (A-B-C)")
                if student_class in ('A', 'B', 'C'):
                    break
            student_list[student_index].student_name = student_name
            student_list[student_index].student_class = student_class
            print("Student Details Updated Successfully")
    elif selection == 4:
        get_students_details(student_list)
    elif selection == 5:
        course_name = input("Enter Course Name")
        while True:
            course_class = input("Select Course Class (A-B-C)")
            if course_class in ('A','B','C'):
                break
        course_id = len(courses_list) + 1
        course = Course(course_id,course_name,course_class)
        courses_list.append(course)
        print("Course Created Successfully")
    elif selection == 6:
        get_courses_list(courses_list)
        student_id = int(input("Enter Student ID"))
        student_index = find_student(student_id,student_list)
        if student_index == -1:
            print("Student Not Exist")
        else:
            course_id = int(input("Enter Course ID"))
            course_index = find_course(course_id,courses_list)
            if course_index == -1:
                print("Course Not Exist")
            else:
                student_list[student_index].enroll_course(courses_list[course_index])
    else:
        exit()