from clinica_veterinaria import Medicamento, Mascota, ClinicaVeterinaria

def main():
    clinica = ClinicaVeterinaria()
    while True:
        print("\nIngrese una opción:")
        print("1- Ingresar una mascota")
        print("2- Ver fecha de ingreso")
        print("3- Ver número de mascotas en el servicio")
        print("4- Ver medicamentos que se están administrando")
        print("5- Eliminar mascota")
        print("6- Salir")
        opcion = int(input("Usted ingresó la opción: "))

        if opcion == 1:
            if clinica.numero_mascotas() >= 10:
                print("No hay espacio para más mascotas.")
                continue
            numero_historia = input("Ingrese el número de historia clínica: ")
            if clinica.ver_fecha_ingreso(numero_historia) != "La mascota no está en el sistema.":
                print("Ya existe una mascota con ese número de historia clínica.")
                continue
            nombre = input("Ingrese el nombre de la mascota: ")
            tipo = input("Ingrese el tipo (canino/felino): ")
            peso = float(input("Ingrese el peso: "))
            fecha_ingreso = input("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
            medicamentos = []
            num_medicamentos = int(input("Ingrese el número de medicamentos: "))
            for _ in range(num_medicamentos):
                nombre_med = input("Ingrese el nombre del medicamento: ")
                dosis = input("Ingrese la dosis del medicamento: ")
                medicamentos.append(Medicamento(nombre_med, dosis))
            mascota = Mascota(nombre, numero_historia, tipo, peso, fecha_ingreso, medicamentos)
            mensaje = clinica.ingresar_mascota(mascota)
            print(mensaje)

        elif opcion == 2:
            numero_historia = input("Ingrese el número de historia clínica: ")
            fecha_ingreso = clinica.ver_fecha_ingreso(numero_historia)
            print("La fecha de ingreso de la mascota es: " + fecha_ingreso)

        elif opcion == 3:
            numero = clinica.numero_mascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif opcion == 4:
            numero_historia = input("Ingrese el número de historia clínica: ")
            medicamentos = clinica.ver_medicamentos(numero_historia)
            if medicamentos != "La mascota no está en el sistema.":
                print("Los medicamentos suministrados son: ")
                for med in medicamentos:
                    print(f"\n- {med.nombre}")
            else:
                print(medicamentos)

        elif opcion == 5:
            numero_historia = input("Ingrese el número de historia clínica: ")
            resultado_operacion = clinica.eliminar_mascota(numero_historia)
            if resultado_operacion:
                print("Mascota eliminada del sistema con éxito.")
            else:
                print("No se ha podido eliminar la mascota. La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif opcion == 6:
            confirmacion = input("¿Está seguro que desea salir? (s/n): ")
            if confirmacion.lower() == 's':
                print("Saliendo del sistema.")
                break
            else:
                print("Operación cancelada.")

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
