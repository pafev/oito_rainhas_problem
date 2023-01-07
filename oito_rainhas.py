valid = 1
rainhas_coordenadas = []
count = 0

def checaAtaqueHorizontal():
    pass

def checaAtaqueVertical():
    pass

def checaAtaqueDiagonal():
    pass

def checaEntrada():
    pass

def recebeDados(linha, posicao_linha, rainhas_coordenadas):
    pass


while count < 8 and valid == 1:
    valid = recebeDados(input(), count, rainhas_coordenadas)
    count += 1

if valid == 1:
    valid = checaEntrada(rainhas_coordenadas)
elif valid == 1:
    valid = checaAtaqueHorizontal(rainhas_coordenadas)
elif valid == 1:
    valid = checaAtaqueVertical(rainhas_coordenadas)
elif valid == 1:
    valid = checaAtaqueDiagonal(rainhas_coordenadas)


print(valid)