#1. For a grading project, we need to have students. I assume those are dictionaries.
john: dict = {"name": "John", "grade": "90"}
mary: dict = {"name": "Mary", "grade": "85"}
kate: dict = {"name": "Kate", "grade": "95"}

#2 We need to print their grades.
# Copilot suggests using typing hints, but that doesn't make sense unless I'm going to write out error messages.
# That looks like a lot of fun, but I'm going to drop that for now.
# ALso changed grades to strings, since printing doesn't like concatenation of ints.
def print_grade(student: dict):
    print(student["name"] + " got a " + student["grade"] + " on the test.")

#Test that it prints John's grade correctly; works
# print_grade(john)


# A list of students
students: list = [john, mary, kate]

# Cheated here since I don't know the syntax for loops yet
#Did learn the syntax for docstrings though, that's cool :D
def print_all_grades(students: list):
    '''
    Print all the students' grades
    '''
    for (student) in students:
        print_grade(student) 

# Test that it prints all grades
print_all_grades(students)