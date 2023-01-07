valid = 1
rainhas_coordenadas = []
count = 0

def checaAtaqueHorizontal(rainhas_coordenadas):
    pass

def checaAtaqueVertical(rainhas_coordenadas):
    pass

def checaAtaqueDiagonal(rainhas_coordenadas):
    pass

def checaEntrada(rainhas_coordenadas):
    pass

def recebeDados(linha, posicao_linha, rainhas_coordenadas):
    if len(linha) != 8:
        return -1
    else:
        if '1' in linha:
            for posicao_coluna in range(len(linha)):
                if linha[posicao_coluna] == '1':
                    par_coordenadas = (posicao_linha, posicao_coluna)
                    rainhas_coordenadas.append(par_coordenadas)
        return 1


while count < 8 and valid == 1:
    try:
        valid = recebeDados(input(), count, rainhas_coordenadas)
    except Exception:
        pass
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