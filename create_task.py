from flet import *


class Task_section(UserControl):
    def __init__(self):
        super().__init__()
        self.back_button = None
        # initialize button
        self.back_to_mainButton()

    def back_to_mainButton(self):
        self.back_button = IconButton(
            icon=icons.ARROW_BACK,
            on_click=lambda e: self.page.go('/')
        )

    def build(self):
        return Container(
            width=400,
            height=750,
            bgcolor='#3450a1',
            border_radius=30,
            padding=padding.only(left=10, top=10),
            content=Column(
                controls=[
                    Row(
                        controls=[
                            self.back_button,
                        ]
                    )
                ]
            )
        )
