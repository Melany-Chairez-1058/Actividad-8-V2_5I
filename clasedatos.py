class Informacion:
    def mi_lista(self):
        Lista_nomperros=["Boby","Dollar","Fany"]
        for x in Lista_nomperros:
            print(x)
    def mi_tupla(self):
        tuplas_raza=("chihuaha","golden retriever","husky")
        for x in tuplas_raza:
            print(x)
    def mi_conjunto(self):
        conjunto_colores={"cafe","rubio","gris"}
        for x in conjunto_colores:
            print(x)
    def mi_dic(self):
        dic_edades={
        "Boby":" 3 años",
        "Dollar":" 2 años ",
        "Fany":" 4 años"
            }
        for x,y in dic_edades.items():
            print(x,y)
#creando  el objeto
datos=Informacion()
print("\n Listado de nombre de perro ")
datos.mi_lista()
print("\n Listado razas de perros")
datos.mi_tupla()
print("\n Listado colores de perros")
datos.mi_conjunto()
print("\n Listado edades de perros")
datos.mi_dic()