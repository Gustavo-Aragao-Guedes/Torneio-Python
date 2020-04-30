import sys
print("Bem-vindo ao Torneio Python!")
print()
print("HISTÓRIA:")
print("Você é uma pessoa cuja família está passando por sérios problemas financeiros. Para tentar conseguir algum dinheiro de forma rápida, você decide entrar em um torneio de perguntas e resposta que está sendo realizado em sua cidade. O objetivo do torneio é testar o conhecimento dos participantes com perguntas sobre a linguagem de programação Python durante um duelo entre os participantes. A cada pergunta respondida corretamente, o participante ganha uma pequena quantidade de dinheiro e um bônus cada vez que ele subir no ranking. Com uma parte do pouco dinheiro que você e sua família tinham e com seu breve conhecimento que você possui sobre a linguagem, você paga a taxa de inscrição (R$20), e entra na competição da liga 'Conhecimentos Básicos', na esperança de conseguir sair dali com mais dinheiro de que quando entrou.") 
print()
print("INSTRUÇÕES:")
print("Responda corretamente as perguntas para causar 1 dano no seu oponente. Cause 2 danos para derrota-lo! A cada resposta incorreta você receberá 1 dano! Receba 2 danos (em um único duelo) e você será derrotado, retornando para casa com o dinheiro que você conseguiu.")
print("Responda digitando, EM MAIÚSCULO, a letra da alternativa que você acha ser a correta. Digitar outro caractere considerará a resposta como errada e infligirá 1 de dano á você.")
print()
print("VALORES:")
print("Acerto de cada questão: + R$30")
print("Derrotar cada oponente: + R$100")
print("Derrotar o campeão: + R$500")
print()
print("CLASSIFICAÇÕES:")
print("Ruim...: Dinheiro < R$100")
print("Decente: R$100 < Dinheiro < R$200")
print("Boa!: R$200 < Dinheiro < R$350")
print("EXCELENTE!: Dinheiro > R$500")
print()
contDin = 0
contAtq = 0
contDano = 0
contDue = 1
Nome = input("Digite seu nome: ")
print("Primeiro duelo! TEMA: Variáveis e Entra/Saída!")
print("PERGUNTA 1: Qual variável é válida?")
print("A) 'Cao_Azul'  B) Cao Azul  C) Cao_Azul  D) Cão_Azul")
respost1 = input("Resposta: ")
if respost1 != "C":
    print("Resposta errada! Você recebeu 1 de dano!")
    contDano = contDano + 1
elif respost1 == "C":
    print("Resposta certa! Você causou 1 de dano!")
    contAtq = contAtq + 1
    contDin = contDin + 30
print("PERGUNTA 2: Qual dessas palavras NÃO está reservada no Python?")
print("A) not  B) of  C) in  D) or")
respost2 = input("Resposta: ")
if respost2 != "B":
    print("Resposta errada! Você recebeu 1 de dano!")
    contDano = contDano + 1
elif respost2 == "B":
    print("Resposta certa! Você causou 1 de dano!")
    contAtq = contAtq + 1
    contDin = contDin + 30
if contAtq == 2:
    print("Oponente derrotado! Você avançou para as semifinais e ganhou um bônus de R$100!")
    contDin = contDin + 100
    contDue = contDue + 1
elif contDano == 2:
    print("Você foi derrotado/a! Dinheiro recebido: R$ 0")
    print(Nome,"e sua família morreram de fome!")
    print("CLASSIFICAÇÃO: Ruim...")
    print("FIM DE JOGO")
    sys.exit()
elif contAtq < 2:
    print("PERGUNTA 3: Qual o tipo de dado que representa uma sequência de letras, dígitos ou símbolos especiais?")
    print("A) int  B) float  C) str")
    respost3 = input("Resposta: ")
    if respost3 != "C":
        print("Resposta errada! Você recebeu 1 de dano!")
        print("Você foi derrotado/a! Dinheiro recebido: R$ 30")
        print(Nome,"e sua família morreram de fome!")
        print("CLASSIFICAÇÃO: Ruim...")
        print("FIM DE JOGO")
        sys.exit()
    elif respost3 == "C":
        print("Resposta certa! Você causou 1 de dano!")
        print("Oponente derrotado! Você avançou para as semifinais e ganhou um bônus de R$100!")
        contDin = contDin + 100
        contDue = contDue + 1
