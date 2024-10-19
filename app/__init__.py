import os
from dotenv import load_dotenv
from app.plugin_loader import load_plugins
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class App:
    def __init__(self):
        load_dotenv()
        
        environment = os.getenv('ENVIRONMENT', 'production')  
        print(f"Running in {environment} mode")

        self.commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand()
        }

        self.commands.update(load_plugins())

    def start(self) -> None:
        print("Welcome to the Calculator. Type 'menu' to see commands or 'exit' to exit.")
        
        while True:
            user_input = input(">>> ").strip().lower()
            if user_input == "exit":
                print("Exiting...")
                break
            elif user_input == "menu":
                print(f"Available commands: {', '.join(self.commands.keys())}")
            else:
                parts = user_input.split()
                if len(parts) == 0:
                    print("Error: Please enter a command.")
                    continue

                command_name = parts[0]
                if command_name not in self.commands:
                    print(f"Unknown command. Type 'menu' to list available commands.")
                    continue

                if len(parts) != 3:
                    print("Invalid input. Please provide a command followed by two numbers.")
                    continue

                try:
                    a, b = map(float, parts[1:])
                    result = self.commands[command_name].execute(a, b)
                    print(f"Result: {result}")
                except ValueError:
                    print("Error: Please provide valid numbers.")
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
