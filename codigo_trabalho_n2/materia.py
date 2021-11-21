class Materia:
    def __init__(self, nome, professor, turma, notas):
        self.nome = nome
        self.professor = professor
        self.turma = turma
        self.notas = notas

        turma.addMateria(self)
        professor.addMateria(self)

    def setTurma(self, turma):
        self.turma = turma

    def setProfessor(self, professor):
        self.professor = professor
