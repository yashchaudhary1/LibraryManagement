from Student import Student;

class Library:

    def __init__(self):
        self.studentRecord = self._getStudentRecord();
        print("Library is initialized")

    def _getStudentRecord(self):
            Student1 = Student("Yash", "5th", "A", "kanker khera,meerut")
            Student2 = Student("harsh", "7th", "C", "defence,meerut")
            Student3 = Student("ram", "11th", "b", "begum pull,meerut")
            Student4 = Student("goldie", "3rd", "A", "army colony, meerut")
            Student5 = Student("akshit", "12th", "A", "nehru colony,meerut")
            student_dictionary = {51: Student("Yash", "5th", "A", "kanker khera,meerut"),
                                  12: Student("harsh", "7th", "C", "defence,meerut"),
                                  33: Student("ram", "11th", "b", "begum pull,meerut"),
                                  23: Student("goldie", "3rd", "A", "army colony, meerut"),
                                  44: Student("akshit", "12th", "A", "nehru colony,meerut")}
            return student_dictionary

    def _printStudentRecord(self, studentRecord):
        for key, value in self.studentRecord.items():
            print(f"key: {key} | value: {value}")

lib_obj = Library()
lib_obj._printStudentRecord(lib_obj.studentRecord)



