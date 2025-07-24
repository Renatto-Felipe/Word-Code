import jogo
from arquivos import*

palavras = banco_palavras()

def menu ():
    print("bem vindo ao word code ! ")
    print(" memorize em segundos uma associação entre palavras e numeros")
   
    print("1 para modo facil: com apenas 3 palavras e 6 rodadas ")
    print("2 para modo médio: com 6 palavras")
    print("3 para modo dificil com 3 palavras mas cada codigo é uma letra da palavra")
    print("4 para adicionar palavras ao banco de palavras do jogo")
   
    opcao = int(input("sua opção: "))
   
    match opcao:
        case 1:
            for x in range (0,3):
               jogo.jogo_facil()
               
            menu()
        case 2:
            print("ainda nao disponivel")
        case 3:
            print("ainda nao disponivel")
        case 4:
            salvar_palavra(palavras)
 
menu()