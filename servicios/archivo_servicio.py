import json


class ArchivoServicio:

    @staticmethod
    def cargar(ruta):

        with open(
            ruta,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(archivo)