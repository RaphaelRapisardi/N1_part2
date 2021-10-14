from abc import abstractproperty
import re

def adicionar_elemento(lista: list, elemento: str) -> bool:
    if re.search(r"[A-Z]", elemento[0]) is not None:
        for x in elemento:
            if re.search(r"[A-Za-z\s]", x) is None:
                return False
        
        lista.append(elemento)
        return True

    else:
        return False    


def buscar_elemento(lista: list, elemento: str) -> bool:
    if(elemento in lista):
        return True
    else:
        return False


def remover_elemento(lista: list, elemento: str) -> bool:
    if(elemento in lista):
        lista.remove(elemento)
        return True
    else:
        return False


def limpar_lista(lista: list) -> None:
    lista.clear()


def ordenar_lista(lista: list) -> None:
    lista.sort()


def pegar_quantidade(lista: list) -> int:
    return len(lista)


def converter_maiusculo(lista: list) -> list:
    Lista2 = []

    for x in lista:
        Lista2.append(x.upper())

    return Lista2


def eliminar_repetidos(lista: list) -> list:
    Lista2 = []
    Acc = None

    for x in lista:
        if (Acc != x):
            Lista2.append(x)

        Acc = x

    return Lista2