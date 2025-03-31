import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print(f" Adicionando ao sys.path: {project_root}")
sys.path.insert(0, project_root)

from calculator import add, substract

def test_add():
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(5, 2) == 3
