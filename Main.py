from classes.Consultorio import Consultorio


def Main():
    #Inicializando o sistema com no mínimo três consultorios
    central = []
    consultorio1 = Consultorio(1)
    consultorio2 = Consultorio(2)
    consultorio3 = Consultorio(3)
    central.append(consultorio1)
    central.append(consultorio2)
    central.append(consultorio3)

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
                print("case 1")


if __name__ == "__main__":
    Main()
