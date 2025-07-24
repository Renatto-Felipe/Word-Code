import random
import time
import os
from arquivos import*




palavra = banco_palavras()

def jogo_facil ():
   
    ordem = {1:"", 2:"",3:""}
   
    # aqui vamos adicionar um numero a uma chave que será uma palavra aleatoria
    frase_completa = ""
    for x in range (1,4):
       
        ordem[x]= palavras[random.randint(0,len(palavras)-2)]
       
        print(f" numero : {x} ,  palavra: {ordem[x]}")
       
        # aqui adicionamos uma sequencia aleatoria das palavras que serão exibidas
       
    sequencia = random.sample([1,2,3],3)
   
    sequencia_str = ''.join(str(sequencia))
   
    for digitos in sequencia :
        frase_completa+=ordem[int(digitos)]
       
    resposta =frase_completa  
   
    time.sleep(6)
   
    '''os.system('clear')'''
   
    tentativa = input(f"quais palavras representam os numeros {sequencia_str}: ").lower().split()
   
    tentativa_unida = "".join(tentativa)
   
   
    print (resposta)
    print(tentativa_unida)
   
    if tentativa_unida  == resposta :
        print("+20 pontos adicionados")
        salvar_pontos(palavras)
       
    else:
        print("errou")
        time.sleep(3)