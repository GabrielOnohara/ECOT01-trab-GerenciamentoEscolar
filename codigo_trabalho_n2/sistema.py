class Sistema:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.turmas = []
        self.ultima_matricula_aluno = 0
        self.ultima_matricula_professor = 0

    def addAluno(self, aluno):
        self.ultima_matricula_aluno += 1
        aluno.matricula = self.ultima_matricula_aluno
        self.alunos.append(aluno)

    def addProfessor(self, professor):
        self.ultima_matricula_professor += 1
        professor.matricula = self.ultima_matricula_professor
        self.professores.append(professor)

    def addTurma(self, turma):
        self.turmas.append(turma)

    # Retorna a turma com o dado nome
    def getTurma(self, nome_turma):
        for t in self.turmas:
            if t.nome == nome_turma:
                return t
        return None

    # Retorna o professor com o dado nome
    def getProfessor(self, nome_professor):
        for p in self.professores:
            if p.nome == nome_professor:
                return p
        return None

    def removeAluno(self, aluno):
        aluno.turma.removeAluno(aluno)
        aluno.turma = None
        self.alunos.remove(aluno)

    def removeProfessor(self, professor):
        for materia in professor.materias:
            self.removeMateria(materia)
        self.professores.remove(professor)

    def removeMateria(self, materia):
        materia.professor.removeMateria(materia)
        materia.professor = None
        materia.turma.removeMateria(materia)
        materia.turma = None
        self.materias.remove(materia)

    def removeTurma(self, turma):
        for aluno in turma.alunos:
            self.removeAluno(aluno)
        turma.alunos = None
        self.turmas.remove(turma)
