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
                Task_section(task_submit_callback=page.main_frame.update_task_listing)  # Pass the callback here
            ]
        )
    }
    return Pages_


# creating routing functionality
def route_change(event):
    event.page.views.clear()
    event.page.views.append(
        function(event.page).get(event.page.route, function(event.page)['/'])  # Use a default route if not found
    )
    event.page.update()
