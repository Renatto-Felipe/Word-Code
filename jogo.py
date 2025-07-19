
import random 
import time
import os 
from pontos_arquivos import salvar_pontos




with open('banco_de_palavras.txt','r') as arquivo:
    lista_palavras = arquivo.readlines()
    
palavras = [palavra.strip() for palavra in lista_palavras]

def jogo_facil ():
    
    palavra = palavras[random.randint(0,len(palavras)-1)]
    
    numero_de_jogo = random.randint(0,10)
    
    print(f" o numero do jogo  é: {numero_de_jogo} e a palavra é :{palavra}")
    time.sleep(3)
    os.system('cls')
    tentativa = input(f"qual palavra representa o numero {numero_de_jogo}:").lower()
    
    if tentativa == palavra:
        print("acertou  , 20 pontos adicionados")
        salvar_pontos(palavras)
        
    else:
        print("errou")
        time.sleep(3)
    
for x in range (0,3):
    jogo_facil()