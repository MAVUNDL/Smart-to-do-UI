from flet import *
from create_task import *
from AllFunctionality import *


def function(page) -> dict:
    # dictionary containing the view pages
    Pages_ = {
        '/': View(
            "/",
            [
                page.controls[0]
            ]
        ),
        '/create_task': View(
            "/create_task",
            [
                Task_section()
            ]
        )
    }
    return Pages_


# creating routing functionality
def route_change(event):
    event.page.views.clear()
    main_container = event.page.controls[0]
    event.page.views.append(
        function(event.page)[event.page.route]
    )
    event.page.update()
