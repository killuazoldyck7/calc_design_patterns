class Command:
    name = 'divide'
    
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

def get_command():
    return Command