if contDue == 2:
    print()
    print("Dinheiro acumulado: R$", contDin)
    print()
    print("Duelo das semifinais! TEMA: Estrutura Condicional!")
    contDano = 0
    contAtq = 0
    contDin = 160
    print("PERGUNTA 1: Qual operador relacional indica 'diferente'?")
    print("A) ==  B) >=  C) ?=  D) !=")
    respost11 = input("Resposta: ")
    if respost11 != "D":
        print("Resposta errada! Você recebeu 1 de dano!")
        contDano = contDano + 1
    elif respost11 == "D":
        print("Resposta certa! Você causou 1 de dano!")
        contDin = contDin + 30
        contAtq = contAtq + 1
    print("PERGUNTA 2: Qual operador lógico é inválido na Estrutura Condicional?")
    print("A) in  B) and  C) or  D) not")
    respost22 = input("Resposta: ")
    if respost22 != "A":
        print("Resposta errada! Você recebeu 1 de dano!")
        contDano = contDano + 1
    elif respost22 == "A":
        print("Resposta certa! Você causou 1 de dano!")
        contAtq = contAtq + 1
        contDin = contDin + 30
    if contAtq == 2:
        print("Oponente derrotado! Você avançou para as finais e ganhou um bônus de R$100")
        contDin = contDin + 100
        contDue = contDue + 1
    elif contDano == 2:
        print("Você foi derrotado/a! Dinheiro recebido: R$ 160")
        print(Nome,"salvou a sua família de morrer de fome! Mas apenas por um curto tempo...")
        print("CLASSIFICAÇÃO: Decente")
        print("FIM DE JOGO")
        sys.exit()
    elif contAtq < 2:
        print("PERGUNTA 3: Qual tecla faz o espaçamento correto para a indentação das instruções? ?")
        print("A) ESPAÇO   B) SHIFT  C) TAB  D) CAPS LOCK")
        respost33 = input("Resposta: ")
        if respost33 != "C":
            print("Resposta errada! Você recebeu 1 de dano!")
            print("Você foi derrotado/a! Dinheiro recebido: R$ 190")
            print(Nome,"salvou a sua família de morrer de fome! Mas apenas por um curto tempo...")
            print("CLASSIFICAÇÃO: Decente")
            print("FIM DE JOGO")
            sys.exit()
        elif respost33 == "C":
            print("Resposta certa! Você causou 1 de dano!")
            print("Oponente derrotado! Você avançou para as finais e ganhou um bônus de R$100!")
            contDin = contDin + 100
            contDue = contDue + 1
else:
    sys.exit()
