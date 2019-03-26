# Autor: Mario Hernández Cárdenas
# Tarea Ciclos While


def dividir(dividendo, divisor):

    veces = 0
    residuo = dividendo
    while residuo >= divisor:
        dividendo - divisor
        veces += 1
        residuo -= divisor
    print(dividendo, "/", divisor, "=", veces, ", sobra", residuo, "\n")


def encontrarMayor():
    valor = int(input("Teclea un número [-1 para salir]: "))
    valorMayor = valor
    if valor == -1:
        print("No hay valor mayor")
    else:
        valorGuardado = 0
        while valorMayor != -1:
            if valorMayor >= valor:
                valorGuardado += valorMayor
                valorMayor = int(input("Teclea un número [-1 para salir]: "))
            else:
                valorMayor = int(input("Teclea un número [-1 para salir]: "))
        print("El mayor es:", valorGuardado, "\n")


def main():
    print("\nMisión 07. Ciclos while\n"
          "Autor: Mario Hernández Cárdenas\n"
          "Matrícula: A01375869\n"
          "1. Calcular divisiones\n"
          "2. Encontrar el mayor\n"
          "3. Salir")
    opcion = int(input("Teclea tu opción: "))

    while opcion != 3:
        if opcion < 1 or opcion > 3:
                print("ERROR, teclea 1, 2, o 3\n")
                print("\nMisión 07. Ciclos while\n"
                      "Autor: Mario Hernández Cárdenas\n"
                      "Matrícula: A01375869\n"
                      "1. Calcular divisiones\n"
                      "2. Encontrar el mayor\n"
                      "3. Salir")
                opcion = int(input("Teclea tu opción: "))

        elif opcion == 1:
            print("\nCalculando divisiones")
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividir(dividendo, divisor)

            print("\nMisión 07. Ciclos while\n"
                  "Autor: Mario Hernández Cárdenas\n"
                  "Matrícula: A01375869\n"
                  "1. Calcular divisiones\n"
                  "2. Encontrar el mayor\n"
                  "3. Salir")
            opcion = int(input("Teclea tu opción: "))

        elif opcion == 2:
            print("\nTeclea una serie de números para encotrar el mayor.")
            encontrarMayor()

            print("\nMisión 07. Ciclos while\n"
                  "Autor: Mario Hernández Cárdenas\n"
                  "Matrícula: A01375869\n"
                  "1. Calcular divisiones\n"
                  "2. Encontrar el mayor\n"
                  "3. Salir")
            opcion = int(input("Teclea tu opción: "))

    print("\nGracias por usar este programa, regresa pronto.")


main()
