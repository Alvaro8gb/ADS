import sys

class School:
    def __init__(self):
        self.allStudents = {}  # student -> instructor (dict)
        self.instructors = []  # list of Instructor objects

    def puntuacion(self, student):
        # Time: O(1)
        instructor = self.allStudents.get(student)
        if instructor is not None:
            return instructor.students[student]  # O(1)
        return "Error"

    def alta(self, student, instruct_name):
        # Time: O(n) where n = number of instructors
        instructor = None
        for person in self.instructors:  # O(n)
            if instruct_name == person.firstName:
                instructor = person
                break

        if instructor is None:
            instructor = Instructor(instruct_name)
            self.instructors.append(instructor)  # O(1) amortized

        temp_points = 0
        if student in self.allStudents:  # O(1)
            current_instructor = self.allStudents[student]
            if current_instructor != instructor:
                temp_points = current_instructor.students.get(student, 0)  # O(1)
                current_instructor.students.pop(student, None)  # O(1)
            else:
                return

        self.allStudents[student] = instructor  # O(1)
        instructor.students[student] = temp_points  # O(1)

    def es_alumno(self, student, instructor_name):
        # Time: O(1)
        if student in self.allStudents:
            instructor = self.allStudents[student]  # O(1)
            if instructor.firstName == instructor_name:
                if student in instructor.students:  # O(1)
                    return f"{student} es alumno de {instructor_name}"
        return f"{student} no es alumno de {instructor_name}"

    def actualizar(self, student, points):
        # Time: O(1)
        instructor = self.allStudents.get(student)  # O(1)
        if instructor is not None:
            instructor.students[student] += points  # O(1)
            return
        return f"El alumno {student} no esta matriculado."

    def examen(self, instructor_name, points):
        # Time: O(n + m log m), 
        # where n = number of instructors, m = number of students for instructor
        instructor_obj = None
        for person in self.instructors:  # O(n)
            if instructor_name == person.firstName:
                instructor_obj = person
                break

        if instructor_obj is None:
            return []

        eligible = [s for s in instructor_obj.students if instructor_obj.students[s] >= points]  # O(m)
        eligible.sort()  # O(m log m)
        return eligible

    def aprobar(self, student):
        # Time: O(1)
        instructor = self.allStudents.get(student)  # O(1)
        if instructor is not None:
            instructor.students.pop(student, None)  # O(1)
        self.allStudents.pop(student, None)  # O(1)


class Instructor:
    def __init__(self, name):
        self.firstName = name
        self.lastName = ""
        self.address = ""
        self.students = {}  # student -> points (dict)


def convert_file_to_commands(filename):
    # Time: O(k) where k = number of lines in file
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]  # O(k)


def process_operations(operations):
    # Time: O(t), t = total number of operations
    school = School()
    output = []

    for command in operations:
        parts = command.strip().split()
        if not parts:
            continue

        op = parts[0]
        try:
            if op == "alta":
                result = school.alta(parts[1], parts[2])  # O(n)
                if result is not None:
                    output.append(result)
            elif op == "puntuacion":
                result = school.puntuacion(parts[1])  # O(1)
                if result == "Error":
                    output.append(f"El alumno {parts[1]} no esta matriculado")
                else:
                    output.append(f"Puntuacion de {parts[1]}: {result}")
            elif op == "es_alumno":
                output.append(school.es_alumno(parts[1], parts[2]))  # O(1)
            elif op == "actualizar":
                result = school.actualizar(parts[1], int(parts[2]))  # O(1)
                if result is not None:
                    output.append(result)
            elif op == "examen":
                temp = school.examen(parts[1], int(parts[2]))  # O(n + m log m)
                output.append(f"Alumnos de {parts[1]} a examen:")
                for student in temp:
                    output.append(student)
            elif op == "aprobar":
                result = school.aprobar(parts[1])  # O(1)
                if result is not None:
                    output.append(result)
            elif op == "FIN":
                output.append("---")
                break
            else:
                output.append("ERROR: Comando no valido\n")
        except (IndexError, ValueError):
            output.append("ERROR")

    return [line for line in output if line is not None]


def main():
    # Time: O(total input size)
    if len(sys.argv) < 2:
        raise Exception("Usage: python script.py <input_file>")

    input_file = sys.argv[1]
    operations = convert_file_to_commands(input_file)

    test_case = []
    for line in operations:
        if line == "FIN":
            if test_case:
                print("\n".join(process_operations(test_case)))
                print("---")
                test_case = []
        else:
            test_case.append(line)


if __name__ == "__main__":
    main()
