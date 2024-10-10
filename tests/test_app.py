import pytest
from app import App
from app.plugin_loader import load_plugins

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    app = App()  
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app.start()  
    out, err = capfd.readouterr()
    assert "Welcome to the Calculator. Type 'menu' to see commands or 'exit' to exit." in out
    assert "Exiting..." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    app = App()  
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()  
    out, err = capfd.readouterr()
    assert "Welcome to the Calculator. Type 'menu' to see commands or 'exit' to exit." in out
    assert "Unknown command. Type 'menu' to list available commands." in out
    assert "Exiting..." in out

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL shows available commands when 'menu' is typed."""
    app = App()
    
    
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    app.start()
    
    out, err = capfd.readouterr()
    assert "Available commands" in out
    assert "Exiting..." in out


def test_app_invalid_command(capfd, monkeypatch):
    """Test how the REPL handles invalid input."""
    app = App()
    inputs = iter(['invalid_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, err = capfd.readouterr()
    assert "Unknown command. Type 'menu' to list available commands." in out

def test_invalid_number_input(capfd, monkeypatch):
    """Test how REPL handles invalid number input."""
    app = App()
    inputs = iter(['add a b', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, err = capfd.readouterr()
    assert "Error: Please provide valid numbers." in out

def test_extra_arguments(capfd, monkeypatch):
    """Test how REPL handles too many arguments."""
    app = App()
    inputs = iter(['add 1 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, err = capfd.readouterr()
    assert "Invalid input. Please provide a command followed by two numbers." in out

def test_plugin_loader():
    plugins = load_plugins()
    assert isinstance(plugins, dict)  
    assert len(plugins) > 0  
    assert all(hasattr(plugin, 'execute') for plugin in plugins.values())  