from iommi import Table, Form, Column, Action
from django.utils.html import format_html
from ui.pages import BasePage
from schema import models

class ManufacturerListPage(BasePage):
    table = Table(
        auto__model=models.Manufacturer,
        columns__name__cell__url=lambda row, **_: row.get_absolute_url(),
        columns__country__cell__format=lambda row, **_: format_html("{} <img src=\"{}\">", row.country.name, row.country.flag),
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
