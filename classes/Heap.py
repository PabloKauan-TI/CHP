class Heap:
    def __init__(self, paciente):
        self.paciente = paciente
        self.pai = None
        self.filho = []
        self.grau = 0
        self.prioridade = paciente.prioridade