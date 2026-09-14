# Restaurante App - (Semana 13)

Este proyecto corresponde a la **Semana 13** de la materia Programación Orientada a Objetos (POO). Representa la primera versión de la interfaz gráfica de usuario (GUI) desarrollada con **Tkinter**, migrando el sistema base del restaurante desde una aplicación de consola a una arquitectura visual modular.

En esta fase inicial, la aplicación se enfoca únicamente en la gestión e interacción de información base: **usuarios** y **productos**.

---

## 📌 Alcance de la Versión (Semana 13)

### ✅ Funcionalidades Incluidas
* **Autenticación (Login):** Validación de credenciales de usuario contra un archivo persistente `.json`.
* **Vista Principal (MainView):** Carga y visualización dinámica de las listas de productos y usuarios.
* **Persistencia de Datos:** Lectura e hidratación de objetos desde archivos JSON (`productos.json` y `usuarios.json`).
* **Navegación de Ventana Única:** Cambio fluido entre la vista de Login y la vista Principal destruyendo y redibujando marcos (`tk.Frame`) dentro de una sola ventana contenedora.
* **Cierre de Sesión:** Opción para finalizar la sesión actual y regresar a la pantalla de Login.

---

## 📂 Estructura del Proyecto

El proyecto aplica una arquitectura en capas separando la presentación (UI), la lógica de negocio (servicios) y las entidades (modelos):

```text
restaurante_app/
│
├── datos/
│   ├── productos.json       # Persistencia de datos de productos
│   └── usuarios.json        # Persistencia de datos de usuarios
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase entidad Producto
│   └── usuario.py           # Clase entidad Usuario
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py  # Servicio genérico de lectura JSON
│   └── restaurante_servicio.py # Lógica de negocio y manejo de listas
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py        # Interfaz del formulario de autenticación
│   └── main_view.py         # Interfaz principal con listas de datos
│
├── main.py                  # Punto de entrada de la aplicación
└── README.md                # Documentación del proyecto
