class Command:
    name = 'multiply'
    
    def execute(self, a, b):
        return a * b

def get_command():
    return Command