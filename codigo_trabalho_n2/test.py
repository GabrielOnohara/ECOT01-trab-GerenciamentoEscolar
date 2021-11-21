import unittest
from aluno import Aluno
from professor import Professor
from nota import Notas
from turma import Turma
from materia import Materia
from sistema import Sistema


class TestSistema(unittest.TestCase):

    def test_add_remove_aluno(self):
        sistema = Sistema()
        turma = Turma("Turma")
        sistema.addTurma(turma)
        aluno = Aluno("Aluno", 2, turma)
        sistema.addAluno(aluno)

        self.assertEqual(aluno.matricula, 1)
        self.assertEqual(len(turma.alunos), 1)
        self.assertEqual(aluno.turma, turma)

        sistema.removeAluno(aluno)

        self.assertEqual(len(turma.alunos), 0)
        self.assertEqual(aluno.turma, None)

    def test_add_remove_materia(self):
        sistema = Sistema()
        turma = Turma("Turma")
        sistema.addTurma(turma)
        professor = Professor("Professor", 33)
        sistema.addProfessor(professor)
        materia = Materia("Materia", professor, turma, Notas(1))

        self.assertEqual(materia.professor.nome, "Professor")
        self.assertEqual(materia.turma.nome, "Turma")


if __name__ == '__main__':
    unittest.main()
