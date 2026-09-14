import tkinter as tk


class MainView(tk.Frame):

    def __init__(
        self,
        master,
        servicio,
        cerrar_sesion
    ):

        super().__init__(master)

        self.pack(fill="both", expand=True)

        tk.Label(
            self,
            text="RESTAURANTE APP",
            font=("Arial", 16)
        ).pack()

        tk.Label(
            self,
            text="Productos"
        ).pack()

        lista_productos = tk.Listbox(
            self,
            width=60
        )

        lista_productos.pack()

        for producto in servicio.obtener_productos():

            lista_productos.insert(
                tk.END,
                str(producto)
            )

        tk.Label(
            self,
            text="Usuarios"
        ).pack()

        lista_usuarios = tk.Listbox(
            self,
            width=60
        )

        lista_usuarios.pack()

        for usuario in servicio.obtener_usuarios():

            lista_usuarios.insert(
                tk.END,
                str(usuario)
            )

        tk.Button(
            self,
            text="Ventas (Pendiente)",
            state="disabled"
        ).pack(
            pady=10
        )

        tk.Button(
            self,
            text="Cerrar sesión",
            command=cerrar_sesion
        ).pack()