aluno = []
def menu(aluno):   
    print('\nMENU: \n1- Cadastrar \n2- Editar Aluno \n3- Visualizar lista \n4- Excluir Aluno \n5- Sair \n')
    opcao = int(input('Informe a Opção: '))
    if opcao == 1:
        cadastrar(aluno)
    if opcao == 3:
        listar(aluno)
    if opcao == 2:
        editar(aluno)
    if opcao == 4:
        deletar(aluno)
    if opcao == 5:
        sair(aluno)
    else:
        print('\nOpção inválida!')
        return menu(aluno)


def cadastrar(aluno):
    print('\n Cadastrar Aluno ')
    id = int(input('Id: '))
    cpf = input('Cpf: ')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    turma = input('Turma: ')  
    #id generator
    #while True:
    #cont = 0
    #cont = cont + 1
    #id = cont               
    aluno.append({
        'id': id,
        'cpf': cpf,
        'nome': nome,
        'idade': idade,
        'turma': turma
    })
    print('-----------------------\n' 'Concluído!')
    
    opcao = int(input ('\nDeseja cadastrar um novo aluno? [1-Sim/2-Não]: '))
    if opcao == 1:
        cadastrar(aluno)
    elif opcao == 2:
        menu(aluno)
    else:
        print('\nOpção inválida!')
        menu(aluno)


def listar(aluno):
    print('\nLista')
    for i in aluno:
        print( 'Id: ' + str(i['id']) + '\n' + 'Cpf: ' + i['cpf'] + '\n' + 'Nome: ' + i['nome'] + '\n' + 'Idade: ' + str(i['idade']) + '\n' + 'Turma: ' + i['turma'] + '\n' + '-----------------------' )
    opcao = int(input('\nDeseja atualizar algum aluno? 1-Sim/2-Não: '))
    if opcao == 1:
        print('\n--- Atualizar Aluno ---')
        print('1 - Editar')
        print('2 - Deletar')
        print('3 - Menu')
        print('-----------------------\n')

        opcao = int(input('Informe a Opção: '))
        if opcao == 1:
            editar(aluno)
        if opcao == 2:
            deletar(aluno)
        if opcao == 3:
            menu(aluno)
        else:
            print('\nOpção inválida!')
            return menu(aluno)

    else:
        opcao = int(input('\nDeseja retornar ao menu? [1-Sim/2-Não]: '))
        if opcao == 1:
            menu(aluno)

        else:
            exit()


def editar(aluno):
    print('\n--- Editar Aluno ---')
    codigo = int(input('Informe o código: '))

    for i in aluno:
        if i['id'] == codigo:
                i['cpf'] = input('Cpf: ')
                i['nome'] = input('Nome: ')
                i['idade'] = int(input('Idade: '))
                i['turma'] = input('Turma: ')

                print('--------------------\n')
                print('Dados atualizados!')

    opcao = int(input('\nDeseja retornar ao menu? [1-Sim/2-Não]: '))
    if opcao == 1:
        menu(aluno)

    else:
        exit()


def deletar(aluno):
    id = int(input("\nDigite o código do Aluno: "))
    i = 0

    while i < len(aluno):
        if aluno[i]['id'] == id:
            aluno.pop(i)
            print("Aluno deletado!")
        i += 1

    opcao = int(input('\nDeseja retornar ao menu? [1-Sim/2-Não]: '))
    if opcao == 1:
        menu(aluno)

    else:
        exit()


def sair(lista):
    opcao = int(input('\nTem certeza que quer sair? [1-Sim/2-Não]: '))
    if opcao == 1:
        exit()

    else:
        menu(lista)


if __name__ == '__main__':
    menu(aluno)
    