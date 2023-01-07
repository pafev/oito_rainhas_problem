valid = 1
rainhas_coordenadas = []
count = 0

def checaAtaqueHorizontal(rainhas_coordenadas):
    posicoes_linha = []
    for par in rainhas_coordenadas:
        if par[0] not in posicoes_linha:
            posicoes_linha.append(par[0])
        else:
            return 0
    return 1

def checaAtaqueVertical(rainhas_coordenadas):
    posicoes_coluna = []
    for par in rainhas_coordenadas:
        if par[1] not in posicoes_coluna:
            posicoes_coluna.append(par[1])
        else:
            return 0
    return 1

def checaAtaqueDiagonal(rainhas_coordenadas):
    pass

def checaEntrada(rainhas_coordenadas):
    if len(rainhas_coordenadas) != 8:
        return -1
    for par in rainhas_coordenadas:
        if rainhas_coordenadas.count(par) > 1:
            return -1
    return 1


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