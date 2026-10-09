import flet as ft

def main(page: ft.Page):
    page.title = "Mi Primera App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Un texto sencillo para probar que funciona
    texto = ft.Text("¡Hola, ya funciona mi app!", size=20)
    
    def saludar(e):
        texto.value = "¡Botón presionado con éxito!"
        page.update()

    boton = ft.ElevatedButton("Haz clic", on_click=saludar)

    page.add(
        ft.Column([
            texto,
            boton
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)
