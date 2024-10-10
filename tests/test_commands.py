from app.plugins.add import Command as AddCommand
from app.plugins.subtract import Command as SubtractCommand
from app.plugins.multiply import Command as MultiplyCommand
from app.plugins.divide import Command as DivideCommand
import pytest

def test_add_command():
    add_cmd = AddCommand()
    result = add_cmd.execute(3, 4)
    assert result == 7

def test_subtract_command():
    sub_cmd = SubtractCommand()
    result = sub_cmd.execute(10, 5)
    assert result == 5

def test_multiply_command():
    mult_cmd = MultiplyCommand()
    result = mult_cmd.execute(6, 7)
    assert result == 42

def test_divide_command():
    div_cmd = DivideCommand()
    result = div_cmd.execute(10, 2)
    assert result == 5

def test_divide_by_zero():
    div_cmd = DivideCommand()
    with pytest.raises(ZeroDivisionError):
        div_cmd.execute(10, 0)
