"""
Módulo principal com funções utilitárias para o portfólio DevOps/SRE.

Este módulo contém funções de propósito geral com type hints,
incluindo operações matemáticas, validações e utilitários de strings.
"""

from typing import List, Optional, Union


def somar(a: float, b: float) -> float:
    return a + b


def subtrair(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(numerador: float, denominador: float) -> float:
    if denominador == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida")
    return numerador / denominador


def media(numeros: List[float]) -> float:
    if not numeros:
        raise ValueError("A lista de números não pode estar vazia")
    return sum(numeros) / len(numeros)


def eh_par(numero: int) -> bool:
    return numero % 2 == 0


def eh_primo(numero: int) -> bool:
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True


def reverter_string(texto: str) -> str:
    return texto[::-1]


def contar_vogais(texto: str) -> int:
    vogais = "aeiouAEIOU"
    return sum(1 for char in texto if char in vogais)


def validar_email(email: str) -> bool:
    if not isinstance(email, str) or "@" not in email:
        return False
    partes = email.split("@")
    if len(partes) != 2:
        return False
    usuario, dominio = partes
    if not usuario or not dominio:
        return False
    if "." not in dominio:
        return False
    return True


def fatorial(n: int) -> int:
    if n < 0:
        raise ValueError("Fatorial não está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def fibonacci(n: int) -> List[int]:
    if n <= 0:
        raise ValueError("n deve ser maior que zero")
    if n == 1:
        return [0]
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


def buscar_valor(lista: List[Union[int, str]], valor: Union[int, str]) -> Optional[int]:
    for indice, item in enumerate(lista):
        if item == valor:
            return indice
    return None


if __name__ == "__main__":
    print("Portfólio DevOps/SRE - Módulo Principal")
    print(f"2 + 3 = {somar(2, 3)}")
    print(f"10 - 4 = {subtrair(10, 4)}")
    print(f"5 * 6 = {multiplicar(5, 6)}")
    print(f"20 / 4 = {dividir(20, 4)}")
    print(f"Média de [1,2,3,4,5] = {media([1, 2, 3, 4, 5])}")
    print(f"4 é par? {eh_par(4)}")
    print(f"17 é primo? {eh_primo(17)}")
    print(f"'DevOps' invertido = '{reverter_string('DevOps')}'")
    print(f"Vogais em 'Hello World' = {contar_vogais('Hello World')}")
    print(f"'teste@exemplo.com' é válido? {validar_email('teste@exemplo.com')}")
    print(f"Fatorial de 5 = {fatorial(5)}")
    print(f"Fibonacci(10) = {fibonacci(10)}")
    print(f"Índice de 'DevOps' em ['CI', 'CD', 'DevOps'] = {buscar_valor(['CI', 'CD', 'DevOps'], 'DevOps')}")
