class Nodo:
    def __init__(self, nombre, tipo, extension=None, peso=None):
        self.nombre = nombre
        self.tipo = tipo
        self.extension = extension
        self.peso = peso
        self.hijo1 = None
        self.hijo2 = None
        self.hijo3 = None
        self.hijo4 = None

    def agregar_hijo(self, hijo):
        if not self.hijo1:
            self.hijo1 = hijo
            return True
        elif not self.hijo2:
            self.hijo2 = hijo
            return True
        elif not self.hijo3:
            self.hijo3 = hijo
            return True
        elif not self.hijo4:
            self.hijo4 = hijo
            return True
        else:
            return False

    def buscar_hijo(self, nombre):
        for hijo in [self.hijo1, self.hijo2, self.hijo3, self.hijo4]:
            if hijo and hijo.nombre == nombre:
                return hijo
        return None

    def modificar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def modificar_extension(self, nueva_extension):
        self.extension = nueva_extension

    def modificar_peso(self, nuevo_peso):
        self.peso = nuevo_peso

    def imprimir(self, nivel=0):
        if self.tipo == 'Carpeta':
            print(' ' * nivel + f'📁 {self.nombre}')
        else:
            print(' ' * nivel + f'📄 {self.nombre}.{self.extension} ({self.peso} bytes)')
        for hijo in [self.hijo1, self.hijo2, self.hijo3, self.hijo4]:
            if hijo:
                hijo.imprimir(nivel + 1)


class Sistema:
    def __init__(self):
        self.raiz = Nodo('Raíz', 'Carpeta')

    def agregar_carpeta(self, carpeta_madre_nombre, carpeta_nombre):
        carpeta_madre = self.buscar_carpeta(carpeta_madre_nombre)
        if not carpeta_madre:
            print(f'No se encontró la carpeta madre {carpeta_madre_nombre}')
            return
        if carpeta_madre.buscar_hijo(carpeta_nombre):
            print(f'Ya existe una carpeta con el nombre {carpeta_nombre} en la carpeta madre {carpeta_madre_nombre}')
            return
        if not carpeta_madre.agregar_hijo(Nodo(carpeta_nombre, 'Carpeta')):
            print(f'La carpeta madre {carpeta_madre_nombre} ya está llena')

    def agregar_archivo(self, carpeta_madre_nombre, archivo_nombre, archivo_extension, archivo_peso):
        carpeta_madre = self.buscar_carpeta(carpeta_madre_nombre)
        if not carpeta_madre:
            print(f'No se encontró la carpeta madre {carpeta_madre_nombre}')
            return
        if any(hijo for hijo in [carpeta_madre.hijo1, carpeta_madre.hijo2,
                                 carpeta_madre.hijo3, carpeta_madre.hijo4]
               if hijo and hijo.nombre == archivo_nombre and hijo.extension == archivo_extension):
            print(
                f'Ya existe un archivo con el nombre {archivo_nombre} y extensión {archivo_extension} en la carpeta madre {carpeta_madre_nombre}')
            return
        if not carpeta_madre.agregar_hijo(Nodo(archivo_nombre, 'Archivo', archivo_extension, archivo_peso)):
            print(f'La carpeta madre {carpeta_madre_nombre} ya está llena')


    def buscar_carpeta(self, nombre, nodo_actual=None):
        if not nodo_actual:
            nodo_actual = self.raiz
        if nodo_actual.nombre == nombre and nodo_actual.tipo == 'Carpeta':
            return nodo_actual
        for hijo in [nodo_actual.hijo1, nodo_actual.hijo2,
                     nodo_actual.hijo3, nodo_actual.hijo4]:
            if hijo:
                resultado = self.buscar_carpeta(nombre, hijo)
                if resultado:
                    return resultado
        return None


    def buscar_archivo(self, nombre, nodo_actual=None):
        if not nodo_actual:
            nodo_actual = self.raiz
        if nodo_actual.nombre == nombre and nodo_actual.tipo == 'Archivo':
            return nodo_actual
        for hijo in [nodo_actual.hijo1, nodo_actual.hijo2,
                     nodo_actual.hijo3, nodo_actual.hijo4]:
            if hijo:
                resultado = self.buscar_archivo(nombre, hijo)
                if resultado:
                    return resultado
        return None


    def modificar_carpeta(self, carpeta_nombre_antiguo, carpeta_nombre_nuevo):
        carpeta = self.buscar_carpeta(carpeta_nombre_antiguo)
        if not carpeta:
            print(f'No se encontró la carpeta {carpeta_nombre_antiguo}')
            return
        if any(hijo for hijo in [carpeta.hijo1, carpeta.hijo2,
                                 carpeta.hijo3, carpeta.hijo4]
               if hijo and hijo.nombre == carpeta_nombre_nuevo):
            print(f'Ya existe una carpeta con el nombre {carpeta_nombre_nuevo} en el mismo nivel del árbol')
            return
        carpeta.modificar_nombre(carpeta_nombre_nuevo)


    def modificar_archivo(self, archivo_nombre_antiguo, archivo_nombre_nuevo=None,
                          archivo_extension_nueva=None, archivo_peso_nuevo=None):
        archivo = self.buscar_archivo(archivo_nombre_antiguo)
        if not archivo:
            print(f'No se encontró el archivo {archivo_nombre_antiguo}')
            return
        if archivo_nombre_nuevo:
            archivo.modificar_nombre(archivo_nombre_nuevo)
        if archivo_extension_nueva:
            archivo.modificar_extension(archivo_extension_nueva)
        if archivo_peso_nuevo:
            archivo.modificar_peso(archivo_peso_nuevo)


    def imprimir(self):
        self.raiz.imprimir()


