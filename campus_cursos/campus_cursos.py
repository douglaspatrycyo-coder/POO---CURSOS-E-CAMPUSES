from .curso import Curso
class Campus:
    def __init__(self, nome: str, sigla: str):
        self.nome = nome
        self.sigla = sigla
        self.cursos = []  # lista de cursos

    def adicionar_curso(self, curso: Curso):
        for c in self.cursos:
            if c.codigo == curso.codigo:
                print(f"Já existe curso com código {curso.codigo} no campus {self.sigla}")
                return False
        self.cursos.append(curso)
        return True

    def listar_cursos(self):
        if not self.cursos:
            print("Nenhum curso cadastrado neste campus.")
        for i, curso in enumerate(self.cursos):
            print(f"{i + 1}. {curso}")

    def buscar_curso_por_codigo(self, codigo: str):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def remover_curso(self, codigo: str):
        curso = self.buscar_curso_por_codigo(codigo)
        if curso:
            self.cursos.remove(curso)
            return True
        return False

    def atualizar_curso(self, codigo: str, novo_nome: str = None, novo_codigo: str = None):
        curso = self.buscar_curso_por_codigo(codigo)
        if not curso:
            return False
        if novo_nome:
            curso.nome = novo_nome
        if novo_codigo:
            # verificar se não existe outro curso com esse novo código
            if any(c.codigo == novo_codigo for c in self.cursos if c is not curso):
                print("Já existe outro curso com esse novo código.")
                return False
            curso.codigo = novo_codigo
        return True

    def __str__(self):
        return f"Campus(sigla={self.sigla}, nome={self.nome}, total de cursos={len(self.cursos)})"
