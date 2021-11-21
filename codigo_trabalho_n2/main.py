from aluno import Aluno
from professor import Professor
from nota import Notas
from turma import Turma
from materia import Materia
from sistema import Sistema

sistema = Sistema()


def ler_numero(num_opcoes) -> int:

    while True:
        try:
            n = int(input(" >> "))
            if n >= 1 and n <= num_opcoes:
                return n
        except:
            pass
        print(f"erro: insira um numero de 1 a {num_opcoes}")


def opcoes_de_aluno():
    # https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
    global ultima_matricula_aluno
    global sistema

    while True:

        print("Escolha:")
        print(" 1 - Adicionar Aluno")
        print(" 2 - Remover Aluno")
        print(" 3 - Listar Alunos")
        print(" 4 - Voltar")

        opcao = ler_numero(4)

        if opcao == 1:
            if(len(sistema.turmas) != 0):
                nome = input("Digite o nome: ")
                idade = int(input("Digite a idade: "))

                nome_turma = input("Digite o nome da turma a qual pertence:")
                turma = sistema.getTurma(nome_turma)

                if turma != None:
                    # A matricula do aluno é computada automaticamente pela classe Sistema
                    aluno = Aluno(nome, idade, turma)
                    sistema.addAluno(aluno)
                    print(
                        f"Success: o aluno com o nome \"{nome}\" foi adicionado a turma: \"{nome_turma}\" ")
                else:
                    print(
                        f"Error: a turma com o nome \"{nome_turma}\" não existe")
                    print(
                        f"Error: Aluno não foi adicionado ao sistema")
                    continue
            else:
                print(
                    f"Error:nenhuma turma cadastrada, crie uma turma para depois adicionar um aluno")

        elif opcao == 2:
            matricula = input("Digite o numero de matricula do aluno: ")
            try:
                aluno = encontrar_aluno(int(matricula))
            except:
                aluno = None

            if aluno != None:
                sistema.removeAluno(aluno)
                print(
                    f"Success: o aluno \"{aluno.nome}\" - Matricula: {aluno.matricula} foi removido")
            else:
                print(
                    f"Error: o aluno com a matricula \"{matricula}\" não existe")

        elif opcao == 3:
            print("Lista de Alunos:")
            if(len(sistema.alunos) == 0):
                print("Nao foi encontrado nenhum aluno")
            else:
                for aluno in sistema.alunos:
                    print(
                        f"{aluno.nome}, {aluno.idade} anos - Matricula : {aluno.matricula} - Turma : {aluno.turma.nome}")
        elif opcao == 4:
            return


def encontrar_aluno(matricula):
    global sistema
    for aluno in sistema.alunos:
        if aluno.matricula == matricula:
            return aluno
    return None


def encontrar_professor(matricula):
    global sistema
    for professor in sistema.professores:
        if professor.matricula == matricula:
            return professor
    return None


def opcoes_de_turma():
    global sistema

    while True:

        print("Escolha:")
        print(" 1 - Adicionar Turma")
        print(" 2 - Remover Turma")
        print(" 3 - Listar Turmas")
        print(" 4 - Voltar")

        opcao = ler_numero(4)

        if opcao == 1:
            nome = input("Digite o nome da turma:")
            turma = Turma(nome)
            sistema.addTurma(turma)
        elif opcao == 2:
            nome = input("Digite o nome da turma: ")
            encontrou_turma = False
            for turma in sistema.turmas:
                if turma.nome == nome:
                    encontrou_turma = True
                    if len(turma.alunos) == 0:
                        sistema.removeTurma(turma)
                    else:
                        print("remover todos os alunos da turma?")
                        r = input("sim ou não?")
                        if r == "sim":
                            sistema.removeTurma(turma)
                        else:
                            print("A turma não foi removida")
            if not encontrou_turma:
                print(f"Erro: turma com o nome \"{nome}\" não foi encontrada.")

        elif opcao == 3:
            print("Lista de Turmas:")
            for turma in sistema.turmas:
                print(f"{turma.nome}: {len(turma.alunos)} alunos")
        elif opcao == 4:
            return


