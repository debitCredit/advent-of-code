import re

class Processor:
    def __init__(self, registers, program):
        self.registers = registers
        self.program = program
        self.inst_pointer = 0
        self.output = []

        self.func_map = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }

    def combo_operand(self, operand: int):
        match operand:
            case n if n in range(4):
                return operand
            case 4:
                return self.registers["A"]
            case 5:
                return self.registers["B"]
            case 6:
                return self.registers["C"]

    def adv(self, operand: int):
        calc_operand = self.combo_operand(operand)
        self.registers["A"] //= 2 ** calc_operand
        self.inst_pointer += 2

    def bxl(self, operand: int):
        self.registers["B"] ^= operand
        self.inst_pointer += 2

    def bst(self, operand: int):
        self.registers["B"] = self.combo_operand(operand) % 8
        self.inst_pointer += 2

    def jnz(self, operand: int):
        if self.registers["A"] != 0:
            self.inst_pointer = operand
        else:
            self.inst_pointer += 2

    def bxc(self, _):
        self.registers["B"] ^= self.registers["C"]
        self.inst_pointer += 2

    def out(self, operand: int):
        calc_operand = self.combo_operand(operand) % 8
        self.output.append(str(calc_operand))
        self.inst_pointer += 2

    def bdv(self, operand: int):
        calc_operand = self.combo_operand(operand)
        self.registers["B"] = self.registers["A"] // 2 ** calc_operand
        self.inst_pointer += 2

    def cdv(self, operand: int):
        calc_operand = self.combo_operand(operand)
        self.registers["C"] = self.registers["A"] // 2 ** calc_operand
        self.inst_pointer += 2

    def run(self):
        while self.inst_pointer < len(self.program):
            opcode = self.program[self.inst_pointer]
            operand = self.program[self.inst_pointer + 1]
            self.func_map[opcode](operand)
        
        return ",".join(self.output)


def parse_registers_and_program(text):
    register_pattern = r'Register ([ABC]): (\d+)'
    registers = {key: int(value) for key, value in re.findall(register_pattern, text)}
    
    program_pattern = r'Program: ([\d,]+)'
    program_match = re.search(program_pattern, text)
    program = [int(x) for x in program_match.group(1).split(',')] if program_match else []
    
    return registers, program


file = "input.txt"  # or "test_input.txt"

with open(file) as f:
    text = f.read()

registers, program = parse_registers_and_program(text)
processor = Processor(registers, program)
result = processor.run()
print(result)