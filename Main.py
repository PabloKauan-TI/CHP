from classes.Consultorio import Consultorio

from classes.Paciente import Paciente


def Main():
    #Inicializando o sistema com no mínimo três consultorios
    central = []
    consultorio1 = Consultorio(1)
    consultorio2 = Consultorio(2)
    consultorio3 = Consultorio(3)
    central.append(consultorio1)
    central.append(consultorio2)
    central.append(consultorio3)

    with open("formato.txt", "W") as file:
        file.write("")

    S = 0
    while S != 7:
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

            case 2:
                consultorio = int(input("Qual o consultorio: "))
                central[consultorio-1].atender()
            case 3:
                atendePaciente = int(input("Digite o consultorio que irá atender o paciente: "))
                enviaPaciente = int(input("Digite o consultorio que irá enviar o paciente para o atendimento: "))
                paciente = central[enviaPaciente-1].atender()

                with open("formato.txt", "a") as file:
                    file.write(f"\n{atendePaciente}" + paciente  + f" {enviaPaciente}")
                
            case 4:
                for consultorio in central:
                    consultorio.imprimir()
            case 5:
                print("case 5")
            case 6:
                print("case 6")


if __name__ == "__main__":
    Main()
