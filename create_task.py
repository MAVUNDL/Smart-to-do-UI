from flet import *

class Task_section(UserControl):
    def __init__(self, task_submit_callback):
        super().__init__()
        self.back_button = None
        self.New_task_category: TextField = None
        self.New_task_name: TextField = None
        self.Task_list: list = ["start"]
        self.update_value: bool = False
        self.task_submit_callback = task_submit_callback  # Initialize callback function

        # initialize button
        self.back_to_mainButton()
        self.add_task()

    def back_to_mainButton(self):
        self.back_button = IconButton(
            icon=icons.ARROW_BACK,
            on_click=lambda e: self.page.go('/')
        )
        self.update_value = True

    def add_task(self):
        self.New_task_category = TextField(
            hint_text="Category Type",
            expand=True,
            border_color="black",
            width=300
        )

        self.New_task_name = TextField(
            hint_text="Task Name",
            expand=True,
            border_color="black",
            width=300
        )

    def submit(self):
        task_name = self.New_task_name.value
        category_name = self.New_task_category.value
        if task_name:
            # Callback to update tasks in Main_Frame
            if self.task_submit_callback:
                self.task_submit_callback(task_name, category_name)  # Pass the category here
                self.page.go('/')
            self.New_task_category.value = ""
            self.New_task_name.value = ""

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
                        ],
                    ),
                    Container(
                        content=self.New_task_category,
                        padding=padding.only(left=40, top=50),
                    ),
                    Container(
                        content=self.New_task_name,
                        padding=padding.only(left=40, top=50),
                    ),
                    Container(
                        padding=padding.only(left=80, top=50),
                        content=ElevatedButton(
                            "Submit Task",
                            width=200,
                            bgcolor="blue",
                            on_click=lambda e: self.submit()
                        )
                    )
                ]
            )
        )
