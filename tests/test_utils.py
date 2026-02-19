from src.utils import add
from src.validator import validate

def test_add():
    assert add(2, 3) == 5

def test_validate():
    assert validate(5) == True
