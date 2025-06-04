import pytest
from primos.primos import filtrar_primos, es_primo

class TestPrimos:
    def test_es_primo(self):
        assert es_primo(2) == True
        assert es_primo(3) == True
        assert es_primo(4) == False
        assert es_primo(17) == True
        assert es_primo(1) == False

    def test_filtrar_primos(self):
        assert filtrar_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7]
        assert filtrar_primos([11, 12, 13, 14, 15]) == [11, 13]
        assert filtrar_primos([]) == []
        
    def test_filtrar_primos_con_no_lista(self):
        with pytest.raises(TypeError):
            filtrar_primos("no es una lista")
            
    def test_filtrar_primos_con_no_enteros(self):
        assert filtrar_primos([2, 3.5, 4, "5", 7]) == [2, 7]