def main():
    sistema = Sistema()
    while True:
        opcion = input('Menú:\n(i) Agregar carpeta\n(ii) Agregar archivo\n(iii) Modificar carpeta\n(iv) Modificar archivo\n(v) Imprimir árbol de carpetas\n(vi) Salir\n')
        if opcion == 'i':
            carpeta_madre_nombre = input('Nombre de la carpeta madre: ')
            carpeta_nombre = input('Nombre de la nueva carpeta: ')
            sistema.agregar_carpeta(carpeta_madre_nombre, carpeta_nombre)
        elif opcion == 'ii':
            carpeta_madre_nombre = input('Nombre de la carpeta madre: ')
            archivo_nombre, archivo_extension, archivo_peso = input('Nombre, extensión y peso del archivo (separados por espacios): ').split()
            archivo_peso = int(archivo_peso)
            sistema.agregar_archivo(carpeta_madre_nombre, archivo_nombre, archivo_extension, archivo_peso)
        elif opcion == 'iii':
            carpeta_nombre_antiguo = input('Nombre de la carpeta a modificar: ')
            carpeta_nombre_nuevo = input('Nuevo nombre de la carpeta: ')
            sistema.modificar_carpeta(carpeta_nombre_antiguo, carpeta_nombre_nuevo)
        elif opcion == 'iv':
            archivo_nombre_antiguo = input('Nombre del archivo a modificar: ')
            archivo_nombre_nuevo = input('Nuevo nombre del archivo (opcional): ')
            archivo_extension_nueva = input('Nueva extensión del archivo (opcional): ')
            archivo_peso_nuevo = input('Nuevo peso del archivo (opcional): ')
            if not archivo_peso_nuevo:
                archivo_peso_nuevo = None
            else:
                archivo_peso_nuevo = int(archivo_peso_nuevo)
            sistema.modificar_archivo(archivo_nombre_antiguo, archivo_nombre_nuevo,
                                      archivo_extension_nueva, archivo_peso_nuevo)
        elif opcion == 'v':
            sistema.imprimir()
        elif opcion == 'vi':
            break


if __name__ == '__main__':
    main()
