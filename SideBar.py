from flet import *


class Side_Bar(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            width=400,
            height=750,
            bgcolor='#041955',
            border_radius=30,
        )
