import re

def adicionar_elemento(lista: list, elemento: str) -> bool:
    if re.search(r"[A-Z]", elemento[0]) is not None:
        if re.search(r"(?=.*\\d)(?=.*[-+_!@#$%^&*., ?]).+$") is not None:
            return False
            
        else:
            lista.append(elemento)
            return True
        
    else:
        return False
    '''
    Verifica se o elemento começa com letra maiúscula e possui apenas letras e espaços.
    Se ele passar na verificação, inserir na lista e retornar verdadeiro, caso contrário, retorne falso
    '''


def buscar_elemento(lista: list, elemento: str) -> bool:
    '''
    Verifica se um elemento está contido na lista.
    Se estiver, retorne verdadeiro, caso contrário, retorne falso.
    '''


def remover_elemento(lista: list, elemento: str) -> bool:
    '''
    Verifica se a lista contém um elemento específico.
    Se ele estiver contido na lista, remover o elemento e
    retornar verdadeiro, caso contrário, retornar falso.
    '''


def limpar_lista(lista: list) -> None:
    lista.clear()
    '''
    Remove todos os elementos da lista.
    Função sem retorno.
    '''


def ordenar_lista(lista: list) -> None:
    lista_ordenada = sorted(lista)
    print(lista_ordenada)
    '''
    Ordena todos os elementos da lista por ordem
    alfabética. A função não possui retorno
    '''


def pegar_quantidade(lista: list) -> int:
    '''
    Retorna a quantidade de elementos dentro
    da lista
    '''


def converter_maiusculo(lista: list) -> list:
    conversao = lista.lower()
    print(conversao)
    '''
    Converte todos os elementos da lista para letra
    maiúscula e os retorna em uma nova lista
    '''


def eliminar_repetidos(lista: list) -> list:
    '''
    DESAFIO: 0.5 extra
    Remove todos os elementos repetidos na lista
    e retorna uma lista nova
    (não vale utilizar o set)
    '''
