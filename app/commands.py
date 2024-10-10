class Command:
    def execute(self, *args):
        raise NotImplementedError("Subclasses should implement this!")

class AddCommand(Command):
    def execute(self, a, b):
        return a + b

class SubtractCommand(Command):
    def execute(self, a, b):
        return a - b

class MultiplyCommand(Command):
    def execute(self, a, b):
        return a * b

class DivideCommand(Command):
    def execute(self, a, b):
        if abs(b) < 1e-9: 
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

