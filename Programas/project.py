memoria = []

while True:

    comando = input("\n======================\nDigite um comando:\n======================\n1- ABOUT\n2- ADD\n3- LIST\n4- UPDATE\n5- DELETE\n0- QUIT\n======================\n").upper()

    if comando == "ABOUT" or comando == "1":
        print("\nGestor de jogos da Bianca Jacon")

    elif comando == "QUIT" or comando == "0":
        print("\nSaindo do Gestor de jogos, até logo!")
        break

    elif comando == "ADD" or comando == "2":

        while True:
            try:
                quantidade_jogos = int(input("Quantos jogos você deseja adicionar? "))
                if quantidade_jogos <= 0:
                    print("Quantidade inválida, tente novamente!")
                    continue
                break

            except:
                print("Valor inválido, insira um número!")

        for jogo in range(quantidade_jogos):
            print(f"\n Cadastro de jogo {jogo+1}")

            nome = input("Digite o nome do jogo: ")

            jogo = {
                "nome": nome,
                "concluido": False,
                "historico": []
            }

            memoria.append(jogo)
            print(f"Jogo '{nome}' cadastrado!")

    elif comando == "LIST" or comando == "3":

        if len(memoria) == 0:
            print("\nNão há nenhum jogo na lista no momento!")

        else:
            print("\n===== LISTA DE JOGOS =====")
            for i, jogo in enumerate(memoria, start=1):
                status = "Concluído" if jogo["concluido"] else "Pendente"

                print(f"{i} Nome: {jogo['nome']} | Status: {status}")
                print(f"Histórico: {jogo['historico']}")

    elif comando == "UPDATE" or comando == "4":

        nome_jogo_para_modificar = input("Qual jogo você deseja modificar? ")
        jogo_para_modificar = None

        for jogo in memoria:
            if jogo["nome"].lower() == nome_jogo_para_modificar.lower():
                jogo_para_modificar = jogo
                break

        if jogo_para_modificar is not None:
            print(f"\nJogo encontrado: {jogo_para_modificar['nome']}")
            print("======================\n1 - Alterar nome\n2 - Marcar como concluído\n3 - Marcar como pendente\n======================")

            opcao = input("Escolha uma opção: ")

            if opcao == "1" or opcao == "Alterar nome":
                novo_nome = input("Digite o novo nome do jogo: ")
                jogo_para_modificar["historico"].append(f"Nome alterado de {jogo_para_modificar['nome']} para {novo_nome}")
                jogo_para_modificar["nome"] = novo_nome
                print("Nome alterado com sucesso!")

            elif opcao == "2" or opcao == "Marcar como concluido":
                jogo_para_modificar["concluido"] = True
                jogo_para_modificar["historico"].append("Status alterado para concluído")
                print("Jogo marcado como concluído!")

            elif opcao == "3" or opcao == "Marcar como pendente":
                jogo_para_modificar["concluido"] = False
                jogo_para_modificar["historico"].append("Status alterado para pendente")
                print("Jogo marcado como pendente!")

            else:
                print("Opção inválida!")

        else:
            print("Jogo não encontrado!")

    elif comando == "DELETE" or comando == "5":

        nome_jogo_para_remover = input("Qual jogo você deseja remover? ")
        jogo_para_remover = None

        for jogo in memoria:
            if jogo["nome"] == nome_jogo_para_remover:
                jogo_para_remover = jogo
                break

        if jogo_para_remover is not None:
            memoria.remove(jogo_para_remover)
            print(f"Jogo '{nome_jogo_para_remover}' removido com sucesso!")
        else:
            print("Jogo não encontrado!")

    else:
        print("ERRO: Comando não reconhecido")