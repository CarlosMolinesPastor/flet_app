import flet
from flet import *

# Pagina de comunity de supabase
import os
from supabase import create_client, Client


## FUNCION MAIN
def main(page: Page):
    # Pagina de comunity de supabase
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    # Added
    listall = []
    tempapp = []
    alldata = Column()
    # Pagina
    data = data = supabase.table("Users").select("*").execute()

    name = TextField(label="Name")
    password = TextField(label="Password")

    def addToSupabase(e):
        data = (
            supabase.table("Users")
            .insert({"name": name.value, "password": password.value})
            .execute()
        )
        alldata.controls.append(
            Column(
                [
                    ListTile(
                        title=Text(name.value),
                        subtitle=Text(password.value),
                        trailing=IconButton(
                            icon=icons.DELETE_FOREVER_ROUNDED,
                            bgcolor="red500",
                            on_click=print("Delete"),
                        ),
                    )
                ],
                alignment="center",
            )
        )
        page.update()

    if not data:
        print("no data")
    else:
        # Listamos los datos de la tabla
        listall.append(data)
        tempapp = listall[0].data
        for element in tempapp:
            alldata.controls.append(
                Column(
                    [
                        ListTile(
                            title=Text(element["name"]),
                            subtitle=Text(element["password"]),
                            trailing=IconButton(
                                icon=icons.DELETE_FOREVER_ROUNDED,
                                bgcolor="red500",
                                on_click=print("Delete"),
                            ),
                        )
                    ],
                    alignment="center",
                )
            )

    page.add(
        Column(
            [
                name,
                password,
                FloatingActionButton(
                    icon=icons.ADD,
                    bgcolor="blue200",
                    on_click=addToSupabase,
                ),
                alldata,
            ],
            alignment="center",
        )
    )


# For Scroll page
page.scroll = "always"

flet.app(target=main)
