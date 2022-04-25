def cadastrarAluno():
    try:
        with open('alunos.txt', 'a+') as file:
            print('\n-----------Cadastro de aluno(a)----------\n')
            nome = input('\nDigite o nome do aluno(a) -> ')
            curso = input('\nDigite o nome do curso -> ')
            nota1 = float(input(f'\nDigite a primeira nota de {nome} -> '))
            nota2 = float(input(f'\nDigite a segunda nota de {nome} -> '))
            nota3 = float(input(f'\nDigite a terceira nota de {nome} -> '))
            faltas = int(input(f'\nDigite o numero de faltas de {nome} -> '))
            media = calcularMedia(nota1, nota2, nota3)
            aprovado = verificarAprovacao(media, faltas)

            file.write('----------------------------------------\n')
            file.write(f'Nome: {nome}')
            file.write(f'\nCurso: {curso}')
            file.write(f'\nNota 1: {nota1}')
            file.write(f'\nNota 2: {nota2}')
            file.write(f'\nNota 3: {nota3}')
            file.write(f'\nFaltas: {faltas}\n')

            print('\nAluno(a) cadastrado(a) com sucesso !\n')

            if aprovado:
                with open('alunosAprovados.txt', 'a+') as fileAprovados:
                    fileAprovados.write(f'{nome}\n')
            else:
                with open('alunosReprovados.txt', 'a+') as fileReprovados:
                    fileReprovados.write(f'{nome}\n')
    except FileNotFoundError:
        print('\n----------Nao existe um arquivo para armazenar os alunos !----------\n')

def excluirAluno():
    file = open("alunos.txt")
    
    print('\n--------------------Excluir Aluno(a)--------------------\n')

    nome = input('\nDigite o nome do aluno que deseja excluir -> ')
    alunoEncontrado = False
    listaAlunos = []
    
    atualizarLista('alunosReprovados', nome)
    atualizarLista('alunosAprovados', nome)

    for line in file.readlines():
        line = line.rstrip('\n')
        if line == f'Nome: {nome}':
            alunoEncontrado = True
        listaAlunos.append(line)

    if len(listaAlunos) < 1:
        print('\n----------Nao existem alunos cadastrados----------\n')
        print('---Por favor, efetue um ou mais cadastros de alunos antes de repetir a operacao !---\n')
        return
    
    with open("alunos.txt", "w") as file1:
        if alunoEncontrado and len(listaAlunos) > 1:
            for line in listaAlunos:
                if line == f'Nome: {nome}':
                    indexLinha = listaAlunos.index(line) - 1
                    for i in range(7):
                        del(listaAlunos[indexLinha])
            file1.write('\n'.join(listaAlunos))
            print('\n----------Aluno(a) excluido(a) com sucesso!----------\n')
        else:
            print('\n----------Aluno(a) nao encontrado(a) !----------\n')
            print('---Por favor, verifique o nome do(a) aluno(a) e repita a operacao !---\n')
            file1.write('\n'.join(listaAlunos))

def listarAlunos():
    print('\n----------Listar Alunos----------\n')
    print('1 - Listar todos os alunos')
    print('\n2 - Listar alunos aprovados')
    print('\n3 - Listar alunos reprovados')
    opcao = int(input('\nSelecione a opcao que deseja -> '))

    if opcao == 1:
        print('\n----------Lista de alunos----------\n')
        with open('alunos.txt') as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    elif opcao == 2:
        print('\n----------Lista de alunos aprovados----------\n')
        with open('alunosAprovados.txt') as fileAprovados:
            for line in fileAprovados.readlines():
                print(line.rstrip('\n'))
    elif opcao == 3:
        print('\n----------Lista de alunos reprovados----------\n')
        with open('alunosReprovados.txt') as fileReprovados:
            for line in fileReprovados.readlines():
                print(line.rstrip('\n'))
        
    else:
        print('\n----------Opcao invalida !----------\n')

def atualizarLista(arquivo, nome):
    file = open(f'{arquivo}.txt')

    alunoEncontrado = False
    listaAlunos = []

    for line in file.readlines():
        line = line.rstrip('\n')
        if line == f'{nome}':
            alunoEncontrado = True
        listaAlunos.append(line)

    with open(f"{arquivo}.txt", "w") as file1:
        if alunoEncontrado:
            for line in listaAlunos:
                if line == f'{nome}':
                    indexLinha = listaAlunos.index(line)
            del(listaAlunos[indexLinha])
            file1.write('\n'.join(listaAlunos))
        else:
            file1.write('\n'.join(listaAlunos))


def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

def verificarAprovacao(media, faltas):
    #Considerando o numero de aulas totais como 15 !

    numeroAulas = 15
    frequencia = (((numeroAulas - faltas) / numeroAulas) * 100)
    
    if int(frequencia) >= 75 and media >= 6.0:
        return True
    else:
        return False

def main():
    while True:
        print('\n--------------------Bem vindo(a) ao sistema academico--------------------\n')
        print('\n1 - Inserir aluno')
        print('\n2 - Excluir aluno')
        print('\n3 - Relatorios')
        print('\n4 - Sair')
        opcao = int(input('\n\nSelecione a opcao que deseja -> '))

        if opcao == 1:
            cadastrarAluno()
        elif opcao == 2:
            excluirAluno()
        elif opcao == 3:
            listarAlunos()
        elif opcao == 4:
            print('\n----------Sistema Encerrado !----------\n')
            break
        else:
            print('\n----------Opcao invalida !----------\n')

main()