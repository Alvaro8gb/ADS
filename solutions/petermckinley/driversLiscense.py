import sys

class DriversLiscenseSystem:
    def __init__(self):
        # index maps dni -> points | arr[i] = number of drivers with i points
        self.index = {}  # O(1) access/update
        self.arr = [0] * 16  # O(1) fixed-size array for points 0–15

    def nuevo(self, dni):
        # Time: O(1)
        if dni in self.index:  # O(1)
            return "ERROR: Conductor duplicado"
        self.index[dni] = 15  # O(1)
        self.arr[15] += 1     # O(1)

    def quitar(self, dni, puntos):
        # Time: O(1)
        if dni not in self.index:  # O(1)
            return "ERROR: Conductor inexistente"
        
        self.arr[self.index[dni]] -= 1  # O(1)
        self.index[dni] -= puntos       # O(1)
        
        # Clamp value to [0, 15] (O(1))
        if self.index[dni] < 0:
            self.index[dni] = 0
        if self.index[dni] > 15:
            self.index[dni] = 15
        
        self.arr[self.index[dni]] += 1  # O(1)

    def consultar(self, dni):
        # Time: O(1)
        if dni not in self.index:  # O(1)
            return "ERROR: Conductor inexistente"
        return f"Puntos de {dni}: {self.index[dni]}"

    def cuantos_con_puntos(self, puntos):
        # Time: O(1)
        if puntos < 0 or puntos > 15:  # O(1)
            return "ERROR: Puntos no válidos"
        return f"Con {puntos} puntos hay {self.arr[puntos]}"


# Reads input file and returns list of stripped command lines
def convert_file_to_commands(filename):
    # Time: O(n) where n is number of lines
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


# Executes a sequence of commands, returns result lines
def process_operations(operations):
    system = DriversLiscenseSystem()
    output = []

    for op in operations:  # Time: O(m), m = number of commands
        parts = op.split()
        if not parts:
            continue
        command = parts[0]

        try:
            if command == "nuevo":
                result = system.nuevo(parts[1])
                if result is not None:
                    output.append(result)
            elif command == "quitar":
                result = system.quitar(parts[1], int(parts[2]))
                if result is not None:
                    output.append(result)
            elif command == "consultar":
                output.append(system.consultar(parts[1]))
            elif command == "cuantos_con_puntos":
                output.append(system.cuantos_con_puntos(int(parts[1])))
            elif command == "FIN":
                output.append("---")
                break
            else:
                output.append("ERROR: Comando no válido\n")
        except Exception:
            output.append("ERROR")

    return [line for line in output if line is not None]


def main():
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
