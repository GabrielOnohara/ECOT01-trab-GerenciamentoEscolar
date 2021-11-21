class Professor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.matricula = 0
        self.materias = []

    def addMateria(self, materia):
        self.materias.append(materia)

    def removeMateria(self, materia):
        self.materias.remove(materia)
