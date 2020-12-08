import sys

class Program:

    def __init__(self):
        self.acc = 0
        self.ip = 0
        self.instructions = []

    
    def add_instruction(self, line):
        line = line.strip()
        op, arg = line.split()
        self.instructions.append(Operation(op, int(arg)))

    
    @property
    def next_instruction(self):
        return self.instructions[self.ip]


class Operation:

    def __init__(self, op, arg):
        self.op = op
        self.arg = arg
        self.n = 0


    def execute(self, program):
        self.n += 1
        if self.op == 'acc':
            program.acc += self.arg
        
        if self.op == 'jmp':
            program.ip += self.arg
        else:
            program.ip += 1


p = Program()
for line in sys.stdin:
    p.add_instruction(line)
    

while p.next_instruction.n == 0:
    p.next_instruction.execute(p)

print(p.acc)