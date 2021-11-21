class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
        self.materias = []

    def addAluno(self, aluno):
        self.alunos.append(aluno)  # adiciona o aluno à turma

    def removeAluno(self, aluno):
        self.alunos.remove(aluno)  # retira o aluno da turma

    def addMateria(self, materia):
        self.materias.append(materia)

    def removeMateria(self, materia):
        materia.setTurma(None)
        materia.professor.removeMateria(materia)
        materia.professor = None
        self.materias.remove(materia)
