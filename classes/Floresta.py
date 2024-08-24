from classes.Heap import Heap

class Floresta:
    def __init__(self, paciente):
        self.floresta = []
        self.floresta.append(Heap(paciente))
    
    def unir(self, floresta = None):
        if floresta == None:
            a = 0
            x = 1
            y = 2
            try:
                while y <= len(self.floresta)-1:
                    while self.floresta[a].grau == self.floresta[x].grau and self.floresta[x].grau != self.floresta[y].grau:
                        self.unir_caso(a, x)
                    if self.floresta[x].grau == self.floresta[y].grau or self.floresta[a].grau != self.floresta[x].grau:
                        a+=1
                        x+=1
                        y+=1
                if self.floresta[a].grau == self.floresta[x].grau:
                    self.unir_caso(a, x)
            except IndexError:
                pass
        else:
            for heap in floresta:
                self.floresta.append(heap)
            self.floresta.sort(key= lambda heap : heap.grau)
            self.unir()

    def unir_caso(self, x, y):
        if self.floresta[x].prioridade <= self.floresta[y].prioridade:
            self.floresta[x].filho.append(self.floresta[y])
            self.floresta[x].filho.sort(key= lambda heap : heap.grau)
            self.floresta[x].grau += 1
            self.floresta.pop(y)
        else:
            self.floresta[y].filho.append(self.floresta[x])
            self.floresta[y].filho.sort(key= lambda heap : heap.grau)
            self.floresta[y].grau += 1
            self.floresta.pop(x)
    
    def adicionar(self, paciente):
        self.floresta.append(Heap(paciente))
        self.floresta.sort(key= lambda heap : heap.grau)
        self.unir()

    def procurar(self):
        heap_aux = 0
        for i in range(len(self.floresta)):
            if self.floresta[heap_aux].prioridade > self.floresta[i].prioridade:
                heap_aux = i
        return heap_aux

    def atender(self):
        id = self.procurar()
        paciente = self.floresta[id]
        filhos = self.floresta[id].filho
        self.floresta.pop(id)
        if len(filhos) > 0:
            self.unir(filhos)
        if paciente.prioridade is not True:
            return paciente.paciente.__str__()
        else:
            return paciente.paciente.__str__()
            
    def imprimirPacientes(self, consultorio):
        print(f"Consultorio {consultorio.id}:", end=" ")
        for i in self.floresta:
            print(i.paciente, end=" ")
        print() 
    
    def somatorio(self):
        pessoas = 0
        for heap in self.floresta:
            pessoas += 2**heap.grau
        
        return pessoas