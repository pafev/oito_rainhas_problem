from oito_rainhas import checaAtaqueHorizontal, checaAtaqueVertical, checaAtaqueDiagonal, checaEntrada

def testa_checaAtaqueHorizontal():
    tabuleiroDados1 = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7)]
    tabuleiroDados2 = [(0,1), (0,5), (1,7), (3,3), (4,0), (5,2), (6,4), (7,6)]
    tabuleiroDados3 = [(0,0), (1,6), (2,3), (3,5), (4,7), (5,1), (6,4), (7,2)]
    
    assert checaAtaqueHorizontal(tabuleiroDados1) == 0
    assert checaAtaqueHorizontal(tabuleiroDados2) == 0
    assert checaAtaqueHorizontal(tabuleiroDados3) == 1

def testa_checaAtaqueVertical():
    pass

def testa_checaAtaqueDiagonal():
    pass

def testa_checaEntrada():
    pass