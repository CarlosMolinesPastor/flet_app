import flet
from flet import *


def main(page: Page):
    name = TextField(label="Nombre")
    passw = TextField(label="Contraseña")
    mensaje = Text("", height=120)
    anyadir = []

    def anyadir_lista(e):
        if name is None:
            print("Falta algun dato")
        else:
            anyadir.append({name.value, passw.value})
            page.add(
                Container(
                    Row(
                        [
                            Text("User: " + name.value),
                            Text("Password: " + passw.value),
                        ]
                    )
                )
            )
            name.value = ""
            passw.value = ""
            page.update()
            print(anyadir)

    def mostrar_lista(e):
        if not anyadir:
            mensaje.value = "La lista esta vacia"
        else:
            temp = ""
            for i in anyadir:
                temp = temp + str(i) + ", "
                mensaje.value = temp
        page.update()

    def borrar_lista(e):
        anyadir.clear()
        mensaje.value = "La lista esta vacia"
        recargar_pagina()
        page.update()

    def recargar_pagina():
        page.clean()
        inicia()

    def inicia():
        page.add(
            Column(
                controls=[
                    name,
                    passw,
                    Row(
                        [
                            ElevatedButton(
                                "Add", bgcolor="Blue100", on_click=anyadir_lista
                            ),
                            ElevatedButton(
                                "Mostrar Lista",
                                bgcolor="Green100",
                                on_click=mostrar_lista,
                            ),
                            ElevatedButton(
                                "Borrar Lista", bgcolor="Red100", on_click=borrar_lista
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    mensaje,
                ]
            )
        )

        page.update()
        
    inicia()

app(target=main)
