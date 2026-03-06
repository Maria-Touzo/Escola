import pytest
from escola import verificador_media

# Teste parametrizado
# Com uma unica função testo vários valores
@pytest.mark.parametrize(
                            ("media","resultado_esperado"),
                            [
                                (7,"Aprovado"),
                                (5,"Recuperação"),
                                (5.5,"Recuperação"),
                                (0,"Reprovado"),
                                (10,"Aprovado")
                            ]
                        )
def test_testando_bordas(media, resultado_esperado):
    assert verificador_media(media) == resultado_esperado