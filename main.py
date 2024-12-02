import os
import flet as ft
from threading import Timer


def main(page: ft.Page):
    # Page Setup
    page.title = "LightsOut"
    page.window.width = 400
    page.window.height = 300
    page.padding = 20

    # Retrieve the last saved time or set default manually
    last_time = page.client_storage.get("last_time")
    if last_time is None:
        last_time = "5"  # Default to 15 minutes

    def shutdown_system():
        if os.name == "nt":  # Windows
            os.system("shutdown /s /t 1")
        elif os.name == "posix":  # macOS/Linux
            os.system("sudo shutdown now")

    def start_timer(e):
        try:
            minutes = int(time_dropdown.value)
            seconds = minutes * 60
            output_text.value = f"Shutting down in {minutes} minute(s)..."
            output_text.color = "green"
            page.client_storage.set("last_time", str(minutes))  # Save selected time
            page.update()
            Timer(seconds, shutdown_system).start()
        except ValueError:
            output_text.value = "Something went wrong. Please try again."
            output_text.color = "red"
            page.update()

    # UI Elements
    header_text = ft.Text(
        "LightsOut",
        size=30,
        weight="bold",
        color="white",
    )
    label_text = ft.Text(
        "Select time from the dropdown to schedule shutdown:",
        size=14,
        color="white",
    )
    time_dropdown = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("5"),
            ft.dropdown.Option("10"),
            ft.dropdown.Option("15"),
            ft.dropdown.Option("30"),
            ft.dropdown.Option("45"),
            ft.dropdown.Option("60"),
            ft.dropdown.Option("90"),
            ft.dropdown.Option("120"),
        ],
        value=last_time,  # Set the last used time as default
    )
    start_button = ft.IconButton(
        icon=ft.icons.PLAY_ARROW,
        icon_color="blue400",
        icon_size=30,
        tooltip="Start timer",
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
                            [time_dropdown, start_button],
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
