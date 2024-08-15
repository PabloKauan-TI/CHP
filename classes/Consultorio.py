from classes.Floresta import Floresta

class Consultorio:
    def __init__(self, id):
        self.id = id
        self.filas = [ None, None]
    
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

    def atender(self):
        if len(self.filas[0].floresta) == None:
            return self.filas[1].atender()
        else:
            return self.filas[0].atender()
    

    def imprimir(self):
            for fila in self.filas:
                if fila is not None:
                    fila.imprimirPacientes(self)
    