def menu():
    VoltarMenuPrincipal = 'sim'
    
    while VoltarMenuPrincipal == 'sim':

        opcao = input('''
    =============================================================================

    MENU:
    [1]CADASTRAR CONTATO
    [2]LISTAR CONTATO                  
    [3]BUSCAR CONTATO PELO NOME
    [4]DELETAR CONTATO 
    [5]ATUALIZAR CONTATO                                   
    [6]SAIR
                      
    ==============================================================================
    ESCOLHA UMA OPÇÃO:                   
    ''')

        if opcao == "1":
            CadastrarContato()
        elif opcao == "2":
            ListarContato()
        elif opcao == "3":
            BuscarContatoPeloNome()
        elif opcao == "4":
            DeletarContato()
        elif opcao == "5":
            AtualizarContato()
        else:
            Sair()
            # return opcao
        VoltarMenuPrincipal = input("Deseja retornar ao menu principal? (sim ou nao) \n").lower()


def CadastrarContato():
    nome = input("Digite o nome do seu contato: \n")
    ID = input("Escolha a ID do seu contato: \n")
    telefone = input("Coloque o telefone do contato: \n")
    email = input("Coloque o email do contato: \n")
    try:
        agenda = open("agenda.txt","a")
        dados = f'{nome};{ID};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print("Contato gravado com sucesso !!!!")
    except:
        print("Erro na gravação do contato")
        
        
def ListarContato():
    agenda = open("agenda.txt","r")
    for contato in agenda:
        print(contato)
    agenda.close()


def BuscarContatoPeloNome():
    nome1 = input("Digite o nome a ser procurado: \n").upper()
    encontrado = False  # Flag para indicar se o contato foi encontrado
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if nome1 in contato.split(";")[0].upper():
            print(contato)
            encontrado = True  # Contato encontrado
    agenda.close()
    
    if not encontrado:
        print("ERRO: Contato não encontrado!!!")
        return BuscarContatoPeloNome()


def DeletarContato():
    tentativas = 0
    max_tentativas = 3
    encontrado = False
    
    while tentativas < max_tentativas:
        nomeDeletado = input("Digite o nome do contato a ser deletado: \n").lower()
        
        with open("agenda.txt", "r") as agenda:
            aux = agenda.readlines() #para ler as linhas
        
        aux2 = []
        for i in range(len(aux)):
            if nomeDeletado not in aux[i].lower():
                aux2.append(aux[i])
            else:
                encontrado = True
        
        if encontrado:
            with open("agenda.txt", "w") as agenda:
                for i in aux2:
                    agenda.write(i)
            print("Contato deletado com sucesso!!")
            return
        else:
            print("ERRO: Contato não encontrado!!!")
            tentativas += 1
    
    print("Limite de tentativas excedido. Saindo...")
    

    DeletarContato()


def AtualizarContato():
    nomeDeletado = input("Digite o nome do contato a ser Atualizado: \n").lower()
    encontrado = False
    agenda = open("agenda.txt","r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt","w")
    for i in aux2:
        agenda.write(i)
    nome = input("Digite o nome do seu contato atualizado: \n")
    ID = input("Escolha a ID do seu contato atualizado: \n")
    telefone = input("Coloque o telefone do contato atualizado: \n")
    email = input("Coloque o email do contato atualizado: \n")
    try:
        agenda = open("agenda.txt","a")
        dados = f'{nome};{ID};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print("Contato atualizado com sucesso !!!!")
    except:
        print("Erro na atualização do contato")

def Sair():
    print(f"Ate mais... !!!!!")
    exit()

def main():
    menu()

main()