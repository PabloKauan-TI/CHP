from classes.Consultorio import Consultorio
from classes.Paciente import Paciente

def achar_consultorio(central, id):
    for consultorio in central:
        if consultorio.id == id:
            return central.index(consultorio)

def Main():
    #Inicializando o sistema com no mínimo três consultorios
    central = []
    for i in range(2):
        if len(central) == 0:
            central.append(Consultorio(1))
        central.append(Consultorio(len(central)+1))

    with open("formato.txt", "w") as file:
        file.write("-----------Central Hospitalar Iniciando Atividades-----------\nABRT C 1\nABRT C 2\nABRT C 3\n")

    S = 0
    while S != 7:
        print('\n')
        print("$---------Próximos a serem Chamados---------$")
        for consultorio in central:
            consultorio.imprimir()
        print("\n")
        print("$-------------------CHP---------------------$")
        print("| 1) Cadastrar Paciente                     |")
        print("| 2) Atender Paciente                       |")
        print("| 3) Chamar Paciente de outro Consultorio   |")
        print("| 4) Checar Status dos Consultorios         |")
        print("| 5) Abrir Novo Consultorio                 |")
        print("| 6) Fechar Consultorio                     |")
        print("| 7) Finalizar Sistema                      |")
        print("$-------------------------------------------$")
        print("\nSelecione uma opção:")
        S = int(input())

        match S:
            case 1:
                print("\nInforme as informações do seu paciente:")
                nome = input("Nome: ")
                sintomas = input("Sintomas: ")
                prioridade = int(input("Número do Protocolo: "))
                prioritario = bool(input("Seu paciente é de acesso prioritário: "))
                consultorio_imaginario = int(input("Qual o consultorio do Protocolo: "))

                consultorio_real = achar_consultorio(central, consultorio_imaginario)
                paciente = Paciente(nome, prioridade, prioritario, sintomas, consultorio_imaginario)

                central[consultorio_real].adicionar_paciente(paciente)

                with open("formato.txt", "a") as file:
                    file.write(f"TRD: {paciente.nome}"  + f" C{consultorio_imaginario} {paciente.prioritario}\n")

            case 2:
                consultorio_imaginario = int(input("Qual o consultorio: "))
                consultorio_real = achar_consultorio(central, consultorio_imaginario)
                paciente = central[consultorio_real].atender()

                with open("formato.txt", "a") as file:
                    file.write(f"ATD: C{consultorio_imaginario}" + paciente + "\n")

            case 3:
                atendePaciente_imaginario = int(input("Digite o consultorio que irá atender o paciente: "))
                enviaPaciente_imaginario = int(input("Digite o consultorio que irá enviar o paciente para o atendimento: "))
                enviaPaciente_real = achar_consultorio(central, atendePaciente_imaginario)
                paciente = central[enviaPaciente_real].atender()

                with open("formato.txt", "a") as file:
                    file.write(f"ATD: C{atendePaciente_imaginario}" + paciente  + f" C{enviaPaciente_imaginario}\n")
                
            case 4:
                print("\n")
                for consultorio in central:
                    id = consultorio.id
                    pessoas = consultorio.tamanho()
                    print(f"Consultorio {id} há {pessoas} pacientes a serem atendidos.")

            case 5:
                central.append(Consultorio(len(central)+1))

                with open("formato.txt", "a") as file:
                    file.write(f"ABRT: C{len(central)+1}\n")

            case 6:
                c_menor = None
                tam = 0
                for consultorio in central:
                    if consultorio.tamanho() > tam:
                        tam = consultorio.tamanho()
                        c_menor = consultorio.id
                c_menor = achar_consultorio(central, c_menor)
                
                consultorio_imaginario = int(input("Digite qual consultorio deseja fechar: "))
                consultorio_real = achar_consultorio(central, consultorio_imaginario)

                central[consultorio_real].fechar_consultorio(central[c_menor])

                with open("formato.txt", "a") as file:
                    file.write(f"FCH: C{central[consultorio_real].id}\n")

                central.pop(consultorio_real)

if __name__ == "__main__":
    Main()
