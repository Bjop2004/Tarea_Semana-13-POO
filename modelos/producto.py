class Producto:

    def __init__(self, codigo, nombre, categoria, precio):

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    @staticmethod
    def desde_diccionario(data):

        return Producto(
            data["codigo"],
            data["nombre"],
            data["categoria"],
            data["precio"]
        )

    def __str__(self):

        return (
            f"{self.codigo} - "
            f"{self.nombre} - "
            f"{self.categoria} - "
            f"${self.precio}"
        )