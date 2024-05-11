# Modulos importamos flet y sqlite3
import flet
import sqlite3
# Rutas, de fleto importamos todo y de datetime importamos datetime
from flet import *
from datetime import datetime


#Creamos la clase FormContainer que hereda de UserControl y muestra el
#formulario para añadir tareas a la lista
class Formulario(UserControl):
    #Creamos el constructor de la clase
    def __init__(self):
        # Creamos una funcion
        self.func = lambda e: print("Añadir tarea")
        #Llamamos al constructor de la clase UserControl
        super().__init__()

    #Creamos el metodo build que retorna un contenedor con un formulario
    def build(self):
        return Container(
            width=280,
            height=80,
            bgcolor="bluegrey500",
            opacity=0,  #cambiamos mas tarde cuando le damos el boton añadir tarea
            border_radius=40,
            margin=margin.only(left=-20, right=-20),
            animate=animation.Animation(400, "decelerate"),
            animate_opacity=200,
            padding=padding.only(top=45, bottom=45),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    TextField(
                        height=48,
                        width=255,
                        filled=True,
                        text_size=12,
                        color="black",
                        border_color="transparent",
                        hint_text="Descripción...",
                        hint_style=TextStyle(
                            size=11,
                            color="black", ),
                    ),
                    IconButton(
                        content=Text(
                            "Añadir tarea"
                        ),
                        width=180,
                        height=44,
                        on_click=self.func,
                        style=ButtonStyle(
                            bgcolor={"": "black"},
                            shape={
                                "": RoundedRectangleBorder(radius=8),
                            },
                        ),
                    ),
                ]
            ),
        )


# Creamos la funcion main
def main(page: Page):
    # Alineamos la pagina horizontal y verticalmente
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # Funcion para expandir y esconder el formulario
    def CreateToDo(e):
        #Cuando hacemos click en el boton añadir tarea, se expande
        # el formulario y cambia la opacidad
        if form.height != 200:
            form.height, form.opacity = 200, 1,
            form.update()
        else:
            form.height, form.opacity = 80, 0,
            form.update()
        pass

    # Creamos una columna principal para la pagina
    __main_column__ = Column(
        scroll="hidden",
        expand=True,
        alignment=MainAxisAlignment.START,
        controls=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Text("Tareas", size=18, weight="bold"),
                    IconButton(
                        icons.ADD_CIRCLE_ROUNDED,
                        icon_size=18,
                        on_click=lambda e: CreateToDo(e),
                    )
                ],
            ),
            Divider(height=8, color="white24"),
        ],
    )

    # Añadimos a la pagina un contenedor
    page.add(
        Container(
            # Definimos el ancho y alto de la pagina
            width=1500,
            height=800,
            margin=-10,
            bgcolor="bluegrey800",
            alignment=alignment.center,
            # Anadimos una fila a la pagina
            content=Row(
                # Alineamos la fila horizontal y verticalmente
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                # Anadimos controles a la fila
                controls=[
                    #Anadimos un contenedor
                    Container(
                        # Definimos el ancho y alto del contenedor
                        width=280,
                        height=600,
                        bgcolor="#0f0f0f",
                        border_radius=40,
                        border=border.all(0.5, "white"),
                        padding=padding.only(top=35, left=20, right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE,  # el clip contiene el contenido del contenedor
                        # Anadimos una columna
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                # La columna principal
                                __main_column__,
                                # Añadimos el formulario que devuelve la clase Formulario un contenedor
                                Formulario(),
                            ]
                        ),

                    ),
                ]
            ),
        ),
    )
    page.update()

    # Creamos una variable form que contiene el formulario
    form = page.controls[0].content.controls[0].content.controls[1].controls[0]


# Si el archivo se ejecuta directamente, ejecutamos la aplicacion
if __name__ == '__main__':
    flet.app(target=main)
