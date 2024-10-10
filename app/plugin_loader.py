import os
import importlib

def load_plugins():
    commands = {}
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    
    for filename in os.listdir(plugins_dir):
        if filename.endswith('.py'):  
            module_name = f'app.plugins.{filename[:-3]}'  
            try:
                module = importlib.import_module(module_name)  
                command_class = module.get_command() 
                
                command_instance = command_class() 
                
                
                if command_instance.name in commands:
                    print(f"Warning: Command '{command_instance.name}' is already defined. Skipping.")
                else:
                    commands[command_instance.name] = command_instance  
            except AttributeError:
                print(f"Error: Plugin {module_name} does not have 'get_command()'. Skipping.")
    
    return commands
