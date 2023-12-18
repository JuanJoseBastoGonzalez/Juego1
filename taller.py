import os

alumnos = []
isActive = True
menu = "1. Registrar Alumno\n2. Registrar Notas\n3. Mostrar Alumnos\n4. Salir\n: "
subMenuNotas = ["Parciales", "Quices", "Trabajos", "Regresar al menu principal"]

while isActive:
    os.system("cls")
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato ingresado")
        os.system("pause")
    else:
        if opMenu == 1:
            rta = "S"
            while rta in ["S", "s"]:
                codigo = input("Ingrese el código del estudiante: \n")
                nombre = input("Ingrese el nombre del estudiante: \n")
                edad = int(input(f"Ingrese la edad del estudiante {nombre}: \n"))
                alumno = [codigo, nombre, edad, [], [], []]
                alumnos.append(alumno)
                print(alumnos)
                os.system("pause")
                rta = input("Desea agregar otro alumno? S[si] o N[no]: ").upper()
                
        elif opMenu == 2:  # Notas
            isActiveGrades = True
            while isActiveGrades:
                os.system("cls")
                codigoE = input("Ingrese el código del estudiante: \n")
                for i, item in enumerate(alumnos):
                    if codigoE == item[0]:
                        for j, nota in enumerate(subMenuNotas):
                            print(f"{j+1}. {nota}")
                        try:
                            opNotas = int(input(": "))
                        except ValueError:
                            print("Error en el dato ingresado")
                            os.system("pause")
                        else:
                            reiterar = True
                            if opNotas == 1:
                                while reiterar:
                                    try:
                                        alumnoNota = int(input(f"Ingrese su nota: \nNota actual: {alumnos[i][opNotas + 2]}"))
                                       
                                    except:
                                            print("Error en el dato ingresado")
                                            os.system("pause")
                                    else:        
                                        alumnos[i][opNotas + 2] += [alumnoNota]
                                        otraNota = input("Desea agregar otra nota? S[si] o N[no]: ").upper()
                                        if otraNota in ["N","n"]:
                                            reiterar = False
                                            
                            elif opNotas == 2:
                                try:
                                 alumnoNota = int(input(f"Ingrese su nota: \nNota actual: {alumnos[i][opNotas + 2]}"))
                                except:
                                    print("Error en el dato ingresado")
                                    os.system("pause")
                                else:        
                                    alumnos[i][opNotas + 3] += [alumnoNota]  # Error en esta línea
                                    otraNota = input("Desea agregar otra nota? S[si] o N[no]: ").upper()
                                    if otraNota in ["N","n"]:
                                        reiterar = False

                            elif opNotas ==3:
                                    try:
                                        alumnoNota = int(input(f"Ingrese su nota: \nNota actual: {alumnos[i][opNotas + 2]}"))
                                       
                                    except:
                                            print("Error en el dato ingresado")
                                            os.system("pause")
                                    else:        
                                        alumnos[i][opNotas + 3] += [alumnoNota]
                                        otraNota = input("Desea agregar otra nota? S[si] o N[no]: ").upper()
                                        if otraNota in ["N","n"]:
                                            reiterar = False
                            elif opNotas == 4:
                                isActiveGrades = False
                            else:
                                print("terminar luego")
                    else:
                        print("El código no existe")
                        os.system("pause")

        elif opMenu == 3:
            os.system("cls")
            print("Lista de alumnos:")
            for item in alumnos:
                print(item)
            os.system("pause")

        elif opMenu == 4:
            os.system("cls")
            
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            os.system("cls")
            print("Opción inválida")
        os.system("pause")
