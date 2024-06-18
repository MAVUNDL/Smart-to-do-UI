from flet import *


class Main_Frame(UserControl):
    list_of_categories = ['Business', 'Entertainment', 'Science', 'Technology']

    def __init__(self, page, animation_container):
        super().__init__()
        self.Task_listing = None
        self.information_icons = None
        # add icons
        self.icons_creation()
        # call the initialize function
        self.initialize_task_funct()
        # call to add tasks columns
        self.insert_tasks()
        # animation container
        self.animation_container = animation_container
        # will be set by the main function
        self.page = page

    # this function will handle the initialization of the button effect
    def initialize_task_funct(self):
        self.Task_listing = Stack(
            controls=[
                # columns task
                self.task_columns,
                # add button
                FloatingActionButton(
                    icon=icons.ADD,
                    on_click=lambda e: self.page.go('/create_task'),
                    bottom=2,
                    right=20,
                ),
            ]
        )

    # animation
    def animate_(self):
        if self.animation_container:
            if self.animation_container.width == 400:
                self.animation_container.animate_position = animation.Animation(1000, AnimationCurve.DECELERATE)
                self.animation_container.animate_size = animation.Animation(400, AnimationCurve.DECELERATE)
                self.animation_container.width = 120
                self.animation_container.right = 0
            else:
                self.animation_container.animate_position = animation.Animation(1000, AnimationCurve.DECELERATE)
                self.animation_container.animate_size = animation.Animation(400, AnimationCurve.DECELERATE)
                self.animation_container.width = 400
                self.animation_container.right = None
            self.page.update()

    # header information -> Icons set up
    def icons_creation(self):
        self.information_icons = Container(
            content=Column(
                controls=[
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            Container(
                                on_click=lambda e: self.animate_(),
                                content=Icon(
                                    icons.MENU,
                                ),
                            ),
                            Row(
                                controls=[
                                    Icon(
                                        icons.SEARCH
                                    ),
                                    Icon(
                                        icons.NOTIFICATIONS
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        )

    # Labels
    Header_text = Container(
        content=Column(
            controls=[
                Text(
                    value='Welcome back!'
                )
            ]
        )
    )
    Footer_text = Container(
        content=Column(
            controls=[
                Text(
                    value='CATEGORIES'
                )
            ]
        )
    )

    text_label = Text(
        value="Today's tasks"
    )

    # adding more categories
    def add_category(self, category_type) -> None:
        self.list_of_categories.append(category_type)

    # this will the card for the categories
    category_card = Row(
        scroll='auto',
    )

    # this will add each category type to a card
    for i, category in enumerate(list_of_categories):
        category_card.controls.append(
            Container(
                bgcolor='#041955',
                border_radius=20,
                width=170,
                height=110,
                padding=15,
                content=Column(
                    controls=[
                        Text('Task 01'),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=i * 30),
                            content=Container(
                                bgcolor='#eb06ff'
                            )
                        )
                    ]
                )
            )
        )

    # Creating a container to store the cards
    task_categories = Container(
        padding=padding.only(
            top=10,
            bottom=20,
        ),
        content=category_card
    )

    # listing of tasks
    task_columns = Column(
        height=300,
        scroll='auto',
    )

    # function to add task columns on page
    def insert_tasks(self):
        for i in range(10):
            self.task_columns.controls.append(
                Container(
                    height=50,
                    width=400,
                    bgcolor='#041955',
                    border_radius=15,
                    padding=padding.only(left=10),
                    content=Checkbox(
                        active_color='#eb06ff',
                        overlay_color='#fffff',
                        label=' ',
                        adaptive=True,
                        autofocus=True,
                        shape=RoundedRectangleBorder(
                            radius=24
                        ),
                    )
                )
            )

    # this function handles the routing of the button
    def onclick(self, e):
        self.page.go('/create_task')

    # add

    # all contents are added to this function
    def main_window(self) -> Container:
        raise NotImplemented

    def build(self):
        self.animation_container.content = Row(
            controls=[
                Container(
                    width=400,
                    height=750,
                    bgcolor='#3450a1',
                    border_radius=30,
                    padding=padding.only(
                        top=50,
                        left=20,
                        right=20,
                        bottom=5,
                    ),
                    content=Column(
                        controls=[
                            # Header Icons
                            self.information_icons,
                            # adding space between
                            Container(
                                height=20
                            ),
                            # text labels
                            self.Header_text,
                            self.Footer_text,
                            # task cards
                            self.task_categories,
                            # more labels
                            Container(
                                height=20,
                            ),
                            self.text_label,
                            # add button
                            self.Task_listing,

                        ]
                    )

                )
            ],
        )
        return self.animation_container
