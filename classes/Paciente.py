class Paciente:
    def __init__(self, nome, prioridade, prioritario, sintomas, consultorio):
        self.nome = nome
        self.prioridade = int(prioridade)
        self.prioritario = prioritario
        self.sintomas = sintomas
        self.consultorio = int(consultorio)

        def __str__(self):
            return f"Nome: {self.nome}, Prioridade: {self.prioridade}, Prioritário: {self.prioritario}, Sintomas: {self.sintomas}"
    