import os 


def dia_da_semana():
    os.system ("cls || clear")

    while True:
        try:
            numero = int(input("Digite um dia da semana de 1 a 7: "))

            match(numero):
                case 1:
                    print("Domingo na fé de cristo \n Final de semana.\n"
                          f"Programacao aleatoria")
                    break
                case 2:
                    print("Segunda feira abencoada. \n "
                          f"05:00 - 06:00  - Acorda\n Tomar café\n Escovar os dentes\n Tomar banho"
                          f"06:20 - 11:30 - SENAI "
                          f"13:20 - Tomar banho \n Almocar \n "
                          f"15:00 - 17:00 - Estudar Python POO\n"
                          f"17:20 - Banco de dados\n"
                          f"Lazer e gratidao\n")
                    break
                case 3:
                    print("Terça - feira \n "
                          f"05:00 - 06:00  - Acorda\n Tomar café\n Escovar os dentes\n Tomar banho"
                          f"06:20 - 11:30 - SENAI "
                          f"13:20 - Tomar banho \n Almocar \n "
                          f"15:00 - 17:00 - Estudar Python POO \n"
                          f"17:20 - Banco de dados \n"
                          f"Lazer e gratidao\n")
                    break
                case 4:
                    print("Quarta - feira \n "
                          f"05:00 - 06:00  - Acorda\n Tomar café\n Escovar os dentes\n Tomar banho"
                          f"06:20 - 11:30 - SENAI\n"
                          f"13:20 - Tomar banho \n Almocar \n "
                          f"15:00 - 17:00 - Estudar Python POO\n"
                          f"17:20 - Banco de dados\n"
                          f"Lazer e gratidao\n")
                    break
                case 5:
                    print("Quinta - feira \n "
                          f"05:00 - 06:00  - Acorda\n Tomar café\n Escovar os dentes\n Tomar banho"
                          f"06:20 - 11:30 - SENAI "
                          f"13:20 - Tomar banho \n Almocar \n "
                          f"15:00 - 17:00 - Estudar Python POO\n"
                          f"17:20 - Banco de dados\n"
                          f"Lazer e gratidao\n")
                    break
                case 6:
                    print("Sexta - feira  \n "
                          f"05:00 - 06:00  - Acorda\n Tomar café\n Escovar os dentes\n Tomar banho"
                          f"06:20 - 11:30 - SENAI "
                          f"13:20 - Tomar banho \n Almocar \n "
                          f"15:00 - 17:00 - Estudar Python POO\n"
                          f"17:20 - Banco de dados\n"
                          f"Lazer e gratidao\n")
                case 7:
                    print("Sabado \n Final de semana.\n"
                          f"Programacao aleatoria")

                case _:
                    input("Opção invalida")

        except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
                continue
dia_da_semana()