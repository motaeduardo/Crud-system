import os

Vetor = []  
    
while True:
    os.system('cls')  # Limpa a tela no Windows
    print("========== Menu ===========")
    print("1 - Cadastrar palavra")
    print("2 - Consultar palavras cadastradas")
    print("3 - Editar palavras cadastradas")
    print("4 - Excluir palavras cadastradas")
    print("5 - Sair")
    opcao = int(input("\nEscolha uma opção: "))
    

    if opcao == 1:
        cadastro = input("\nDigite a nova palavra para cadastrar: ")
        Vetor.append(cadastro)  
        print("\nPalavra cadastrada com sucesso!")
        input("\nPressione Enter para continuar...")

    elif opcao == 2:
        if Vetor:
            print("\nPalavras cadastradas:")
            for i in Vetor:
                print(i)
            input("\nPressione Enter para continuar...")  
        else:
            print("\nNenhuma palavra cadastrada!")
            input("\nPressione Enter para continuar...")
                    
    elif opcao == 3:
        editar = input("\nDigite a palavra para Editar: ")
        for i in range(len(Vetor)):
            if editar == Vetor[i]:
                mudar = input("\nDigite a Alteração: ")
                Vetor[i] = mudar
                print("\nPalavra alterada com sucesso!")
                print("\nPalavras cadastradas após a alteração:")
                for palavra in Vetor:
                    print(palavra)
                    input("\nPressione Enter para continuar...")
                break
        else:
            print("\nPalavra não encontrada!")
            input("\nPressione Enter para continuar...")
                
    elif opcao == 4:
        excluir = input("\nDigite a palavra para excluir: ")
        for i in range(len(Vetor)):
            if excluir == Vetor[i]:
                del Vetor[i]
                print("\nPalavra excluída com sucesso!")
                print("\nPalavras cadastradas após a exclusão:")
                for palavra in Vetor:
                    print(palavra)
                    input("\nPressione Enter para continuar...")
                break
        else:
            print("\nPalavra não encontrada!")
            input("\nPressione Enter para continuar...")

    elif opcao == 5:
        print("\nSaindo do programa...")
        input("\nPressione Enter para continuar...")
        break  

    else:
        print("\nOpção inválida! Tente novamente.")
        input("\nPressione Enter para continuar...")


