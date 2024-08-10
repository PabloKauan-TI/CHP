from classes.Floresta import Floresta

class Consultorio:
    def __init__(self, id):
        self.id = id
        self.filas = []
    
    def adicionar_paciente(self, paciente):
        if paciente.prioritario:
            if self.filas[0] == None:
                self.filas[0] = Floresta(paciente)
            else:
                self.filas[0].adicionar(paciente)
        else:
            if self.filas[1] == None:
                self.filas[1] = Floresta(paciente)
            else:
                self.filas[1].adicionar(paciente)

    def fechar_consultorio(self):
        pass

    def atender_outro_consultorio(x):
        pass

    def atender_prioritario(self):
        pass

    def atender(self):
        pass