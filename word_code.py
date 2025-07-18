import random
import time
import os
 
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


'''aqui ta o problema'''
def salvar_palavra(palavras):
    nova_palavra = input("digite uma nova palavra: ")
    palavras.insert(0,nova_palavra)
    
    with open('banco_de_palavras.txt','w') as arquivo:
        arquivo.write(palavras)
         
    
        
salvar_palavra(palavras)

'''
def ramdomize ():
    palavra = palavras[random.randint(0,len(palavras)-1)]
    
    numero_de_jogo = random.randint(0,10)
    
    print(f" o numero do jogo  é: {numero_de_jogo} e a palavra é :{palavra}")
    time.sleep(3)
    os.system('cls')
    tentativa = input(f"qual palavra representa o numero {numero_de_jogo}:").lower()
    
    if tentativa == palavra:
        print("acertou mizeravi")
        salvar_pontos(palavras)
        
    else:
        return ramdomize()
'''






