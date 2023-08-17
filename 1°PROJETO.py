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
    [5]SAIR
                                        
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
    nomeDeletado = input("Digite o nome do contato a ser deletado: \n").lower()
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
        encontrado = True
    agenda.close()
    print(f"Contato deletado com sucesso!!")
    

    if not encontrado:
        print("ERRO: Contato não encontrado!!!")
        return DeletarContato()
        

def Sair():
    print(f"Ate mais... !!!!!")
    exit()

def main():
    menu()

main()