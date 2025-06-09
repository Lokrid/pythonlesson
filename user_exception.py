class GroupFullException(Exception):
    def __init__(
        self,
        message="There are already 10 students in the group. It is not possible to add more.",
    ):
        super().__init__(message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record book: {self.record_book}"

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.record_book))

    def __eq__(self, other):
        return (
            isinstance(other, Student)
            and self.first_name == other.first_name
            and self.last_name == other.last_name
        )


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullException()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(stud) for stud in self.group)
        return f"Number:{self.number}\n{all_students} "


gr = Group("PD1")

for people in range(10):
    st = Student(
        "Male", 30 + people, f"Student{people+1}", f"Last{people+1}", f"RB{people+1}"
    )
    gr.add_student(st)

try:
    extra = Student("Female", 22, "Extra", "Last11", "RB11")
    gr.add_student(extra)
except GroupFullException as _except:
    print("Error", _except)
