while (True):
    print("\n\n-----------Bem vindo------------\n\n")
    print("\tFunções disponíveis:  \n\t")
    print("1 - Probabilidade Binomial Individual (P = x)")
    print("2 - Probabilidade Binomial Acumulada (P <= x)")
    print("3 - Probabilidade Binomial Acumulada (P >= x)\n")
    print("\n-------------------------------\n")
    escolha = int(input("Digite o número da função a ser utilizada (ou 0 para terminar):  \n\n"))

    i = 1
    
    
    if escolha == 1:

        n = float(input("\nDigite o número de observações (n):  \n"))
        p = float(input("Digite a probabilidade de sucesso em cada observação (em porcentagem)(p):  %\n")) # ele que vai fazer p e q
        x = float(input("Digite o número de sucessos (x):  \n\n"))

        proba = p / 100
        diff_homiiebart = n - x
        def fatoiral(n,x):
            i = 1
            j= 1
            y = 1
            homer_simpson = 1
            dostoievski =1
            bart_simpson = 1
            while (i <= n):

                homer_simpson *= i
                i += 1
                if i > n:

                    break

            while (j <= x):

                bart_simpson *= j
                j += 1
                if j > x:
                    break

            while (y <= diff_homiiebart):

                dostoievski *= y
                y += 1
                if y > diff_homiiebart:
                    break
            c = homer_simpson / (bart_simpson * dostoievski)
            return homer_simpson / (bart_simpson * dostoievski)

        caso1 = proba ** x
        caso2 = (1 - proba) ** diff_homiiebart
        print(f"Probabilidade do caso acontecer exatamente {n} vezes: {(fatoiral(n,x) * caso1 * caso2) * 100:.2f} %")

    elif escolha == 2:
        
        resultado = 0
        n = float(input("\nDigite o número de observações (n):  "))
        p = float(input("\nDigite a probabilidade de sucesso em cada observação (em porcentagem)(p): ")) # ele que vai fazer p e q
        x = float(input("\nDigite o número de sucessos (x):  \n\n"))

        while (True):

            i = 1



            if x < 0:
              print(f"Probabilidade do caso acontecer no máximo {x} vezes: {resultado * 100:.2f} %\n\n")
              break


            proba = p / 100
            diff_homiiebart = n - x


            def fatoiral(n,x):
                i = 1
                j= 1
                y = 1
                homer_simpson = 1
                dostoievski =1
                bart_simpson = 1
                while (i <= n): #SEMPRE O FATORIAL DE N

                    homer_simpson *= i
                    i += 1
                    if i > n:

                        break

                while (j <= x): #SEMPRE O FATORIAL DE X

                    bart_simpson *= j
                    j += 1
                    if j > x:
                        break

                while (y <= diff_homiiebart): #SEMPRE O FATORIAL DA DIFERENÇA ENTRE N & X

                    dostoievski *= y
                    y += 1
                    if y > diff_homiiebart:
                        break
                return homer_simpson / (bart_simpson * dostoievski)



            c = fatoiral(n,x)
            caso1 = proba ** x
            caso2 = (1 - proba) ** diff_homiiebart

            resultado = c * caso1 * caso2 + resultado
            x -= i
    
    elif escolha == 3:

        resultado = 0
        n = float(input("\nDigite o número de observações (n):  "))
        p = float(input("\nDigite a probabilidade de sucesso em cada observação (em porcentagem)(p): ")) # ele que vai fazer p e q
        x = float(input("\nDigite o número de sucessos (x):  \n\n"))

        while (True):

            i = 1

            if x == n:
              print(f"Probabilidade do caso acontecer no mínimo {x} vezes: {resultado * 100:.2f} %\n\n")
              break


            proba = p / 100
            diff_homiiebart = n - x


            def fatoiral(n,x):
                i = 1
                j= 1
                y = 1
                homer_simpson = 1
                dostoievski =1
                bart_simpson = 1
                while (i <= n): #SEMPRE O FATORIAL DE N

                    homer_simpson *= i
                    i += 1
                    if i > n:

                        break

                while (j <= x): #SEMPRE O FATORIAL DE X

                    bart_simpson *= j
                    j += 1
                    if j > x:
                        break

                while (y <= diff_homiiebart): #SEMPRE O FATORIAL DA DIFERENÇA ENTRE N & X

                    dostoievski *= y
                    y += 1
                    if y > diff_homiiebart:
                        break
                return homer_simpson / (bart_simpson * dostoievski)



            c = fatoiral(n,x)
            caso1 = proba ** x
            caso2 = (1 - proba) ** diff_homiiebart

            resultado = c * caso1 * caso2 + resultado
            x += i


    else:
        break



     ##c = homer_simpson / (bart_simpson * dostoievski)
               ## print
               ## caso1 = proba ** x
                ###print(f"proba1 {caso1}")
               ######resultado = c * caso1 * caso2 + resultado
               ## print(f"resultado final do loop: {resultado}")