class Aluno:
    def __init__(self, nome, idade, turma):
        self.nome = nome
        self.idade = idade
        self.matricula = 0
        self.turma = turma

        turma.addAluno(self)

    def getTurma(self):
        return self.turma

    def setTurma(self, turma):
        self.turma = turma
