from iommi import Table, Form, Column, Action
from ui.pages import BasePage
from schema import models

class ManufacturerListPage(BasePage):
    table = Table(
        auto__model=models.Manufacturer,
        query_from_indexes=True,
        actions__create_manufacturer=Action(
            attrs__href='/ui/manufacturer/create/',
            include=lambda request, **_: request.user.is_staff,
        ),
        columns__edit=Column.edit(
            after=0,
            include=lambda request, **_: request.user.is_staff,
        ),
    )
