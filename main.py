from flet import *

def main(page:Page):
    rows = Column() # use a column instead of a row
    def plus_one(e):
        text_field = TextField() # create a new text field
        rows.controls.append(text_field) # append it to the column
        rows.update()
        page.client_storage.set('num_text_fields', len(rows.controls)) # save the number of text fields
        print(1)
    button = IconButton(icon=icons.PLUS_ONE,on_click=plus_one)
    page.add(button, rows) # only add the button and the column to the page

    num_icons = 0 # keep track of the number of icons added
    def add_icons(e):
        nonlocal num_icons
        my_icon=IconButton(icon=icons.FOLLOW_THE_SIGNS_ROUNDED)
        page.add(my_icon)
        page.update()
        num_icons += 1 # increment the number of icons added
        page.client_storage.set('num_icons', num_icons) # save the number of icons added
    icon_button=IconButton(icon=icons.FORWARD,on_click=add_icons)
    page.add(icon_button)

    # restore the state of the rows column if it exists
    num_text_fields = page.client_storage.get('num_text_fields')
    if num_text_fields:
        for _ in range(num_text_fields):
            text_field = TextField()
            rows.controls.append(text_field)
        rows.update()

    # restore the state of the icons if it exists
    num_icons = page.client_storage.get('num_icons')
    if num_icons is None:
        num_icons = 0
    if num_icons:
        for _ in range(num_icons):
            my_icon = IconButton(icon=icons.FOLLOW_THE_SIGNS_ROUNDED)
            page.add(my_icon)
import flet as flet

flet.app(target=main,view='web_browser')
