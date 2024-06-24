import sys

import flet
from flet import *
from AllFunctionality import Main_Frame
from routing import route_change
from database import init_db


# main application entry
def main(page: Page):
    page.title = 'Smart to Do Application'
    page.window_width = 450
    page.window_height = 800

    # Initialize the database
    init_db()

    #
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    # Initialize animation container
    animation_container = Container(
        width=400,
        height=750,
        bgcolor='#041955',
        border_radius=30,
        animate=animation.Animation(1000, AnimationCurve.DECELERATE),
        animate_scale=animation.Animation(400, AnimationCurve.DECELERATE),
    )

    # Initialize Main_Frame
    main_frame = Main_Frame(page, animation_container)

    # Store main_frame in page for access in route_change
    page.main_frame = main_frame

    #
    circle = Stack(
        controls=[
            Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor='white12'
            ),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=['#00000000', PINK],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(
                    alignment='center',
                    controls=[
                        Container(
                            padding=padding.all(5),
                            bgcolor=BG,
                            width=90, height=90,
                            border_radius=50,
                            content=Container(
                                bgcolor=FG,
                                height=80, width=80,
                                border_radius=40,
                                content=CircleAvatar(
                                    opacity=0.8,
                                    foreground_image_url="https://img.freepik.com/free-photo/cute-kid-cartoon-illustration_1409-5978.jpg?t=st=1719230928~exp=1719234528~hmac=b0e40c1e89fec16375be280acf3b1ca7af09e162b8ddeb13389443653beabe94&w=996"
                                )
                            )
                        )
                    ],
                ),
            ),
        ]
    )

    # Create a main container for the page
    container = Container(
        width=400,
        height=750,
        bgcolor='#041955',
        border_radius=30,
        content=Stack(
            controls=[
                Container(
                    padding=padding.only(left=20),
                    content=Column(
                        controls=[
                            Container(height=20),
                            circle,
                            Text('Skhumbuzo\nBembe', size=32, weight='bold'),
                            Container(height=25),
                            Row(controls=[
                                IconButton(icons.NOTIFICATIONS_OFF_SHARP),
                                Text('Turn off notifications', size=15, weight=FontWeight.W_300, color='white',
                                     font_family='poppins')
                            ]),
                            Container(height=5),
                            Row(controls=[
                                IconButton(icons.NOW_WIDGETS),
                                Text('Widget', size=15, weight=FontWeight.W_300, color='white',
                                     font_family='poppins')
                            ]),
                            Container(height=5),
                            Row(controls=[
                                IconButton(icons.LOGIN_ROUNDED, on_click=lambda e: page.window_close()),
                                Text('Exit', size=15, weight=FontWeight.W_300, color='white',
                                     font_family='poppins')
                            ]),
                            Image(src=f"/images/1.png",
                                  width=300,
                                  height=200,
                                  ),
                            Text('Good', color="#3450a1", font_family='poppins', ),
                            Text('Consistency', size=22, )
                        ],
                    )
                ),
                main_frame.build()
            ],
        ),
    )

    # Add the main container to the page
    page.add(container)

    # Update the page to render changes
    page.update()

    # Set route change handler after the main container has been added
    page.on_route_change = route_change

    # Initial route navigation
    page.go(page.route)


if __name__ == '__main__':
    # Start the Flet application with the main function
    flet.app(target=main)
