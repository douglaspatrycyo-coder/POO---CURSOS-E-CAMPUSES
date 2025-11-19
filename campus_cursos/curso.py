class Curso:
    def __init__(self, nome: str, codigo: str):
        self.nome = nome
        self.codigo = codigo

    def __str__(self):
        return f"Curso(código={self.codigo}, nome={self.nome})"