def opcoes_de_materia():
    global sistema

    while True:

        print("Escolha:")
        print(" 1 - Adicionar Materia")
        print(" 2 - Remover Materia")
        print(" 3 - Listar Materias")
        print(" 4 - Voltar")

        opcao = ler_numero(4)

        if opcao == 1:
            if(len(sistema.professores) == 0):
                print("A escola não possui nenhum professor ainda")
            elif(len(sistema.turmas) == 0):
                print("A escola não possui nenhuma turma ainda")
            else:
                nome = input("Digite o nome da materia: ")
                nome_professor = input("Digite o nome do professor: ")
                professor = sistema.getProfessor(nome_professor)

                nome_turma = input("Digite o nome da turma a qual pertence: ")
                turma = sistema.getTurma(nome_turma)

                if professor == None:
                    print(
                        f"Error: o professor com o nome \"{nome_professor}\" não existe")
                    continue

                if turma == None:
                    print(
                        f"Error: a turma com o nome \"{nome_turma}\" não existe")
                    continue

                materia = Materia(nome, professor, turma,
                                  Notas(len(turma.alunos)))
                print(
                    f"Success: a materia \"{nome}\" foi adicionada a turma \"{turma.nome}\"")

        elif opcao == 2:
            nome_turma = input("Digite a turma da materia: ")

            nome_materia = input("Digite o nome da materia: ")
            removeu_materia = False
            for turma in sistema.turmas:
                if turma.nome == nome_turma:
                    for materia in turma.materias:
                        if materia.nome == nome_materia:
                            turma.removeMateria(materia)
                            removeu_materia = True
                            break
                    break
                if not removeu_materia:
                    print(
                        f"Error: a turma \"{turma.nome}\" não possui a materia \"{nome}\"")
        elif opcao == 3:
            print("Lista de Materias:")
            for turma in sistema.turmas:
                for materia in turma.materias:
                    print(
                        f"{materia.nome} - Turma : {turma.nome} - Professor : {materia.professor.nome}")
        elif opcao == 4:
            return


def opcoes_de_professor():
    global sistema

    while True:

        print("Escolha:")
        print(" 1 - Adicionar Professor")
        print(" 2 - Remover Professor")
        print(" 3 - Listar Professores")
        print(" 4 - Voltar")

        opcao = ler_numero(4)

        if opcao == 1:
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            # a matricula do professor é computada automaticamente pelo sistema
            professor = Professor(nome, idade)
            sistema.addProfessor(professor)

        elif opcao == 2:
            matricula = input("Digite a matricula: ")
            try:
                professor = encontrar_professor(int(matricula))
            except:
                professor = None

            if professor != None:
                print(
                    f"Success: o professor \"{professor.nome}\" - Matricula: {matricula} foi removido")
                sistema.removeProfessor(professor)
            else:
                print(
                    f"Error: o profesor com a matricula \"{matricula}\" não existe")
        elif opcao == 3:
            print("Lista de Professores:")
            listaMaterias = ""
            for professor in sistema.professores:
                if(len(professor.materias) > 0):
                    for materia in professor.materias:
                        listaMaterias = listaMaterias + " " + materia.nome
                else:
                    listaMaterias = "Nenhuma"
                print(
                    f"{professor.nome}, {professor.idade} anos - Matricula : {professor.matricula} - Materias :{listaMaterias}.")
        elif opcao == 4:
            return


if __name__ == "__main__":

    while True:
        print("Escolha:")
        print(" 1 - Opções de Aluno")
        print(" 2 - Opções de Turma")
        print(" 3 - Opções de Materia")
        print(" 4 - Opçoes de Professor")
        print(" 5 - Sair")

        opcao = ler_numero(5)

        if opcao == 1:
            opcoes_de_aluno()
        elif opcao == 2:
            opcoes_de_turma()
        elif opcao == 3:
            opcoes_de_materia()
        elif opcao == 4:
            opcoes_de_professor()
        elif opcao == 5:
            break
