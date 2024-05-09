from bhaskara import Bhaskara
from pitagoras import Pitagoras

print("""
Bem-vindo!
        
Escolha qual tipo de Calculadora você gostaria de usar:
-------------------------------------------------------
|   1- Bhaskara                                       |
|   2- Pitágoras                                      |
|   3- ??????                                         |
-------------------------------------------------------
""")


if __name__ == '__main__':

    escolha = int(input("Escolha: "))
    
    if escolha == 1:
        
        print("--------------------------------")
        print("Você escolheu Bhaskara (ax² + bx + c)\n")
        print("--------------------------------\n")
        
        tentativas = 0
        while tentativas < 3:
            try:
                a = int(input("Digite o Valor de A: "))
                if a == 0:
                    print("Caso x² esteja sozinho, ele passa a valer 1")
                    a = 1
                b = int(input("Digite o valor de B: "))
                if b == 0:
                    print("Caso x esteja sozinho, ele passa a valer 1")
                    b = 1
                c = int(input("Digite o valor de C: ")) 
                calc = Bhaskara(a, b, c,)
                calc.results()
                calc.graph(a,b,c)

            except ValueError:
                tentativas += 1
                if tentativas == 3:
                    sair = input("Deseja sair do programa? [s/n] ")
                    if sair.lower() == "s":
                        print("Obrigado por utilizar o programa!")
                        exit()
                    else:
                        tentativas = 0
                print("Por favor, digite um número\nTente Novamente")
                
                
    elif escolha == 2:
        print("\nVocê escolheu Pitágoras (a² + b² = c²)\n")
        
        print("--------------------------------")
        print("Digite 0 para o valor à ser identificado!")
        print("--------------------------------\n")
        tentativas = 0
        while tentativas < 3:
            try:
                c1 = int(input("Digite o valor do Cateto Oposto: "))
                c2 = int(input("Digite o valor do Cateto Adjacente: "))
                h = int(input("Digite o valor da Hipotenusa: "))
                print("--------------------------------")

                pit = Pitagoras(h, c1, c2)
                pit.results()
                exit()
                    
            except ValueError:
                tentativas += 1
                if tentativas == 3:
                    sair = input("Deseja sair do programa? [s/n] ")
                    if sair.lower() == "s":
                        print("Obrigado por utilizar o programa!")
                        exit()
                    else:
                        tentativas = 0
                print("Por favor, digite um número\nTente Novamente")
    
    elif escolha == 3:
        print("Função ainda não desenvolvida")
                    