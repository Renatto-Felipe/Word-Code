with open('banco_de_palavras.txt','r') as arquivo:
    lista_palavras = arquivo.readlines()
    
palavras = [palavra.strip() for palavra in lista_palavras]


def salvar_pontos(palavras):
    ''' o ultimo elemento da lista é o numero de pontos do jogador
    então adicionamos 20 pontos em cada rodada '''
    
    pontos  = int(palavras[-1]) + 20
    palavras[-1]= str(pontos)
    
    palavras = "\n".join(palavras)
    
    with open('banco_de_palavras.txt','w') as arquivo:
        arquivo.write(palavras)



def salvar_palavra(palavras):
    nova_palavra = input("digite uma nova palavra: ")
    palavras.insert(0,nova_palavra)
    palavras = "\n".join(palavras)
    
    with open('banco_de_palavras.txt','w') as arquivo:
        arquivo.write(palavras)
      
    with open('banco_de_palavras.txt','r') as arquivo:
        teste = arquivo.readlines() 
        verificador = [palavra.strip() for palavra in teste]
        if nova_palavra in verificador :
            print("palavra salva com sucesso")
    
         
    
        











