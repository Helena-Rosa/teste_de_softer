import pytest 
from escola import verificador_media

def test_string_como_entrada():
    with pytest .raises(TypeError, match = "Tipo invalido, a entrada deve ser numerica"):
        verificador_media("OITO")


def test_menor_que_dez_como_entrada():
    with pytest .raises(TypeError, match = "O valor é maior que 0 e menor a 10"):
        verificador_media("-5")



def test_maior_que_dez_como_entrada():
    with pytest .raises(TypeError, match = "O valor é maior que 0 e menor a 10"):
        verificador_media("2000")



