rainhas_coordenadas = []

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
    for index_par1 in range(len(rainhas_coordenadas)):
        par1 = rainhas_coordenadas[index_par1]
        for par2 in rainhas_coordenadas[(index_par1 + 1):]:
            if abs(par1[0] - par2[0]) == abs(par1[1] - par2[1]):
                return 0
    return 1


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

def checaSolucao(matriz_linhas):
    global rainhas_coordenadas
    valid = 1
    if len(matriz_linhas) > 8:
        valid = -1
    else:
        count = 0
        while count < 8 and valid == 1:
            valid = recebeDados(matriz_linhas[count], count, rainhas_coordenadas)
            count += 1     
        if valid == 1:
            valid = checaEntrada(rainhas_coordenadas)
        if valid == 1:
            valid = checaAtaqueHorizontal(rainhas_coordenadas)
        if valid == 1:
            valid = checaAtaqueVertical(rainhas_coordenadas)
            print(valid)
        if valid == 1:
            valid = checaAtaqueDiagonal(rainhas_coordenadas)
    rainhas_coordenadas = []
    return valid