from word_code import ramdomize


def teste():
    print("batata")

def menu ():
    print("bem vindo ao word code ! ")
    print(" memorize em 5 segundos uma associação entre palavras e numeros")
    
    print("1 para modo facil: com apenas 3 palavras e 6 rodadas ")
    print("2 para modo médio: com 6 palavras")
    print("3 para modo dificil com 3 palavras mas cada codigo é uma letra da palavra")
    print("4 para adicionar palavras ao banco de palavras do jogo")
    
    opcao = int(input("sua opção: "))
    
    match opcao:
        case 1:
           ramdomize()
        case 2:
            print("abobra")
 
     
    
    
menu()