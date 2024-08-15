class Paciente:
    def __init__(self, nome, prioridade, prioritario, sintomas, consultorio):
        self.nome = nome
        self.prioridade = int(prioridade)
        self.prioritario = prioritario
        self.sintomas = sintomas
        self.consultorio = int(consultorio)

    def __str__(self):
            if self.prioritario == True:
                return f" {self.nome} P"  
            else:
                return f"{self.nome} NP"
    