class Coleccion_de_datos:
    def __init__(self,departamento,municipio,cultivo,numero_registros):
        self.departamento = departamento
        self.municipio = municipio
        self.cultivo = cultivo
        self.numero_registros = numero_registros

    def imprima(self):
        print(f'Departamento: {self.departamento} | Municipio: {self.municipio} | Cultivo: {self.cultivo}')

#   def retorno_de_coleccion_de_datos():   // para la api


def menu_desplegable():
    while True:
        print('DIGITE ') 
        departamento = (input("Departamento: "))
        municipio = input('Municipio: ')
        cultivo = input('Cultivo: ')
        cantidad_registros = input('Numero de registros a consultar[inferior a 500]: ')
        coleccion = Coleccion_de_datos(departamento,municipio,cultivo)
        coleccion.imprima()
