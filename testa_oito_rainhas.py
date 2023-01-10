from oito_rainhas import *

def testa_checaAtaqueHorizontal():
    tabuleiroDados1 = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7)]
    tabuleiroDados2 = [(0,1), (0,5), (1,7), (3,3), (4,0), (5,2), (6,4), (7,6)]
    tabuleiroDados3 = [(0,0), (1,6), (2,3), (3,5), (4,7), (5,1), (6,4), (7,2)]
    
    assert checaAtaqueHorizontal(tabuleiroDados1) == 0
    assert checaAtaqueHorizontal(tabuleiroDados2) == 0
    assert checaAtaqueHorizontal(tabuleiroDados3) == 1

def testa_checaAtaqueVertical():
    tabuleiroDados1 = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0)]
    tabuleiroDados2 = [(1,0), (5,0), (7,1), (3,3), (0,4), (2,5), (4,6), (6,7)]
    tabuleiroDados3 = [(0,0), (6,1), (3,2), (5,3), (7,4), (1,5), (4,6), (2,7)]

    assert checaAtaqueVertical(tabuleiroDados1) == 0
    assert checaAtaqueVertical(tabuleiroDados2) == 0
    assert checaAtaqueVertical(tabuleiroDados3) == 1

def testa_checaAtaqueDiagonal():
    tabuleiroDados1 = [(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7)]
    tabuleiroDados2 = [(0,6), (1,0), (2,2), (3,5), (4,7), (5,1), (6,3), (7,5)]
    tabuleiroDados3 = [(0,4), (1,1), (2,3), (3,6), (4,2), (5,7), (6,5), (7,0)]

    assert checaAtaqueDiagonal(tabuleiroDados1) == 0
    assert checaAtaqueDiagonal(tabuleiroDados2) == 0
    assert checaAtaqueDiagonal(tabuleiroDados3) == 1


def testa_recebeDados():
    valid = None
    rainhas_coordenadas = []
    linha1 = '00000000'
    linha2 = '00100010'
    linha3 = '000011000'
    linha4 = '0000000'

    valid = recebeDados(linha1, 0, rainhas_coordenadas)
    assert valid == 1
    assert rainhas_coordenadas == []

    valid = recebeDados(linha2, 1, rainhas_coordenadas)
    assert valid == 1
    assert (1, 2) in rainhas_coordenadas and (1, 6) in rainhas_coordenadas

    valid = recebeDados(linha3, 2, rainhas_coordenadas)
    assert valid == -1

    valid = recebeDados(linha4, 3, rainhas_coordenadas)
    assert valid == -1
    

def testa_checaEntrada():
    tabuleiroDados1 = []
    tabuleiroDados2 = [(0,0), (1,1), (4,7)]
    tabuleiroDados3 = [(0,0), (6,1), (3,2), (5,3), (7,4), (1,5), (4,6), (2,7), (1,5)]
    tabuleiroDados4 = [(0,4), (1,1), (2,3), (3,6), (4,2), (5,7), (6,5), (7,0)]
    tabuleiroDados5 = [(0,4), (0,4), (2,3), (3,6), (4,2), (5,7), (6,5), (7,0)]

    assert checaEntrada(tabuleiroDados1) == -1
    assert checaEntrada(tabuleiroDados2) == -1
    assert checaEntrada(tabuleiroDados3) == -1
    assert checaEntrada(tabuleiroDados4) == 1
    assert checaEntrada(tabuleiroDados5) == -1

def teste_checaSolucao():
    matrizLinhas1 = ['10000000',
                    '00000100',
                    '00000001',
                    '00100000',
                    '00000010',
                    '00010000',
                    '01000000',
                    '00001000']

    matrizLinhas2 = ['10000000',
                    '00000100',
                    '00000001',
                    '00100000',
                    '00000010',
                    '00010000',
                    '01000000',
                    '00001000',
                    '00000000',
                    '00000000']
    
    matrizLinhas3 = ['10000000',
                    '10000000',
                    '00000001',
                    '00100000',
                    '00000010',
                    '00010000',
                    '01000000',
                    '00001000']

    assert checaSolucao(matrizLinhas1) == 1
    assert checaSolucao(matrizLinhas2) == -1
    assert checaSolucao(matrizLinhas3) == 0