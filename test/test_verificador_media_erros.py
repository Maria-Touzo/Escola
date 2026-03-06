import pytest
from escola import verificador_media

def test_string_como_entrada():
    # Captura erros
    with pytest.raises(TypeError, match="Tipo inválido, a entrada deve ser numérica"):
        verificador_media("OITO")

def test_numero_negativo():

    with pytest.raises(ValueError, match="O valor deve ser maior ou igual a 0 e menor ou igual a 10. "):
        verificador_media(-5)

def test_numero_maior():
 
    with pytest.raises(ValueError, match="O valor deve ser maior ou igual a 0 e menor ou igual a 10. "):
        verificador_media(2000)