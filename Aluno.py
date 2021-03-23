class Aluno:
  def __init__(self, codigo, nome, matricula):
    self.codigo = codigo
    self.nome = nome
    self.matricula = matricula

  def printAluno(self):
    print(self.codigo, self.nome, self.matricula)


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        super().__init__(codigo, nome, matricula)
        self.ano = ano

    def printAlunoEnsinoMedio(self):
        print(self.codigo, self.nome, self.matricula, self.ano)


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre

    def printAlunoGraduacao(self):
        print(self.codigo, self.nome, self.matricula, self.semestre)


x = Aluno("Mike", "Olsen", "01002")
x.printAluno()

y = AlunoEnsinoMedio("Mary", "Alf", "08492", "2002")
y.printAlunoEnsinoMedio()

u = AlunoGraduacao("Jack", "Crook", "04087", "Sexto")
u.printAlunoGraduacao()
