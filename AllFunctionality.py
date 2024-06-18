from flet import *
from database import insert_task, get_tasks, delete_task


class Main_Frame(UserControl):
    list_of_categories = ['Welcome']

    def __init__(self, page, animation_container):
        super().__init__()
        self.Task_listing: Stack = None
        self.information_icons = None
        self.animation_container = animation_container
        self.page = page

        # Track the number of tasks per category
        self.tasks_per_category = {category: 0 for category in self.list_of_categories}

        # Initialize task columns
        self.task_columns = Column(
            height=300,
            scroll='auto',
        )

        # Initialize controls
        self.icons_creation()
        self.initialize_task_funct()
        self.insert_tasks("Welcome")
        self.load_tasks_from_db()  # Load tasks from the database

    def initialize_task_funct(self):
        # Initialize Task_listing with task_columns and FloatingActionButton
        self.Task_listing = Stack(
            controls=[
                self.task_columns,
                FloatingActionButton(
                    icon=icons.ADD,
                    on_click=lambda e: self.page.go('/create_task'),
                    bottom=2,
                    right=20,
                ),
            ],
            width=400,
            height=300,
        )

    def update_task_listing(self, task_name: str, category: str = 'Demo'):
        task_id = insert_task(task_name, category)  # Save new task to the database and get its ID

        task_container = Container(
            height=50,
            width=400,
            bgcolor='#041955',
            border_radius=15,
            padding=padding.only(left=10),
            content=Row(
                controls=[
                    Checkbox(
                        active_color='#eb06ff',
                        overlay_color='#fffff',
                        label=task_name,
                        adaptive=True,
                        autofocus=True,
                        shape=RoundedRectangleBorder(radius=24),
                    ),
                    IconButton(
                        icon=icons.DELETE,
                        on_click=lambda e, task_id=task_id: self.delete_task(task_id, task_container, category)
                    ),
                ],
                alignment='spaceBetween'
            )
        )

        self.task_columns.controls.append(task_container)

        # Update the category list and task count
        if category not in self.tasks_per_category:
            self.add_category(category)
        self.tasks_per_category[category] += 1

        self.update_task_columns()
        self.update_category_cards()  # Update category cards after adding a task

    def delete_task(self, task_id, task_container, category):
        # Delete task from the database
        delete_task(task_id)

        # Check if the task_container exists in self.task_columns.controls before removing
        if task_container in self.task_columns.controls:
            self.task_columns.controls.remove(task_container)
        else:
            print(f"Task container not found in controls: {task_container}")

        # Update the task count for the category
        if category in self.tasks_per_category:
            self.tasks_per_category[category] -= 1
            if self.tasks_per_category[category] == 0:
                del self.tasks_per_category[category]
                self.list_of_categories.remove(category)

        self.update_task_columns()
        self.update_category_cards()  # Update category cards after deleting a task

    def update_task_columns(self):
        try:
            # Ensure controls are updated properly
            self.task_columns.update()
            self.Task_listing.update()
            self.page.update()
        except AssertionError as e:
            pass

    def update_category_cards(self):
        if not self.page:
            return

        self.category_card.controls.clear()
        for i, category in enumerate(self.list_of_categories):
            task_count = self.tasks_per_category.get(category, 0)
            self.category_card.controls.append(
                Container(
                    bgcolor='#041955',
                    border_radius=20,
                    width=170,
                    height=110,
                    padding=15,
                    content=Column(
                        controls=[
                            Text(f'Task {task_count:02d}'),
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
        try:
            self.task_categories.update()
        except AssertionError as e:
            pass

    def load_tasks_from_db(self):
        # Load tasks from the database and update the UI
        tasks = get_tasks()
        for task_id, name, category in tasks:
            self.update_task_listing(name, category)

    def animate_(self):
        # Animation logic for animation_container
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

    def icons_creation(self):
        # Create information_icons
        self.information_icons = Container(
            content=Column(
                controls=[
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            Container(
                                on_click=lambda e: self.animate_(),
                                content=Icon(icons.MENU),
                            ),
                            Row(
                                controls=[
                                    Icon(icons.SEARCH),
                                    Icon(icons.NOTIFICATIONS)
                                ]
                            )
                        ]
                    )
                ]
            )
        )

    Header_text = Container(
        content=Column(
            controls=[
                Text(
                    value='Welcome back!',
                    color='white',
                    font_family='poppins',
                    size=32, weight='bold'
                )
            ]
        )
    )

    Footer_text = Container(
        content=Column(
            controls=[
                Text(
                    value='CATEGORIES',
                    weight=FontWeight.W_300, color='white', font_family='poppins',
                    size=22
                )
            ]
        )
    )

    text_label = Text(
        value="Today's tasks",
        weight=FontWeight.W_300, color='white', font_family='poppins'
    )

    def add_category(self, category_type) -> None:
        if category_type not in self.list_of_categories:
            self.list_of_categories.append(category_type)
            self.tasks_per_category[category_type] = 0

    category_card = Row(
        scroll='auto',
    )

    task_categories = Container(
        padding=padding.only(
            top=10,
            bottom=20,
        ),
        content=category_card
    )

    def insert_tasks(self, text_input: str):
        # Insert new task into task_columns
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
                    label=text_input,
                    adaptive=True,
                    autofocus=True,
                    shape=RoundedRectangleBorder(radius=24),
                )
            )
        )

    def onclick(self, e):
        # Handle button click routing
        self.page.go('/create_task')

    def build(self):
        # Build animation_container content
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
                            self.information_icons,
                            Container(height=20),
                            self.Header_text,
                            self.Footer_text,
                            self.task_categories,
                            Container(height=20),
                            self.text_label,
                            self.Task_listing,
                        ]
                    )
                )
            ]
        )
        return self.animation_container
