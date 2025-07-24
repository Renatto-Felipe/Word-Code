

def salvar_pontos(palavras):
    ''' o ultimo elemento da lista é o numero de pontos do jogador
    então adicionamos 20 pontos em cada rodada '''
   
    pontos  = int(palavras[-1]) + 20
    palavras[-1]= str(pontos)
   
    palavras = "\n".join(palavras)
   
    with open('banco_de_palavras.txt','w') as arquivo:
        arquivo.write(palavras)