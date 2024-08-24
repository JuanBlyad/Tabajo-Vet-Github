class Medicamento:
    def __init__(self, nombre, dosis):
        self.nombre = nombre
        self.dosis = dosis

class Mascota:
    def __init__(self, nombre, numero_historia, tipo, peso, fecha_ingreso, medicamentos):
        self.nombre = nombre
        self.numero_historia = numero_historia
        self.tipo = tipo
        self.peso = peso
        self.fecha_ingreso = fecha_ingreso
        self.medicamentos = medicamentos

class ClinicaVeterinaria:
    def __init__(self):
        self.mascotas = []

    def ingresar_mascota(self, mascota):
        if len(self.mascotas) >= 10:
            return "No se pueden admitir más mascotas."
        for m in self.mascotas:
            if m.numero_historia == mascota.numero_historia:
                return "Ya existe una mascota con ese número de historia clínica."
        self.mascotas.append(mascota)
        return f"Mascota {mascota.nombre} ingresada con éxito."

    def ver_fecha_ingreso(self, numero_historia):
        for m in self.mascotas:
            if m.numero_historia == numero_historia:
                return m.fecha_ingreso
        return "La mascota no está en el sistema."

    def numero_mascotas(self):
        return len(self.mascotas)

    def ver_medicamentos(self, numero_historia):
        for m in self.mascotas:
            if m.numero_historia == numero_historia:
                return m.medicamentos
        return "La mascota no está en el sistema."

    def eliminar_mascota(self, numero_historia):
        for m in self.mascotas:
            if m.numero_historia == numero_historia:
                self.mascotas.remove(m)
                return True
        return False
