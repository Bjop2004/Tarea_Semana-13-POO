from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self):

        datos_productos = ArchivoServicio.cargar(
            "datos/productos.json"
        )

        datos_usuarios = ArchivoServicio.cargar(
            "datos/usuarios.json"
        )

        self.productos = [
            Producto.desde_diccionario(p)
            for p in datos_productos
        ]

        self.usuarios = [
            Usuario.desde_diccionario(u)
            for u in datos_usuarios
        ]

    def validar_login(
        self,
        usuario,
        contrasena
    ):

        for u in self.usuarios:

            if (
                u.usuario == usuario
                and
                u.contrasena == contrasena
            ):
                return True

        return False

    def obtener_productos(self):

        return self.productos

    def obtener_usuarios(self):

        return self.usuarios