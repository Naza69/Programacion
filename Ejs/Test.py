import pytest
from FuncionesTests import *
@pytest.mark.parametrize("a, b, resp",[
    (2, 4, 6),
    (6, 5, 10),
    (10, 8, 18),
])
def test_sumar(a, b, resp):
    assert sumar(a, b) == resp
