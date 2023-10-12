import sys
sys.path.append(r"C:\Users\NAZA\Desktop\CodFacultad\Programacion\Tps")
import pytest
import funcionestp5
#Ejercicio 1
@pytest.mark.parametrize("a, res", [
    ("no", False),
    ("si", True)
])
def test_repeat(a, res):
    assert funcionestp5.repeat(a)==res #Este es el unico test que voy a hacer de este tipo de funcion
    #Mas que nada porque las validaciones de eleccion en mis otras funciones comparten exactamente el mismo codigo que esta, solo que tienen otro nombre
    #Si ya se, estoy obviando el motivo principal y mas importante por el cual se usan funciones: para ahorrarse lineas de codigo, solo que al momento me olvide tenerlo en cuenta
@pytest.mark.parametrize("a, res", [
    (46328818, True),
    (3324387426, False)
])
def test_booldni(a, res):
    assert funcionestp5.booldni(a)==res
#Ejercicio 2
@pytest.mark.parametrize("a, res", [
    ("hola", 4),
    ("usando pytest", 6)
])
def test_longstring(a, res):
    assert funcionestp5.longstring(a)==res
#Ejercicio 3
@pytest.mark.parametrize("n, nro, res", [
    ("Nazareno Fioretti", 46328818, "Nazareno8463"),
    ("Felipe Suarez", 45328818, "Felipe6453")
])
def test_idenmember(n, nro, res):
    assert funcionestp5.idenmember(n, nro)==res

@pytest.mark.parametrize("con, res", [
    (1, 2), 
    (4, 5)
])
def test_addingcounter(con, res):
    assert funcionestp5.addingcounter(con)==res

@pytest.mark.parametrize("dni, res", [
    (46328818, True),
    (3288189, True),
    (191219021, False)
])
def test_dniok(dni, res):
    assert funcionestp5.dniok(dni)==res

@pytest.mark.parametrize("name, res", [
    ("Nazareno Fioretti", True),
    ("Nazareno Yoel Fioretti", True),
    ("Nazareno Yoel Fioretti Galarce", False)
])
def test_nameok(name, res):
    assert funcionestp5.nameok(name)==res
#Ejercicio 5
@pytest.mark.parametrize("min, max, res", [
    (10, 25, 17.5),
    (4, 20, 12)
])

def test_avrtemp(min, max, res):
    assert funcionestp5.avrtemp(min, max)==res
#Ejercicio 6

@pytest.mark.parametrize("str, res", [
    ("hola", "h o l a "),
    ("hola como estas?", "h o l a   c o m o   e s t a s ? ")
])

def test_stringspacey(str, res):
    assert funcionestp5.stringspacey(str)==res

#Ejercicio 7

@pytest.mark.parametrize("numli, res", [
    ([1, 4, 8], 8), 
    ([4, 9, -1], 9)
])

def test_greatest(numli, res):
    assert funcionestp5.greatest(numli)==res

@pytest.mark.parametrize("lea, grea, numli, res", [
    (4, 8, [6, 4, 2, 8], 2), 
    (-1, 10, [4, 7, 8, 3, -2], -2)
])

def test_leatest(lea, grea, numli, res):
    assert funcionestp5.leatest(lea, grea, numli)==res
#Ejercicio 8
@pytest.mark.parametrize("rad, res, restwo", [
    (3, 28.274333882308138, 18.84955592153876),
    (2, 12.566370614359172, 12.566370614359172)
])
#El pytest no es congruente con los casos y el assert en este ejercicio solo por los decimales
def test_areaandperimeter(rad, res, restwo):
    assert funcionestp5.areaandperimeter(rad)==res, restwo
#Ejercicio 10
@pytest.mark.parametrize("prod, res",[
    (["1000", "1000"], 1800.0),
    (["2000", "2000"], 3600.0)
])

def test_discount(prod, res):
    assert funcionestp5.discount(prod)==res
#Ejercicio 11
@pytest.mark.parametrize("genlist, res", [
    ([], ["Hola0", "Hola1", "Hola2", "Hola3", "Hola4"]),
    (["Naza"], ["Naza", "Hola0", "Hola1", "Hola2", "Hola3", "Hola4"])
])

def test_metafunction(genlist, res):
    assert funcionestp5.metafunction(genlist)==res
#Ejercicio 12
@pytest.mark.parametrize("ph, res", [
    ("hola como estas?", {"hola":4, "como":4, "estas?":6}),
    ("hola", {"hola":4})
])
def test_converdic(ph, res):
    assert funcionestp5.converdic(ph)==res
#Ejercicio 13
@pytest.mark.parametrize("compone, comptwo, compthree, res", [
    (3, 5, 7, 9.110433579),
    (4, 9, 8, 12.68857754)
])
def test_vectmodul(compone, comptwo, compthree, res):
    assert funcionestp5.calcvectormodul(compone, comptwo, compthree)==res
#De nuevo, el pytest falla por los decimales
#Ejercicio 14
@pytest.mark.parametrize("prim, res", [
    (101, False),
    (203, True)
])

def test_primenumber(prim, res):
    assert funcionestp5.primenumberlocal(prim)==res
#Ejercicio 15
@pytest.mark.parametrize("nro, res", [
    (4, 5),
    (2, 3)
])

def test_numbercounter(nro, res):
    assert funcionestp5.numbercounter(nro)==res

@pytest.mark.parametrize("nro, res", [
    (5, 120),
    (6, 720)
])

def test_factorial(nro, res):
    assert funcionestp5.factorial(nro)==res