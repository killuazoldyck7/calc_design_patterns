import os
import logging
from dotenv import load_dotenv
from app.plugin_loader import load_plugins
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

class App:
    def __init__(self):
        load_dotenv()
        
        environment = os.getenv('ENVIRONMENT', 'production')  
        logging.info(f"Running in {environment} mode")

        self.commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand()
        }

        self.commands.update(load_plugins())

    def start(self) -> None:
        logging.info("Application started.")
        print("Welcome to the Calculator. Type 'menu' to see commands or 'exit' to exit.")
        
        while True:
            user_input = input(">>> ").strip().lower()
            if user_input == "exit":
                logging.info("Exiting application.")
                print("Exiting...")
                break
            elif user_input == "menu":
                print(f"Available commands: {', '.join(self.commands.keys())}")
            else:
                parts = user_input.split()
                if len(parts) == 0:
                    logging.warning("Error: No command entered.")
                    print("Error: Please enter a command.")
                    continue

                command_name = parts[0]
                if command_name not in self.commands:
                    logging.warning("Unknown command entered.")
                    print(f"Unknown command. Type 'menu' to list available commands.")
                    continue

                if len(parts) != 3:
                    logging.warning("Invalid input format.")
                    print("Invalid input. Please provide a command followed by two numbers.")
                    continue

                try:
                    a, b = map(float, parts[1:])
                    result = self.commands[command_name].execute(a, b)
                    logging.info(f"Executed {command_name} command with values: {a}, {b}. Result: {result}")
                    print(f"Result: {result}")
                except ValueError:
                    logging.error("Value error: Invalid number input.")
                    print("Error: Please provide valid numbers.")
                except ZeroDivisionError:
                    logging.error("Attempted division by zero.")
                    print("Error: Division by zero is not allowed.")
