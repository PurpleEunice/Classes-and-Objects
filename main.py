class Student:
    # [assignment] Skeleton class. Add your code here
    def _init_(self, name, age, grade, score):
        def change_name(self):
            self.name = name
        def change_age(self):
            self.age = age
        def add_track(self):
            self.grade.append(grade)
        def get_score(self):
            return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
