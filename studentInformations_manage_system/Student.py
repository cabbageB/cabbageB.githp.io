class Student():
    def __init__(self, name: str, gender: str, age: int, stu_number: str, phone_number: str, address: str):
        self.name = name
        self.gender = gender
        self.age = age
        self.stu_number = stu_number
        self.phone_number = phone_number
        self.address = address

    def __eq__(self, other):
        return self.stu_number == other.stu_number


if __name__ == '__main__':
    student1 = Student("Araon", '男', 30, "12335678", "A417", "重庆")
    student2 = Student("steven", '男', 28, stu_number="12234565", phone_number="A4117", address="重庆")
    print(student1 == student2)
