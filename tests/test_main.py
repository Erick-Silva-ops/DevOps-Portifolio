import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.main import (
    somar,
    subtrair,
    multiplicar,
    dividir,
    media,
    eh_par,
    eh_primo,
    reverter_string,
    contar_vogais,
    validar_email,
    fatorial,
    fibonacci,
    buscar_valor,
)


class TestOperacoesMatematicas:
    def test_somar_positivos(self):
        assert somar(2, 3) == 5

    def test_somar_negativos(self):
        assert somar(-2, -3) == -5

    def test_somar_misto(self):
        assert somar(-2, 5) == 3

    def test_somar_float(self):
        assert somar(1.5, 2.5) == 4.0

    def test_subtrair(self):
        assert subtrair(10, 4) == 6

    def test_subtrair_negativo(self):
        assert subtrair(5, 10) == -5

    def test_multiplicar_positivos(self):
        assert multiplicar(5, 6) == 30

    def test_multiplicar_por_zero(self):
        assert multiplicar(5, 0) == 0

    def test_multiplicar_negativo(self):
        assert multiplicar(-3, 4) == -12

    def test_dividir(self):
        assert dividir(20, 4) == 5

    def test_dividir_float(self):
        assert dividir(7, 2) == 3.5

    def test_dividir_por_zero(self):
        import pytest

        with pytest.raises(ZeroDivisionError):
            dividir(10, 0)


class TestEstatistica:
    def test_media_simples(self):
        assert media([1, 2, 3, 4, 5]) == 3

    def test_media_unico_elemento(self):
        assert media([10]) == 10

    def test_media_lista_vazia(self):
        import pytest

        with pytest.raises(ValueError):
            media([])

    def test_media_negativos(self):
        assert media([-1, -2, -3]) == -2


class TestNumeros:
    def test_eh_par_verdadeiro(self):
        assert eh_par(4) is True
        assert eh_par(0) is True
        assert eh_par(-2) is True

    def test_eh_par_falso(self):
        assert eh_par(3) is False
        assert eh_par(-5) is False

    def test_eh_primo_verdadeiro(self):
        assert eh_primo(2) is True
        assert eh_primo(3) is True
        assert eh_primo(17) is True
        assert eh_primo(29) is True

    def test_eh_primo_falso(self):
        assert eh_primo(1) is False
        assert eh_primo(4) is False
        assert eh_primo(15) is False
        assert eh_primo(0) is False
        assert eh_primo(-5) is False

    def test_fatorial_base(self):
        assert fatorial(0) == 1
        assert fatorial(1) == 1

    def test_fatorial_normal(self):
        assert fatorial(5) == 120
        assert fatorial(6) == 720

    def test_fatorial_negativo(self):
        import pytest

        with pytest.raises(ValueError):
            fatorial(-1)

    def test_fibonacci_um_elemento(self):
        assert fibonacci(1) == [0]

    def test_fibonacci_dois_elementos(self):
        assert fibonacci(2) == [0, 1]

    def test_fibonacci_normal(self):
        assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_fibonacci_n_invalido(self):
        import pytest

        with pytest.raises(ValueError):
            fibonacci(0)
        with pytest.raises(ValueError):
            fibonacci(-5)


class TestStrings:
    def test_reverter_string_simples(self):
        assert reverter_string("DevOps") == "spOveD"

    def test_reverter_string_vazia(self):
        assert reverter_string("") == ""

    def test_reverter_palindromo(self):
        assert reverter_string("arara") == "arara"

    def test_contar_vogais(self):
        assert contar_vogais("Hello World") == 3

    def test_contar_vogais_todas(self):
        assert contar_vogais("aeiouAEIOU") == 10

    def test_contar_vogais_sem_vogais(self):
        assert contar_vogais("bcdfg") == 0

    def test_contar_vogais_vazia(self):
        assert contar_vogais("") == 0


class TestValidacoes:
    def test_validar_email_valido(self):
        assert validar_email("teste@exemplo.com") is True
        assert validar_email("user.name@domain.org") is True

    def test_validar_email_invalido_sem_arroba(self):
        assert validar_email("testeexemplo.com") is False

    def test_validar_email_invalido_sem_usuario(self):
        assert validar_email("@exemplo.com") is False

    def test_validar_email_invalido_sem_dominio(self):
        assert validar_email("teste@") is False

    def test_validar_email_invalido_sem_ponto_dominio(self):
        assert validar_email("teste@exemplo") is False

    def test_validar_email_nao_string(self):
        assert validar_email(123) is False


class TestBusca:
    def test_buscar_valor_existente(self):
        assert buscar_valor(["CI", "CD", "DevOps"], "DevOps") == 2
        assert buscar_valor([10, 20, 30], 20) == 1

    def test_buscar_valor_primeiro(self):
        assert buscar_valor(["CI", "CD", "DevOps"], "CI") == 0

    def test_buscar_valor_inexistente(self):
        assert buscar_valor(["CI", "CD", "DevOps"], "SRE") is None

    def test_buscar_lista_vazia(self):
        assert buscar_valor([], "DevOps") is None
