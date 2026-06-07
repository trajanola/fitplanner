import os
os.system('cls')


def adicionar():    #CREATE
    nome = input("nome do treino: ")
    tipo = input("tipo de treino: ")
    ex = int(input(f"quantas exercicios terá o treino {nome}?: "))

    dados_treino = f"Treino: {nome} | Tipo: {tipo} | Exercícios: "

    for i in range(ex):
        exf = input(f"qual o exercicio {i+1}: ")
        rep = int(input(f"quantas repetições terá o exercicio {i+1}:"))
        dados_treino += f"[{exf}: {rep} rep] "

    with open('treino.txt', 'w') as arquivo:
        arquivo.write(dados_treino + '\n')


def listar():   #READ
    try:
        arquivo = open('treino.txt', 'r')
        treinos = arquivo.readlines()
        arquivo.close()

        if len(treinos) == 0:
            print('Nenhum treino foi cadastrado ainda.')

        else:
            print('Listar treino:')
            for i in range(len(treinos)):
                print(treinos[i].strip())
    except FileNotFoundError:
        print("Nenhum treino encontrado! ")

def atualizar():  # UPDATE
    try:
        treino = input("Digite o nome do treino que deseja atualizar: ")

        arquivo = open('treino.txt', 'r')
        treinos = arquivo.readlines()
        arquivo.close()

        encontrado = False

        for i in range(len(treinos)):

            if treino in treinos[i]:

                print("\nDigite os novos dados do treino:")

                nome = input("Nome do treino: ")
                tipo = input("Tipo de treino: ")
                ex = int(input(f"Quantos exercícios terá o treino {nome}?: "))

                dados_treino = f"Treino: {nome} | Tipo: {tipo} | Exercícios: "

                for j in range(ex):
                    exf = input(f"Qual o exercício {j+1}: ")
                    rep = int(input(f"Quantas repetições terá o exercício {j+1}: "))
                    dados_treino += f"[{exf}: {rep} rep] "

                treinos[i] = dados_treino + "\n"
                encontrado = True
                break

        if encontrado:
            arquivo = open('treino.txt', 'w')

            for treino_atualizado in treinos:
                arquivo.write(treino_atualizado)

            arquivo.close()

            print("Treino atualizado com sucesso!")

        else:
            print("Treino não encontrado.")

    except FileNotFoundError:
        print("Nenhum arquivo encontrado!")

def treino_recomendado():
    print("TIPOS DE TREINO\nSUPERIORES\nINFERIORES")
    tipo = input("tipo de treino: ").upper()
    if tipo == "SUPERIORES":
        superiores = [
            {"exercicio": "Supino Reto","series": 3, "reps":"8-12"},
            {"exercicio": "Supino Inclinado","series": 3, "reps":"8-12"},
            {"exercicio": "Voador","series": 3, "reps":"8-12"},
            {"exercicio": "Triceps Testa","series": 3, "reps":"8-12"},
            {"exercicio": "Triceps Corda","series": 3, "reps":"8-12"},
            {"exercicio": "Triceps Pulley","series": 3, "reps":"8-12"},
            {"exercicio": "Puxada Frontal","series": 3, "reps":"8-12"},
            {"exercicio": "Remada Baixa","series": 3, "reps":"8-12"},
            {"exercicio": "Pulldown(polia)","series": 3, "reps":"8-12"},
            {"exercicio": "Rosca Martelo com Halteres","series": 3, "reps":"8-12"},
            {"exercicio": "Rosca Scott","series": 3, "reps":"8-12"},
            {"exercicio": "Rosca Direta com Barra","series": 3, "reps":"8-12"},
        ]

        nome = "Recomendado do Sistema"
        dados_treino = f"Treino: {nome} | Tipo: {tipo} | Exercícios: "

        for i in superiores:
            dados_treino += f"\n[{i['exercicio']}: {i['series']} x {i['reps']}]"
        with open('treino.txt', 'a') as arquivo:
            arquivo.write(dados_treino + '\n')
    
    elif tipo == "INFERIORES":
        inferiores = [
            {"exercicio": "Agachamento livre","series": 3, "reps":"8-12"},
            {"exercicio": "Leg press","series": 3, "reps":"8-12"},
            {"exercicio": "Agachamento Bulgaro","series": 3, "reps":"8-12"},
            {"exercicio": "Mesa flexora","series": 3, "reps":"8-12"},
            {"exercicio": "Cadeira Abdutora","series": 3, "reps":"8-12"},
            {"exercicio": "Gemeos(pé/sentado)","series": 4, "reps":"12-15"},
        ]

        nome = "Recomendado do Sistema"
        dados_treino = f"Treino: {nome} | Tipo: {tipo} | Exercicios: "

        for i in inferiores:
            dados_treino += f"\n[{i['exercicio']}: {i['series']}x{i['reps']}]"

        with open('treino.txt', 'a') as arquivo:
            arquivo.write(dados_treino + '\n')
    else:
        pass
    
def excluir():       #DELETE

    treino = input("Digite o treino que deseja excluir: ")
    arquivo = open('treino.txt', 'r')
    treinos = arquivo.readlines()
    arquivo.close()
    for i in range(len(treino)):

        if treino in treinos[i].strip():
            treinos.pop(i)
            
            arquivo = open('treino.txt', 'w')
            for j in range(len(treino)):
                arquivo.write("")
            arquivo.close()
            
            print('Treino removido com sucesso!')
        else:
            print('Treino não encontrado.')

while True:
    print('\n1 - Adicionar treino')
    print('2 - Listar treinos')
    print('3 - Atualizar treinos')
    print('4 - Excluir treinos')
    print('5 - Treino recomendado')
    print('6 - Sair')
    
    opcao = int(input('Escolha as opções entre 1-6: '))    

    if opcao == 1:
        adicionar()
    
    elif opcao == 2:
        listar()
    
    elif opcao == 3:
        atualizar()
        
    elif opcao == 4:
        excluir()

    elif opcao == 5:
       treino_recomendado()

    elif opcao == 6:
        break
