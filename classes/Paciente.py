class Paciente:
    def __init__(self, nome, prioridade, prioritario, sintomas, consultorio):
        self.nome = nome
        self.prioridade = int(prioridade)
        self.prioritario = prioritario
        self.sintomas = sintomas
        self.consultorio = int(consultorio)
    
    def definir_consultorio(self):
        id_consultorio = self.consultorio-1
        return id_consultorio
    
    def tornar_prioritario(self):
        self.prioritario = True