if contDue == 3:
    print()
    print("Dinheiro acumulado: R$", contDin)
    print()
    contDano = 0
    contAtq = 0
    contDin = 320
    print("Senhoras e senhores! Chegou a hora das finais!")
    print("*insira música de combate final aqui*")
    print("Neste último duelo teremos", Nome,"versus o campeão: Pythángoras!")
    print("Pythángoras: HA! HA! HA! Boa sorte",Nome,",diferente daqueles oponentes genéricos que você derrotou antes,eu me formei em filosofia nesta linguagem!")
    print("TEMA: Estruturas de repetição(While e for)!")
    print("PERGUNTA 1: Qual é o nome da variável utilizada para controlar a contagem do número de execuções do bloco de instruções?")
    print("A) Acumulador  B) Contador  C) Condicional  D) Somador")
    respost111 = input("Resposta: ")
    if respost111 != "B":
        print("Resposta errada! Você recebeu 1 de dano!")
        print("Pythángoras: Errou! HA! Erre mais uma e você já era,",Nome,"!")
        contDano = contDano + 1
    elif respost111 == "B":
        print("Resposta certa! Você causou 1 de dano!")
        print("Pythángoras: DROGA! Como você se lembrou disso?!")
        print("Pythángoras: ESTE AINDA NÃO É MEU FIM!!!")
        contAtq = contAtq + 1
        contDin = contDin + 30
    print("PERGUNTA 2: Para mostrar todos os pares em: for x in range(1,25,x), qual deve ser o valor de x?")
    print("A) 0  B) 1  C) 2  D) 3")
    respost333 = input("Resposta: ")
    if respost333 != "C":
        print("Resposta errada! Você recebeu 1 de dano!")
        print("Pythángoras: E-R-R-O-U! HAHAHAHA! Guido van Rossum estaria desapontado com você!")
        contDano = contDano + 1
    elif respost333 == "C":
        print("Resposta certa! Você causou 1 de dano!")
        contAtq = contAtq + 1
        contDin = contDin + 30
    if contAtq == 2:
        print("Você derrotou o campeão Pythángoras!")
        print("Pythángoras: NÃOOOOOOOOOOOO!!! COMO PUDE SER DERROTADO?! GUIDO VAN ROSSUM, ME PERDOE...!")
        contDin = contDin + 500
        print("Parabéns você venceu a liga 'Conhecimentos Básicos' e recebeu um total de: R$", contDin)
        print("Com a boa quantidade de dinheiro que",Nome,"recebeu, sua família não morreu de fome e ela conseguiu estabilizar os problemas financeiros que estavam tendo!")
        print("CLASSIFICAÇÃO: EXCELENTE!")
        print("FIM DE JOGO")
        sys.exit()
    elif contDano == 2:
        print("Você foi derrotado pelo campeão Pythángoras!")
        print("Pythángoras: Nadou um oceano inteiro para morrer na praia... Que vergonha!")
        print("Dinheiro recebido: R$ 320")
        print("Apesar da derrota,",Nome,"acumulou dinheiro suficiente para salvar a sua família de morrer de fome!")
        print("CLASSIFICAÇÃO: Boa")
        print("FIM DE JOGO")
        sys.exit()
    elif contAtq < 2:
        print("Pythángoras: Última chance,",Nome,"...")
        print("PERGUNTA SURPRESA!")
        print("Qual o primeiro nome do grupo humorístico que originou o nome da linguagem Python?")
        print("A) Monty  B) Trevor  C) Scott  D) Billy")
        respost333 = input("Resposta: ")
        if respost333 != "A":
            print("Resposta errada! Você recebeu 1 de dano!")
            print("Você foi derrotado pelo campeão Pythángoras!")
            print("Pythángoras: Nadou um oceano inteiro para morrer na praia... Que vergonha!")
            print("Dinheiro recebido: R$ 350")
            print("Apesar da derrota,",Nome,"acumulou dinheiro suficiente para salvar a sua família de morrer de fome!")
            print("CLASSIFICAÇÃO: Boa!")
            print("FIM DE JOGO")
            sys.exit()
        elif respost333 == "A":
            print("Resposta certa! Você causou 1 de dano!")
            contDin = contDin + 30
            print("Você derrotou o campeão Pythángoras e ganhou o prêmio final de R$500!")
            contDin = contDin + 500
            print("Pythángoras: NÃOOOOOOOOOOOO!!! COMO PUDE SER DERROTADO?! GUIDO VAN ROSSUM, ME PERDOE...!")
            print("Parabéns você venceu a liga 'Conhecimentos Básicos' e recebeu um total de: R$", contDin)
            print("Com a boa quantidade de dinheiro que",Nome,"recebeu, sua família não morreu de fome e ela conseguiu estabilizar os problemas financeiros que estavam tendo!")
            print("CLASSIFICAÇÃO: EXCELENTE!")
            print("FIM DE JOGO")
            sys.exit()
else:
    sys.exit()

            
        
        
        
        
    
        
        
          
          
          

          
          
        
        
    
