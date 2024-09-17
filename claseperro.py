print("Clases version 2 el constructor")

class Perro:
    # Funcion Constructor
    def __init__(self, color , edad) :
        self.color=color
        self.edad=edad
# Funciones creadas por el usuario
    def muerde(self):
            print("Chale el perro me mordio")
    def chatperro(self,mensaje):
            print(f"Chat perrro: {mensaje}")        
    def chatperra(self,mensajepe):
        print(f"Chat perra: {mensajepe}")
    def datos(self):   
        print(f"Color: {self.color}  Edad: {self.edad}")
        # crear el objeto
chihuas=Perro("Negro",2)
        # Llamadas a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.chatperra("Hola boby")
chihuas.chatperro("Quieres ser mi chava?")
chihuas.chatperra("grrru....")