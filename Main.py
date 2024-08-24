from classes.Consultorio import Consultorio

from classes.Paciente import Paciente


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
                consultorio = int(input("Qual o consultorio do Protocolo: "))

                paciente = Paciente(nome, prioridade, prioritario, sintomas, consultorio)

                central[consultorio-1].adicionar_paciente(paciente)

                with open("formato.txt", "a") as file:
                    file.write(f"TRD: {paciente.nome}"  + f" C{consultorio} {paciente.prioritario}\n")

            case 2:
                consultorio = int(input("Qual o consultorio: "))
                paciente = central[consultorio-1].atender()

                with open("formato.txt", "a") as file:
                    file.write(f"ATD: C{consultorio}" + paciente + "\n")

            case 3:
                atendePaciente = int(input("Digite o consultorio que irá atender o paciente: "))
                enviaPaciente = int(input("Digite o consultorio que irá enviar o paciente para o atendimento: "))
                paciente = central[enviaPaciente-1].atender()

                with open("formato.txt", "a") as file:
                    file.write(f"ATD: C{atendePaciente}" + paciente  + f" C{enviaPaciente}\n")
                
            case 4:
                for consultorio in central:
                    id = consultorio.id
                    pessoas = consultorio.tamanho()
                    print("\n")
                    print(f"Consultorio {id} há {pessoas} pacientes a serem atendidos.")

            case 5:
                central.append(Consultorio(len(central)+1))

                with open("formato.txt", "w") as file:
                    file.write(f"ABRT: C{len(central)+1}\n")

            case 6:
                print(central[0].tamanho())




if __name__ == "__main__":
    Main()
