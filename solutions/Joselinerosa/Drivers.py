import sys
class Student:
    def __init__(self, name, surname="", phone=""):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.score = 0
        self.instructor = None

class Instructor:
    def __init__(self, name, surname="", phone=""):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.students = set()

class DrivingSchool:
    def __init__(self):
        self.students = {}
        self.instructors = {}

    def alta(self, A, P, surname_A="", phone_A="", surname_P="", phone_P=""): #O(1)
        if P not in self.instructors:
            self.instructors[P] = Instructor(P, surname_P, phone_P)
            
        if A not in self.students:
            self.students[A] = Student(A, surname_A, phone_A)
        else:
            prev_instructor = self.students[A].instructor
            if prev_instructor in self.instructors:
                self.instructors[prev_instructor].students.discard(A)
        
        self.students[A].instructor = P  
        self.instructors[P].students.add(A)

    def es_alumno(self, A, P): #O(1)
        if A in self.students and self.students[A].instructor == P:
            return f"{A} es alumno de {P}"
        return f"{A} no es alumno de {P}"

    def puntuacion(self, A): #O(1)
        if A not in self.students:
            return "ERROR"
        return f"Puntuacion de {A}: {self.students[A].score}"

    def actualizar(self, A, N): #O(1)
        if A not in self.students:
            return "ERROR"
        self.students[A].score += N
        return None

    def examen(self, P, X): #O(nlogn)
        if P not in self.instructors:
            return []
        return sorted([A for A in self.instructors[P].students if self.students[A].score >= X])

    def aprobar(self, A): #O(1)
        if A not in self.students:
            return "ERROR"
        
        instructor = self.students[A].instructor
        if instructor and instructor in self.instructors:
            self.instructors[instructor].students.discard(A)
        
        del self.students[A]
        return None

def process_operations(operations):
    school = DrivingSchool()
    output = []
    
    for op in operations:
        parts = op.strip().split()
        if not parts:
            continue
        
        cmd = parts[0]
        current_output = []
        
        try:
            if cmd == "alta":
                A, P = parts[1], parts[2]
                school.alta(A, P)
            elif cmd == "es_alumno":
                A, P = parts[1], parts[2]
                result = school.es_alumno(A, P)
                current_output.append(result)
            elif cmd == "puntuacion":
                A = parts[1]
                result = school.puntuacion(A)
                current_output.append(result)
            elif cmd == "actualizar":
                A, N = parts[1], int(parts[2])
                result = school.actualizar(A, N)
                if result == "ERROR":
                    current_output.append("ERROR")
            elif cmd == "examen":
                P, N = parts[1], int(parts[2])
                students = school.examen(P, N)
                
                current_output.append(f"Alumnos de {P} a examen:")
                current_output.extend(students)  # Each student on a new line
            elif cmd == "aprobar":
                A = parts[1]
                result = school.aprobar(A)
                if result == "ERROR":
                    current_output.append("ERROR")
        except Exception:
            current_output = ["ERROR"]  
        
        output.extend(current_output)
    
    return output

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file")
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as f:
        current_case = []
        for line in f:
            cleaned = line.strip()
            if cleaned == "FIN":
                if current_case:
                    results = process_operations(current_case)
                    print('\n'.join(results))
                    print("---")
                    current_case = []
            else:
                current_case.append(cleaned)
        
        if current_case: 
            results = process_operations(current_case)
            print('\n'.join(results))
            print("---")

if __name__ == "__main__":
    main()
