import flet
from flet import *

import routing
from SideBar import *
from AllFunctionality import *
from routing import *


# main application entry
def main(page: Page):
    page.title = 'Smart to Do Application'
    page.window_width = 450
    page.window_height = 800

    _container_ = Container(
        width=400,
        height=750,
        bgcolor='#041955',
        border_radius=30,
        animate=animation.Animation(1000, AnimationCurve.DECELERATE),
        animate_scale=animation.Animation(400, AnimationCurve.DECELERATE),
    )

    # initialize main frame
    main_frame = Main_Frame(page, _container_)

    # defining routing
    page.on_route_change = route_change
    page.go(page.route)

    container_ = Container(
        width=400,
        height=750,
        bgcolor='#041955',
        border_radius=30,
        content=Stack(
            controls=[
                main_frame.build()
            ]
        ),
    )

    page.add(container_)
    page.update()


if __name__ == '__main__':
    flet.app(target=main)
