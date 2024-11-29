import os
import time
import flet as ft
from threading import Timer


def main(page: ft.Page):
    # Page Setup for Light Theme
    page.title = "LightsOut"
    page.window.width = 400
    page.window.height = 250
    page.padding = 20

    def shutdown_system():
        if os.name == "nt":  # Windows
            os.system("shutdown /s /t 1")
        elif os.name == "posix":  # macOS/Linux
            os.system("sudo shutdown now")

    def start_timer(e):
        try:
            minutes = int(input_field.value)
            seconds = minutes * 60
            output_text.value = f"Shutting down in {minutes} minute(s)..."
            output_text.color = "green"
            page.update()
            Timer(seconds, shutdown_system).start()
        except ValueError:
            output_text.value = "Invalid input. Please enter a valid number."
            output_text.color = "red"
            page.update()

    # UI Elements with Light Theme Colors
    header_text = ft.Text(
        "LightsOut",
        size=30,
        weight="bold",
        color="white",
    )
    label_text = ft.Text(
        "Please enter time below to schedule shutdown:",
        size=14,
        color="white",
    )
    input_field = ft.TextField(
        label="minutes",
        width=200,
        filled=True,
        fill_color="black",
        border_color="gray",
    )
    start_button = ft.IconButton(
        icon=ft.icons.ADD,
        icon_color="blue400",
        icon_size=30,
        tooltip="Pause record",
        on_click=start_timer,
    )
    output_text = ft.Text()

    # Add elements to page
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        header_text,
                        label_text,
                        ft.Row(
                            [input_field, start_button],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        output_text,
                    ],
                ),
                width=400,
                padding=10,
                border_radius=ft.border_radius.all(5),
            )
        )
    )


ft.app(target=main, assets_dir="assets")
