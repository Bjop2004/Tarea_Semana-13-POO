class Usuario:

    def __init__(
        self,
        usuario,
        contrasena,
        nombre
    ):

        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre

    @staticmethod
    def desde_diccionario(data):

        return Usuario(
            data["usuario"],
            data["contrasena"],
            data["nombre"]
        )

    def __str__(self):

        return self.nombre