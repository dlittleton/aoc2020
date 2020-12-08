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


    def execute(self):
        while True:
            if self.ip == len(self.instructions):
                return True
            elif self.next_instruction.n > 0:
                return False

            self.next_instruction.execute(self)

    
    def reset(self):
        self.acc = 0
        self.ip = 0
        for i in self.instructions:
            i.n = 0


    def search(self):
        for index, instruction in enumerate(self.instructions):
            original = instruction.op
            if original == 'acc':
                continue
            elif original == 'jmp':
                instruction.op = 'nop'
            elif original == 'nop':
                instruction.op = 'jmp'

            result = self.execute()
            if result:
                return index
                
            self.reset()
            instruction.op = original


    
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
    

print(p.search())
print(p.acc)